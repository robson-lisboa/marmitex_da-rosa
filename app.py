from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Configurações de links
IFOOD_LINK = "https://www.ifood.com.br/delivery/mogi-das-cruzes-sp/marmitex-da-rosa---sabor-jardim-marica/0c36497f-001e-4a37-ae6d-e57d04370966"
NOME_DO_ARQUIVO_LOGO = "logo.png" # Certifique-se que o nome no GitHub seja igual a este

@app.route("/")
def home():
    return f"""
    <html>
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
                font-family: 'Arial', sans-serif;
                background-color: #FFC107; /* Amarelo do logo */
                color: #0D214F; /* Azul do logo */
                text-align: center;
            }}
            .card {{
                background: white;
                padding: 40px;
                border-radius: 30px;
                box-shadow: 0 15px 35px rgba(0,0,0,0.2);
                max-width: 320px;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            img.logo {{
                width: 180px;
                height: auto;
                margin-bottom: 20px;
                border-radius: 50%;
            }}
            h1 {{ font-size: 1.5rem; margin-bottom: 10px; }}
            p {{ color: #666; margin-bottom: 20px; }}
            .botao {{
                display: block;
                padding: 15px 25px;
                background-color: #EA1D2C; /* Vermelho iFood */
                color: white;
                text-decoration: none;
                font-weight: bold;
                border-radius: 10px;
                transition: 0.3s;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <img src="/imagem-logo" alt="Logo Marmitex da Rosa" class="logo">
            <h1>Almoço saindo! 🍛</h1>
            <p>Aguarde um instante, estamos te levando para o cardápio...</p>
            <a href="{IFOOD_LINK}" class="botao">ABRIR IFOOD AGORA</a>
        </div>
    </body>
    </html>
    """

# Rota para servir a imagem do seu repositório
@app.route("/imagem-logo")
def servir_logo():
    return send_from_directory(os.getcwd(), NOME_DO_ARQUIVO_LOGO)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

