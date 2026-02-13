from flask import Flask, request

app = Flask(_name_)

@app.route("/", methods=["GET"])
def home():
    return "Gold Line Bot is running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print(data)
    return "OK"
