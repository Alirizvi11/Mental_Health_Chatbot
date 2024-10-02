from flask import Flask, request, jsonify
from langchain_google_genai import ChatGoogleGenerativeAI

app = Flask(__name__)
gemini = ChatGoogleGenerativeAI (api_key='AIzaSyDk0gH6pFP35-XHZh6ON8M7kBdE_fniIYA')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = gemini.generate_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)