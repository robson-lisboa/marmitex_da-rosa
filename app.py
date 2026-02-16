@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <meta http-equiv="refresh" content="2;url={IFOOD_LINK}" />
        <title>Marmitex da Rosa</title>
        <style>
            body {{
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(to bottom, #fffae3, #ffe0b2);
                color: #333;
            }}
            h1 {{
                font-size: 2.5rem;
                margin-bottom: 20px;
            }}
            p {{
                font-size: 1.2rem;
            }}
            a {{
                display: inline-block;
                margin-top: 15px;
                padding: 10px 20px;
                background-color: #ff5722;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s;
            }}
            a:hover {{
                background-color: #e64a19;
            }}
        </style>
    </head>
    <body>
        <h1>🍛 Marmitex da Rosa</h1>
        <p>Redirecionando para o iFood...</p>
        <a href="{IFOOD_LINK}">Peça agora no iFood</a>
    </body>
    </html>
    """
