from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app) # This allows your HTML to talk to the API without "Busy" errors

VALID_KEYS = ["SAVAGE-123", "ADMIN-007"]

@app.route('/check', methods=['POST'])
def check_roblox():
    data = request.json
    username = data.get("username")
    license_key = data.get("key")

    if license_key not in VALID_KEYS:
        return jsonify({"error": "INVALID_LICENSE"}), 403
    
    # Roblox API
    url = f"https://auth.roblox.com/v1/usernames/validate?username={username}&birthday=2004-10-10"
    
    try:
        response = requests.get(url, timeout=5)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": "ROBLOX_TIMEOUT"}), 500

if __name__ == "__main__":
    # Railway uses the PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
