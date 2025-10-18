from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html lang='tr'>
    <head><meta charset='UTF-8'><title>Ana Sayfa</title></head>
    <body>
      <h1>Ana Sayfaya Hoş Geldin</h1>
      <a href='/about'>Hakkında</a> |
      <a href='/secret-coin'>Yazı Tura</a> |
      <a href='/secret-password'>Şifre Oluşturucu</a> |
      <a href='/secret-sunset'>Gün Batımı Motivasyon 😑</a>
    </body>
    </html>
    """

@app.route("/about")
def about():
    return """
    <html lang='tr'>
    <head><meta charset='UTF-8'><title>Hakkında</title></head>
    <body>
      <h1>Bu site Flask ile yazıldı.</h1>
      <a href='/'>Ana Sayfa</a>
    </body>
    </html>
    """

@app.route("/secret-coin")
def secret_coin():
    coin = random.choice(["Yazı", "Tura"])
    return f"""
    <html lang='tr'>
    <head><meta charset='UTF-8'><title>Yazı Tura</title></head>
    <body>
      <h1>Yazı Tura</h1>
      <p>Sonuç: <strong>{coin}</strong></p>
      <a href='/'>Ana Sayfa</a>
    </body>
    </html>
    """

@app.route("/secret-password")
def secret_password():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""
    for i in range(10):
        password = password + random.choice(letters)
    return f"""
    <html lang='tr'>
    <head><meta charset='UTF-8'><title>Şifre Oluşturucu</title></head>
    <body>
      <h1>Rastgele Şifre</h1>
      <p>Şifren: <strong>{password}</strong></p>
      <a href='/'>Ana Sayfa</a>
    </body>
    </html>
    """

@app.route("/secret-sunset")
def secret_sunset():
    messages = [
        "Güneş batıyor, ama umut doğuyor.",
        "Her batış bir başlangıcın habercisidir.",
        "Bugün güzel geçti, yarın daha da güzel olabilir."
    ]
    message = random.choice(messages)
    return f"""
    <html lang='tr'>
    <head><meta charset='UTF-8'><title>Gün Batımı Motivasyon 😑</title></head>
    <body>
      <h1>Gün Batımı Motivasyon 😑</h1>
      <p>{message}</p>
      <a href='/'>Ana Sayfa</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
