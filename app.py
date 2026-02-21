from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Link do iFood (edite aqui se precisar trocar no futuro)
IFOOD_LINK = "https://www.ifood.com.br/delivery/mogi-das-cruzes-sp/marmitex-da-rosa---sabor-jardim-marica/0c36497f-001e-4a37-ae6d-e57d04370966"

HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />

  <!-- Redireciona para o iFood em 3 segundos -->
  <meta http-equiv="refresh" content="3;url={{ ifood_link }}">

  <title>Marmitex da Rosa</title>
  <meta name="description" content="Marmitex da Rosa - comida caseira em Mogi das Cruzes. Peça agora no iFood.">
  <meta name="robots" content="index,follow" />

  <style>
    body{
      display:flex;
      flex-direction:column;
      justify-content:center;
      align-items:center;
      height:100vh;
      margin:0;
      font-family:Arial, sans-serif;
      background:linear-gradient(to bottom,#fff8dc,#ffd8a8);
      text-align:center;
      color:#222;
      padding:16px;
    }
    h1{ font-size:2.5rem; margin-bottom:6px; }
    .frase{ font-size:1.2rem; margin-bottom:10px; }
    .versiculo{ font-size:0.95rem; opacity:0.85; margin-top:10px; }
    .contador{ margin-top:15px; font-size:0.95rem; opacity:0.8; }
    .cta {
      display:inline-block; margin-top:16px; padding:10px 18px;
      background:#ff5722; color:#fff; border-radius:8px; text-decoration:none;
    }
    .cta:hover { background:#e64a19; }
    noscript {
      display:block; margin-top:12px; font-size:0.95rem; color:#333;
      background:#fff3cd; border:1px solid #ffeeba; padding:8px 12px; border-radius:6px;
    }
  </style>
</head>

<body>
  <h1 id="titulo"></h1>
  <div class="frase" id="frase"></div>
  <div class="versiculo" id="versiculo"></div>
  <div class="contador" id="contador">Abrindo iFood em 3s...</div>

  <p>
    {{ ifood_link }}Abrir no iFood agora</a>
  </p>

  <noscript>
    O redirecionamento automático precisa de JavaScript.
    Se não abrir, copie e cole no navegador: {{ ifood_link }}
  </noscript>

  <script>
    const IFOOD_LINK = "{{ ifood_link }}";

    const versiculos = [
      "O Senhor é meu pastor. (Salmo 23:1)",
      "Tudo posso naquele que me fortalece. (Filipenses 4:13)",
      "Deus é amor. (1 João 4:8)",
      "Confia no Senhor. (Provérbios 3:5)",
      "O Senhor é bom. (Salmo 100:5)",
      "A paz esteja com vocês. (João 20:19)"
    ];

    const frases = [
      "Comida caseira feita com carinho",
      "Sabor de comida de casa",
      "Quentinha feita na hora",
      "Almoço caprichado",
      "Comida boa de verdade"
    ];

    const emojis = ["🍛","🥘","🍲","🍽️","🥗"];

    // versículo muda diariamente (dia do mês)
    const hoje = new Date().getDate();
    const versiculo = versiculos[hoje % versiculos.length];

    const frase = frases[Math.floor(Math.random()*frases.length)];
    const emoji = emojis[Math.floor(Math.random()*emojis.length)];

    document.title = emoji + " Marmitex da Rosa";
    document.getElementById("titulo").innerText = emoji + " Marmitex da Rosa";
    document.getElementById("frase").innerText = frase;
    document.getElementById("versiculo").innerText = versiculo;

    // contador regressivo
    let tempo = 3;
    const el = document.getElementById("contador");
    const timer = setInterval(() => {
      tempo--;
      if (tempo >= 0) {
        el.innerText = "Abrindo iFood em " + tempo + "s...";
      } else {
        clearInterval(timer);
      }
    }, 1000);

    // Fallback JS (além do meta refresh)
    setTimeout(() => { window.location.href = IFOOD_LINK; }, 3000);
  </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, ifood_link=IFOOD_LINK)

# Healthcheck para o Render
@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    # Para rodar localmente: python app.py
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
