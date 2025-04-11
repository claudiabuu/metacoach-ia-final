from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

@app.route("/metacoach", methods=["POST"])
def metacoach():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Mensaje no proporcionado"}), 400
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un metacoach experto en PNL, neurociencia y coaching emocional. Eres cálido, inspirador y haces preguntas poderosas."},
                {"role": "user", "content": user_input}
            ]
        )
        metacoach_reply = response.choices[0].message.content
        return jsonify({"response": metacoach_reply})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

def handler(environ, start_response):
    return app(environ, start_response)