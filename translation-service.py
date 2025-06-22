from flask import Flask, request, jsonify
from dotenv import load_dotenv
from google import genai
from PIL import Image
import io
import arabic_reshaper

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# The new SDK picks up the API key from the GOOGLE_API_KEY environment variable
client = genai.Client()

@app.route('/assistant', methods=['POST'])
def assistant():
    task = request.form.get('task')
    language = request.form.get('language')

    image_file = request.files.get('image')
    text = request.form.get('text')

    if not task:
        task = 'translate'
    if not language:
        language = "Arabic"

    # Prepare contents for Gemini API
    contents = []
    if task == 'translate':
        contents.append(
            f"""
            This is an image (jpg, png, jpeg, etc) of an object. Tell me 
            what this is in ${language}. Don't include any extra words in your 
            response -- only what the object is in the ${language} language (no 
            unnecessary descriptions). Choose the colloquial response from the  
            most common region if the language encompasses multiple regions. We 
            want to ensure the translation is as accurate as possible.
            """
        )
    elif task == 'medication':
        contents.append(
            """
            Explain the medication (name, what its for) and instructions 
            shown in this image (jpeg, png, jpeg, etc). When explaining what 
            its for, briefly explain the 3 most common uses
            """
        )
    elif task == 'emergency':
        contents.append("Describe the emergency in this image or text.")
    else:
        contents.append("Describe this image.")

    # Add image if present
    if image_file:
        img = Image.open(io.BytesIO(image_file.read()))
        contents.append(img)
    elif text:
        contents.append(text)

    # Call Gemini API
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=contents
    )

    translated_response = response.text
    # Reverse the output if it's a right-to-left written language
    if (language.lower() in 
        {
            "arabic",
            "aramaic",
            "azeri", 
            "dhivehi", "maldivian",
            "hebrew",
            "kurdish", "sorani",
            "persian", "farsi",
            "urdu"
        }
    ):
        translated_response = response.text[::-1]
    
    if language.lower() == "arabic":
        translated_response = arabic_reshaper.reshape(translated_response)

    print(translated_response)
    return jsonify({'result': translated_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
