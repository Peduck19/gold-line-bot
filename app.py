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

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=10000)
