from flask import Flask, request, jsonify
from dotenv import load_dotenv
from google import genai
from PIL import Image
import io

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# The new SDK picks up the API key from the GOOGLE_API_KEY environment variable
client = genai.Client()

@app.route('/evaluate', methods=['POST'])
def evaluate():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    image = Image.open(image_file.stream)
    
    contents = [
        """
        You are a productivity assistant. You are expected to determine whether the user is being productive or not productive based on a given snapshot of a POV video feed.

        Examples of productive snapshot:
            - code sessions
            - writing essays on word/google docs
            - doing homework
            - folding laundry
            - vacuuming

        Examples of a non-productive snapshot:
            - watching YouTube/Netflix
            - Going on social media (TikTok, SnapChat, Instagram, Facebook, etc)
            - looking away from your computer or paper on desk

        if user is productive, return 'on-task', else return 'off-task'
        """,
        image
    ]
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=contents
    )
    result = response.text.strip().lower()
    if "off" in result:
        return "off-task"
    return "on-task"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)