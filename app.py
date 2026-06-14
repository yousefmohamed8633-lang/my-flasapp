import os
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# تهيئة العميل (سيقرأ المفتاح تلقائياً من إعدادات Vercel التي سنضبطها)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/ask', methods=['POST'])
def ask_ai():
    data = request.json
    user_query = data.get("question", "")
    
    if not user_query:
        return jsonify({"error": "الرجاء إرسال سؤال"}), 400

    # إرسال الطلب للذكاء الاصطناعي
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # أو gpt-4
            messages=[{"role": "user", "content": user_query}]
        )
        answer = response.choices[0].message.content
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
