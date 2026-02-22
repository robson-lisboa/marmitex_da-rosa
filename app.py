from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# --- CONFIGURAÇÕES DO SEU NEGÓCIO ---
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
        <title>Marmitex da Rosa - Comida Caseira</title>
        <style>
            * {{
                box-sizing: border-box;
            }}
            body {{
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
                background-color: #FFC107; /* Amarelo Vibrante do seu Logo */
                color: #0D214F; /* Azul Escuro do seu Logo */
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
            .logo-container {{
                width: 150px;
                height: 150px;
                margin-bottom: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            img.logo {{
                max-width: 100%;
                height: auto;
            }}
            h1 {{
                font-size: 1.6rem;
                margin: 10px 0;
            }}
            p {{
                font-size: 1rem;
                color: #555;
                margin-bottom: 25px;
            }}
            .botao {{
                display: inline-block;
                width: 100%;
                padding: 15px;
                background-color: #EA1D2C; /* Vermelho iFood */
                color: white;
                text-decoration: none;
                font-weight: bold;
                font-size: 1.1rem;
                border-radius: 12px;
                transition: transform 0.2s, background-color 0.2s;
            }}
            .botao:hover {{
                background-color: #d91a2a;
                transform: scale(1.02);
            }}
            .footer-text {{
                margin-top: 15px;
                font-size: 0.8rem;
                color: #888;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="logo-container">
                <img src="/imagem-logo" alt="Logo Marmitex da Rosa" class="logo">
            </div>
            <h1>Almoço disponível! 🍛</h1>
            <p>Estamos te levando para o cardápio da Rosa no iFood...</p>
            
            <a href="{IFOOD_LINK}" class="botao">ABRIR IFOOD AGORA</a>
            
            <span class="footer-text">Redirecionando em 3 segundos...</span>
        </div>
    </body>
    </html>
    """

# ROTA PARA O SERVIDOR ENCONTRAR O ARQUIVO logo.png NO GITHUB/RENDER
@app.route("/imagem-logo")
def servir_logo():
    return send_from_directory(os.getcwd(), NOME_DO_ARQUIVO_LOGO)

if __name__ == "__main__":
    # O Render usa a variável de ambiente PORT, se não houver, usa 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
