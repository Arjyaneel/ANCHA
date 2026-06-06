from flask import Flask, request, jsonify
from flask_cors import CORS

from app.ai.gemini_service import analyze_emotion
from app.ai.memory_extractor import extract_memory

from app.database.models import save_entry
from app.database.memory_model import save_memory

from app.database.user_model import (
    create_user,
    get_user_by_username
)

from app.services.context_builder import build_user_context
from app.services.dashboard_service import get_dashboard_data

print("APP FILE LOADED")

app = Flask(__name__)
CORS(app)



@app.route("/")
def home():
    return "Ancha Backend Running"




@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok"
    })




@app.route("/register", methods=["POST"])
def register():

    try:

        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        existing_user = get_user_by_username(username)

        if existing_user:

            return jsonify({
                "error": "Username already exists"
            }), 400

        user_id = create_user(
            username,
            password
        )

        return jsonify({
            "message": "User registered successfully",
            "user_id": user_id
        })

    except Exception as e:

        print("REGISTER ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 500




@app.route("/login", methods=["POST"])
def login():

    try:

        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        user = get_user_by_username(username)

        if not user:

            return jsonify({
                "error": "User not found"
            }), 404

        if user["password"] != password:

            return jsonify({
                "error": "Invalid password"
            }), 401

        return jsonify({
            "message": "Login successful",
            "user_id": user["id"],
            "username": user["username"]
        })

    except Exception as e:

        print("LOGIN ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 500




@app.route("/dashboard/<int:user_id>", methods=["GET"])
def dashboard(user_id):

    data = get_dashboard_data(user_id)

    return jsonify(data)




@app.route("/analyze", methods=["POST"])
def analyze():

    try:

        data = request.get_json()

        text = data.get("text", "")

        user_id = data.get("user_id")

        if not user_id:

            return jsonify({
                "error": "User not logged in"
            }), 401

        print("USER ID:", user_id)

        context = build_user_context(user_id)

        print("\nCONTEXT SENT TO GEMINI:\n")
        print(context)

        ai_response = analyze_emotion(
            text,
            context
        )

        print("AI RESPONSE:", ai_response)

        

        memory = extract_memory(text)

        print("MEMORY EXTRACTED:", memory)

        if memory["should_save"]:

            save_memory(
                user_id,
                memory["memory_type"],
                memory["memory_content"],
                memory["importance_score"]
            )

            print("NEW MEMORY SAVED")

        print("MEMORY SAVED")

       

        save_entry(
            user_id,
            text,
            ai_response["emotion"],
            ai_response["energy_level"],
            ai_response["mood_summary"],
            ai_response["support_response"],
            str(ai_response["tips"])
        )

        print("INSERT SUCCESSFUL")

        return jsonify(ai_response)

    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "error": "Something went wrong while analyzing the message."
        }), 500



if __name__ == "__main__":

    app.run(
        port=5000,
        debug=True
    )