from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Route to serve your frontend webpage
@app.route('/')
def home():
    return render_template('index.html')

# Python API endpoint to process mobile translation queries securely
@app.route('/api/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text', '')
    lang_pair = data.get('langpair', 'en|es')
    
    try:
        url = f"https://api.mymemory.translated.net/get?q={requests.utils.quote(text)}&langpair={lang_pair}"
        response = requests.get(url, timeout=10)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Runs the server on port 5000, open to network mapping
    app.run(host='0.0.0.0', port=5000, debug=True)