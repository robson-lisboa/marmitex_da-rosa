from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# --- CONFIGURAÇÕES ---
IFOOD_LINK = "https://www.ifood.com.br/delivery/mogi-das-cruzes-sp/marmitex-da-rosa---sabor-jardim-marica/0c36497f-001e-4a37-ae6d-e57d04370966"
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
        <title>Marmitex da Rosa</title>
        <style>
            body {{
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: sans-serif;
                background-color: #FFC107;
                color: #0D214F;
                text-align: center;
            }}
            .card {{
                background: white;
                padding: 30px;
                border-radius: 25px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                width: 280px;
            }}
            img.logo {{
                width: 150px;
                margin-bottom: 15px;
            }}
            .btn {{
                display: block;
                padding: 12px;
                background-color: #EA1D2C;
                color: white;
                text-decoration: none;
                font-weight: bold;
                border-radius: 8px;
                margin-top: 15px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <img src="/imagem-logo" alt="Marmitex da Rosa" class="logo">
            <h2 style="margin: 0;">Quase lá! 🍛</h2>
            <p style="font-size: 0.9rem; color: #666;">Estamos te levando para o iFood...</p>
            <a href="{IFOOD_LINK}" class="btn">VER CARDÁPIO</a>
        </div>
    </body>
    </html>
    """

@app.route("/imagem-logo")
def servir_logo():
    # Isso busca o logo.png na pasta principal do seu GitHub
    return send_from_directory(os.getcwd(), NOME_DO_ARQUIVO_LOGO)

if __name__ == "__main__":
    # Ajuste crucial para o Render parar de dar erro de porta
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
