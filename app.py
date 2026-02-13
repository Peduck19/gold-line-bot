from flask import Flask, request
import requests
import os

app = Flask(__name__)

LINE_NOTIFY_TOKEN = "ใส่_tokenจริงของคุณ"

def send_line(msg):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": f"Bearer {LINE_NOTIFY_TOKEN}"
    }
    data = {"message": msg}
    requests.post(url, headers=headers, data=data)

@app.route("/", methods=["GET"])
def home():
    return "Gold Line Bot is running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    price = float(data.get("price", 0))

    msg = f"ราคามาถึง {price:.0f} เตรียมตัว 🚨🚨"
    send_line(msg)
    send_line(msg)

    print(data)
    return "OK"
import os

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
