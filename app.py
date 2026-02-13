from flask import Flask, request

app = Flask(_name_)

@app.route("/", methods=["GET"])
def home():
    return "Gold Line Bot is running"
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    
    symbol = data.get("symbol", "Asset")
    price = float(data.get("price", 0))
    target = float(data.get("target", 0))

    message = f"{symbol} มาถึงราคา {price} ใกล้ถึงจุดเข้าที่ {target} แล้ว"

    print(message)
    print(data)
    return "OK"
import os

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
