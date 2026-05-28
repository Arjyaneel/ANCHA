from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend calls during development

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/analyze", methods=["POST"])
def analyze():
    # Placeholder: later you will add emotion + sentiment logic
    data = request.get_json()
    text = data.get("text", "")
    # Temporary fake response:
    return jsonify({
        "face_emotion": "neutral",
        "text_sentiment": "neutral",
        "mood_summary": "Placeholder summary",
        "tips": ["This is just a placeholder. AI logic will be added here."]
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)