from flask import Flask
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>ARAPP SYSTEM - Sistem Garage</title>
<style>
body{font-family:sans-serif;background:#111;padding:16px;margin:0;color:#111}
.box{background:white;padding:22px;border-radius:16px;text-align:center;max-width:420px;margin:20px auto}
.btn{display:block;background:#111;color:white;padding:16px;border-radius:10px;text-decoration:none;font-weight:bold;font-size:18px;margin-top:12px}
.btn-green{display:block;background:#25D366;color:white;padding:14px;border-radius:10px;text-decoration:none;font-weight:bold;margin-top:10px}
.btn-purple{display:block;background:#673ab7;color:white;padding:14px;border-radius:10px;text-decoration:none;font-weight:bold;margin-top:10px}
.card{background:#f4f4f4;padding:14px;border-radius:12px;margin-top:12px;text-align:left}
.small{font-size:12px;color:#888}
</style></head><body>
<div class="box">
<h1>🏍️ ARAPP SYSTEM</h1>
<p style="margin-top:-10px">Sistem Pengurusan Bengkel Motor</p>
<h2 style="color:red">Trial 7 Hari FREE</h2>
<h1 style="font-size:42px">RM49 <span style="font-size:16px">/ Bulan</span></h1>
<p style="text-align:left">✅ Unlimited Motor Masuk<br>✅ Unlimited Pomen<br>✅ Approval Tokey<br>✅ WhatsApp Customer Auto<br>✅ Rekod Duit Harian<br>✅ Arkib Motor Lama</p>
<a class="btn" href="https://toyyibpay.com/Langanan-Bulanan">💳 BAYAR RM49 SEKARANG</a>
<a class="btn-green" href="https://wa.me/60123456789?text=Salam%20saya%20nak%20subscribe%20Arapp%20Garage%20RM49">📱 WHATSAPP ADMIN - NAK SUBSCRIBE</a>

<div class="card">
<h3 style="margin:0">🏪 Kedai Yang Dah Guna:</h3>
<p style="margin:8px 0">🔥 <b>BOTTOL GARAGE</b> - Aktif</p>
<a class="btn-purple" href="https://bottol-garage.onrender.com">➡️ MASUK BOTTOL GARAGE</a>
<p class="small">Link ni khas untuk staff Bottol Garage sahaja. Kedai lain tak boleh access data Bottol.</p>
</div>

<div class="card">
<h3 style="margin:0">❓ Macam mana nak ada link kedai sendiri?</h3>
<p>1. WhatsApp Admin<br>2. Bayar RM49<br>3. Admin buatkan link kedai kau sendiri<br>Contoh: <b>ali-garage.onrender.com</b></p>
<a class="btn-green" href="https://wa.me/60123456789?text=Salam%20saya%20nak%20buka%20link%20kedai%20sendiri">📱 NAK BUKA KEDAI SENDIRI</a>
</div>

<p class="small">© 2026 ARAPP SYSTEM Garage</p>
</div></body></html>
"""

@app.route("/")
def index():
    return HTML

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
