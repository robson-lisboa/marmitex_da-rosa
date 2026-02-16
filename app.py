from flask import Flask, redirect
import time

app = Flask(__name__)

IFOOD_LINK = "COLE_AQUI_O_LINK_DO_IFOOD"

@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <meta http-equiv="refresh" content="2;url={IFOOD_LINK}" />
    </head>
    <body style="text-align:center;margin-top:100px;font-family:Arial;">
        <h1>🍛 Almoço disponível!</h1>
        <p>Redirecionando para o iFood...</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
