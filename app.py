from flask import Flask, request
import requests
import time
import os

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = "iSwVH5bbcYAoVCdL4bQp2OJKzxFsuDXICbnLTMw3IRHW/9p/Bbrm4PXjm9h95ngPSL/qxWb3bXOmIjKuXFsD0IfD8JgmgDPvVmEIM7/KEDCZfqaz6leMooVpTnl0C07pALmUtCIpShP5qg0tggBZVAdB04t89/1O/w1cDnyilFU="
GROUP_ID = "ใส่_groupId_ของกลุ่ม"

def send_line(msg):
    url = "https://notify-api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {iSwVH5bbcYAoVCdL4bQp2OJKzxFsuDXICbnLTMw3IRHW/9p/Bbrm4PXjm9h95ngPSL/qxWb3bXOmIjKuXFsD0IfD8JgmgDPvVmEIM7/KEDCZfqaz6leMooVpTnl0C07pALmUtCIpShP5qg0tggBZVAdB04t89/1O/w1cDnyilFU=}"
    }
    data = {
        "to": GROUP_ID,
        "messages": [
            {"type": "text", "text": msg}
        ]
    }
    
        r = requests.post(url, headers=headers, json=data)
    print("LINE:", r.status_code, r.text)

@app.route("/")
def home():
    return "Bot is running"

# 🔹 TradingView ยิงมาที่นี่
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    price = float(data.get("price", 0))

    msg = f"ราคามาถึง {price:.0f} เตรียมตัว 🚨"
    send_line(msg)
    time.sleep(2)
    send_line(msg)

    return "OK"

# 🔹 LINE ใช้ verify เท่านั้น
@app.route("/callback", methods=["POST"])
def callback():
    return "OK"

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
