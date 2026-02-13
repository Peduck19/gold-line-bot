from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Gold Line Bot is running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print(data)
    return "OK"
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
