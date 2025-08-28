from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# ====== SETUP YOUR GEMINI API KEY ======
# Get API key from environment variable or use the one in the code
api_key = os.getenv('GEMINI_API_KEY', "AIzaSyDivzUH14d7q2HgwR-cH-BupK7xdBiJFpk")
genai.configure(api_key=api_key)

# ====== OWL AI RESPONSE ======
def owl_ai_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"You are a helpful and knowledgeable AI assistant named Owl. Answer the following question clearly and concisely:\n\n{user_input}"
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"

# ====== ROUTES ======
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_owl():
    try:
        user_question = request.json.get('question')
        if not user_question:
            return jsonify({'response': 'Please provide a question.'}), 400
        
        answer = owl_ai_response(user_question)
        return jsonify({'response': answer})
    except Exception as e:
        return jsonify({'response': f'Error processing request: {str(e)}'}), 500

if __name__ == '__main__':
    print("🦉 Owl AI Chat is starting...")
    print("Make sure you have set your GEMINI_API_KEY in the .env file or in the code")
    app.run(debug=True, host='0.0.0.0', port=5000)
