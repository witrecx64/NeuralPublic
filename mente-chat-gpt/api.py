from flask import Flask, request, jsonify
import main as mt

app = Flask(__name__)

@app.route("api/chatbot", methods=['POST'])

def chatbot():
    data = request.get_json()
    question = data['question']
    response = mt.pregunta(question)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
