from flask import Flask, request
import requests
import threading
import time
import os

app = Flask(_name_)

# ===== ใส่ LINE TOKEN ของคุณ =====
LINE_NOTIFY_TOKEN = "ใส่_tokenจริงของคุณ"

# ===== รายการจุดเตือน =====
alerts = []

# ===== ส่งข้อความไป LINE =====
def send_line(msg):
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {LINE_NOTIFY_TOKEN}"}
    requests.post(url, headers=headers, data={"message": msg})

# ===== ดึงราคาทอง =====
def get_price(symbol):
    try:
        base = symbol[:3]
        quote = symbol[3:]
        r = requests.get(
            f"https://metals-api.com/api/latest?base={base}&symbols={quote}"
        )
        data = r.json()
        if data.get("rates") and quote in data["rates"]:
            return float(data["rates"][quote])
    except:
        return None
    return None

# ===== ตัวตรวจราคาทำงานตลอด =====
def price_watcher():
    while True:
        try:
            for a in alerts[:]:
                price = get_price(a["symbol"])
                if price is None:
                    continue

                if price >= a["alert"]:
                    msg = f'{a["symbol"]} มาถึง {round(price,2)} ใกล้จุดเข้า {a["target"]} แล้ว'
                    send_line(msg)
                    alerts.remove(a)

        except Exception as e:
            print("watcher error:", e)

        time.sleep(20)

# ===== เริ่มตัวตรวจราคา =====
threading.Thread(target=price_watcher, daemon=True).start()

# ===== หน้าเช็คสถานะ =====
@app.route("/", methods=["GET"])
def home():
    return "Gold Line Bot is running"

# ===== รับคำสั่งจาก LINE =====
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    text = data.get("text", "")

    # ตัวอย่างคำสั่ง: SET XAUUSD 5105 5100
    if text.startswith("SET"):
        _, symbol, alert, target = text.split()
        alerts.append({
            "symbol": symbol,
            "alert": float(alert),
            "target": float(target)
        })
        send_line(f"ตั้งเตือน {symbol} ที่ {alert} (เป้า {target}) แล้ว")

    return "OK"

# ===== รันเซิร์ฟเวอร์ =====
if _name_ == "_main_":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
