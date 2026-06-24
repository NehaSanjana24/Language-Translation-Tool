import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
# Allows your GitHub Pages frontend to communicate with this backend securely
CORS(app, resources={r"/*": {"origins": "*"}})

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

@app.route('/translate', methods=['POST'])
def translate():
    # Safely fetches the key from Render's Environment Variables
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        return jsonify({"error": "Backend configuration error: API Key missing on Render settings."}), 500

    try:
        data = request.json
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # Forward the instructions directly to the Groq Llama-3 compiler
        response = requests.post(GROQ_API_URL, json=data, headers=headers)
        return jsonify(response.json()), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Binds dynamically to Render's allocated port system
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)