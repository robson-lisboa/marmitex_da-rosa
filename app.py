from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# --- CONFIGURAÇÕES DO SEU NEGÓCIO ---
# Link do seu iFood para onde o cliente será enviado
IFOOD_LINK = "https://www.ifood.com.br/delivery/mogi-das-cruzes-sp/marmitex-da-rosa---sabor-jardim-marica/0c36497f-001e-4a37-ae6d-e57d04370966"

# Nome exato do ficheiro da imagem que está no seu GitHub
NOME_DO_ARQUIVO_LOGO = "logo.png" 

@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="3;url={IFOOD_LINK}" />
        <title>Marmitex da Rosa - Comida Caseira</title>
        <style>
            body {{
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #FFC107; /* Amarelo do logótipo */
                color: #0D214F; /* Azul do logótipo */
                text-align: center;
            }}
            .card {{
                background: white;
                padding: 40px 20px;
                border-radius: 30px;
                box-shadow: 0 15px 35px rgba(0,0,0,0.2);
                max-width: 350px;
                width: 90%;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            img.logo {{
                width: 150px;
                height: auto;
                margin-bottom: 20px;
            }}
            h1 {{ font-size: 1.6rem; margin: 10px 0; }}
            p {{ font-size: 1rem; color: #555; margin-bottom: 25px; }}
            .botao {{
                display: inline-block;
                width: 100%;
                padding: 15px;
                background-color: #EA1D2C; /* Vermelho iFood */
                color: white;
                text-decoration: none;
                font-weight: bold;
                border-radius: 12px;
                transition: transform 0.2s;
            }}
            .botao:hover {{ transform: scale(1.05); }}
        </style>
    </head>
    <body>
        <div class="card">
            <img src="/imagem-logo" alt="Logo Marmitex da Rosa" class="logo">
            <h1>Almoço disponível! 🍛</h1>
            <p>Estamos a levar-te para o cardápio no iFood...</p>
            <a href="{IFOOD_LINK}" class="botao">ABRIR IFOOD AGORA</a>
        </div>
    </body>
    </html>
    """

# ROTA PARA O LOGÓTIPO: Faz com que o Render encontre a imagem no GitHub
@app.route("/imagem-logo")
def servir_logo():
    return send_from_directory(os.getcwd(), NOME_DO_ARQUIVO_LOGO)

# ROTA DE PING: Resposta rápida para o UptimeRobot saber que o site está vivo
@app.route("/ping")
def ping():
    return "OK", 200

if __name__ == "__main__":
    # Define a porta 10000 exigida pelo Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
