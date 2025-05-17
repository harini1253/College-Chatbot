# app.py
from flask import Flask, request, jsonify, render_template
from chatbot import get_bot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message")
    response = get_bot_response(message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)



