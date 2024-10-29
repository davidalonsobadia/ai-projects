from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)

CORS(app)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_API_URL = 'https://api.openai.com/v1/chat/completions'

# This is not working because we need to pay for the calls done to OPEN AI - GPT Model
@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    prompt = data.get('prompt')

    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        'model': 'gpt-4o-mini', 
        'prompt': prompt,
        'max_tokens': 150
    }
    response = requests.post(OPENAI_API_URL, headers=headers, json=payload)
    print(response.json())
    
    if response.status_code == 200:
        print(response)
        result = response.json()
        generated_text = result['choices'][0]['text'].strip()
        return jsonify({'generated_text': generated_text})
    else:
        return jsonify({'error': 'Error en la generación de texto'}), response.status_code

if __name__ == '__main__':
    app.run(port=5000)
