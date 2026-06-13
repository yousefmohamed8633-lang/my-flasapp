from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "عظيم جداً! السيرفر المحلي يعمل بنجاح على هاتفك."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
