import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
# This allows your frontend (GitHub Pages) to securely talk to this backend
CORS(app, resources={r"/*": {"origins": "*"}})

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

@app.route('/translate', methods=['POST'])
def translate():
    # Automatically pulls the key from Render's secure settings environment variable
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        return jsonify({"error": "Backend configuration error: API Key missing."}), 500

    try:
        data = request.json
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # Forward the data directly to Groq
        response = requests.post(GROQ_API_URL, json=data, headers=headers)
        return jsonify(response.json()), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Use the port assigned by Render dynamically
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)