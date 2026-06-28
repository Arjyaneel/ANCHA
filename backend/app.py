
from time import time

from app.services.conversation_service import (
    process_message
)

from flask import (
    Flask,
    Response,
    jsonify,
    request,
    stream_with_context,
)
from flask_cors import CORS


from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from app.database.user_model import (
    create_user,
    get_user_by_username
)
from app.ai.gemini_service import (
    stream_ancha_response
)
from app.services.ai_context_service import build_user_context
from app.services.dashboard_service import get_dashboard_data
from app.database.memory_model import (
    get_top_memories
)

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



@app.route("/analyze-stream", methods=["POST"])
def analyze_stream():

    start = time()

    data = request.get_json()

    text = data.get("text", "")
    user_id = data.get("user_id")

    context = build_user_context(user_id)

    print(
        "CONTEXT BUILD TIME:",
        round(time() - start, 2),
        "seconds"
    )

    def generate():

        stream_start = time()

        first_chunk = True

        for chunk in stream_ancha_response(
            text,
            context
        ):

            if first_chunk:

                print(
                    "FIRST TOKEN TIME:",
                    round(
                        time() - stream_start,
                        2
                    ),
                    "seconds"
                )

                first_chunk = False

            yield chunk

    return Response(
        stream_with_context(
            generate()
        ),
        mimetype="text/plain"
    )

@app.route("/memory-data")
def memory_data():

    user_id = request.args.get(
        "user_id"
    )

    memories = get_top_memories(
        user_id,
        5
    )

    return jsonify({

        "memories": memories

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

        password_hash = generate_password_hash(password)

        user_id = create_user(
            username,
            password_hash
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

        if not check_password_hash(
            user["password_hash"],
            password
        ):

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

        user_id = data.get("user_id")
        text = data.get("text", "")

        if not user_id:

            return jsonify({
                "error": "User not logged in"
            }), 401

        ai_response = process_message(
            user_id,
            text
        )

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

