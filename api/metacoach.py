from flask import Request, jsonify
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def handler(request: Request):
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"error": "Mensaje no proporcionado"}), 400

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
        return jsonify({"error": str(e)}), 500
