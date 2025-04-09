from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API Key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=150,
            temperature=0.7
        )
        bot_message = response.choices[0].text.strip()
        return jsonify({'response': bot_message})

    except Exception as e:
        return jsonify({'response': f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
