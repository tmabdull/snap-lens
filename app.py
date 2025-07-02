from flask import Flask, request, jsonify
from dotenv import load_dotenv
from google import genai
from PIL import Image, UnidentifiedImageError
import io
import arabic_reshaper

load_dotenv()
app = Flask(__name__)

# Initialize Gemini client (API key from env)
client = genai.Client()

def handle_translation_response(response, language):
    """
    Helper to process the Gemini response text based on language.
    """
    
    text = getattr(response, 'text', None)
    if not text or not text.strip():
        return "No translation result."
    
    right_to_left_languages = {
        "arabic",
        "aramaic",
        "azeri", 
        "dhivehi", "maldivian",
        "hebrew",
        "kurdish", "sorani",
        "persian", "farsi",
        "urdu"
    }
    
    if (language.lower() in right_to_left_languages):
        text = text[::-1]

    if language.lower() == "arabic":
        text = arabic_reshaper.reshape(text)

    return text

@app.route('/translate', methods=['POST'])
def translate():
    image_file = request.files.get('image')
    language = request.form.get('language', 'English')

    prompt = (
        f"""
        This is an image (jpg, png, jpeg, etc) of some text. 
        Extract and translate the text to ${language}. 
        Don't include any extra words in your response -- only the 
        translation. 
        Account for colloqiual dialects in addition to the standard form of 
        the input language.
        If the text is formatted in a specific way with a series of items 
        (e.g. a foreign-language menu), translate each item and format the 
        response line by line so that the client can choose to print just 
        one item / line.
        """
    )

    contents = [prompt]

    if image_file:
        try:
            img = Image.open(io.BytesIO(image_file.read()))
            contents.append(img)
        except UnidentifiedImageError:
            return jsonify({'result': 'Invalid image file.'}), 400
    else:
        return jsonify({'result': 'No image file provided.'}), 400

    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=contents
        )

        translated = handle_translation_response(response, language)
        print("Translated Text:\n", translated)

        return jsonify({'result': translated})
    except Exception:
        return jsonify({'result': 'Translation failed.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
