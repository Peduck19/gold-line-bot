from flask import Flask, request
import requests
import os
import time

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = "iSwVH5bbcYAoVCdL4bQp2OJKzxFsuDXICbnLTMw3IRHW/9p/Bbrm4PXjm9h95ngPSL/qxWb3bXOmIjKuXFsD0IfD8JgmgDPvVmEIM7/KEDCZfqaz6leMooVpTnl0C07pALmUtCIpShP5qg0tggBZVAdB04t89/1O/w1cDnyilFU="
GROUP_ID = "ใส่_GROUP_ID"

def send_line(msg):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Authorization": "Bearer " + iSwVH5bbcYAoVCdL4bQp2OJKzxFsuDXICbnLTMw3IRHW/9p/Bbrm4PXjm9h95ngPSL/qxWb3bXOmIjKuXFsD0IfD8JgmgDPvVmEIM7/KEDCZfqaz6leMooVpTnl0C07pALmUtCIpShP5qg0tggBZVAdB04t89/1O/w1cDnyilFU=,
        "Content-Type": "application/json"
    }
    data = {
        "to": GROUP_ID,
        "messages": [{"type": "text", "text": msg}]
    }
    requests.post(url, headers=headers, json=data)

@app.route("/")
def home():
    return "Bot is running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    price = data.get("price", "ไม่มีราคา")

    msg = f"ราคาถึง {price} แล้ว"
    send_line(msg)
    time.sleep(2)
    send_line(msg)

    return "OK"

@app.route("/callback", methods=["POST"])
def callback():
    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
