from flask import Flask, send_from_directory
import os

app = Flask(__name__)

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
        <title>Marmitex da Rosa</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #FFC107;
                font-family: 'Segoe UI', Arial, sans-serif;
                color: #0D214F;
                overflow: hidden;
            }}

            .card {{
                background: white;
                padding: 40px 20px;
                border-radius: 30px;
                box-shadow: 0 15px 35px rgba(0,0,0,0.2);
                max-width: 350px;
                width: 85%;
                text-align: center;
            }}

            img.logo {{
                width: 160px;
                height: auto;
                margin-bottom: 20px;
                border-radius: 50%;
            }}

            #text {{
                font-size: 20px;
                line-height: 1.6;
                transition: opacity 0.2s ease;
                margin-bottom: 30px;
                min-height: 80px;
                font-weight: bold;
            }}

            .botao {{
                display: inline-block;
                padding: 16px 30px;
                font-size: 18px;
                background-color: #EA1D2C;
                color: white;
                text-decoration: none;
                font-weight: bold;
                border-radius: 12px;
                transition: transform 0.2s;
                box-shadow: 0 4px 15px rgba(234, 29, 44, 0.3);
            }}

            .botao:hover {{
                transform: scale(1.05);
            }}
        </style>
    </head>
    <body>

        <div class="card">
            <img src="/imagem-logo" alt="Logo Marmitex da Rosa" class="logo">
            <div id="text"></div>
            <a href="{IFOOD_LINK}" class="botao">VER CARDÁPIO NO IFOOD</a>
        </div>

        <script>
            const textElement = document.getElementById("text");

            const mensagens = [
                "Comida caseira de verdade. Peça agora! 🍛"
            ];

            let i = 0;

            function mudarTexto() {{
                if (i < mensagens.length) {{
                    textElement.style.opacity = 0;
                    setTimeout(() => {{
                        textElement.innerHTML = mensagens[i];
                        textElement.style.opacity = 1;
                        i++;
                        setTimeout(mudarTexto, 900);
                    }}, 300);
                }}
            }}

            window.onload = () => {{
                mudarTexto();

                setTimeout(() => {{
                    window.location.href = "{IFOOD_LINK}";
                }}, 5000);
            }};
        </script>

    </body>
    </html>
    """

@app.route("/imagem-logo")
def servir_logo():
    return send_from_directory(os.getcwd(), NOME_DO_ARQUIVO_LOGO)

@app.route("/ping")
def ping():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

