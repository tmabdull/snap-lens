from flask import Flask, request, jsonify
import requests
import urllib3

# Disable SSL warnings for self-signed certs (DEV ONLY!)
urllib3.disable_warnings()

app = Flask(__name__)

# HTTPS backend server (self-signed cert)
BACKEND_URL = 'https://localhost:3001/translate'

@app.route('/proxy-translate', methods=['POST'])
def proxy_translate():
    try:
        files = {'image': request.files['image']}
        data = {'language': request.form.get('language', 'English')}

        response = requests.post(
            BACKEND_URL,
            files=files,
            data=data,
            verify=False  # Allow self-signed cert (DEV ONLY)
        )
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({'error': 'Proxy failed', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
