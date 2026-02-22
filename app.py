from flask import Flask, render_template_string
import os

app = Flask(__name__)

# LINK DO RESTAURANTE NO IFOOD
IFOOD_LINK = "https://www.ifood.com.br/delivery/mogi-das-cruzes-sp/marmitex-da-rosa---sabor-jardim-marica/0c36497f-001e-4a37-ae6d-e57d04370966"

HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- Redirecionamento automático -->
<meta http-equiv="refresh" content="5;url={{ ifood_link }}">

<title>Marmitex da Rosa</title>
<meta name="description" content="Marmitex da Rosa - comida caseira em Mogi das Cruzes. Peça agora no iFood.">

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

h1{
font-size:2.4rem;
margin-bottom:8px;
}

.versiculo{
font-size:1.2rem;
margin-top:10px;
max-width:500px;
}

.botao{
margin-top:20px;
padding:14px 28px;
background:#ff5722;
color:white;
border-radius:10px;
text-decoration:none;
font-size:1.1rem;
font-weight:bold;
}

.botao:hover{
background:#e64a19;
}

.contador{
margin-top:15px;
font-size:0.95rem;
opacity:0.8;
}
</style>
</head>

<body>

<h1 id="titulo">🍛 Marmitex da Rosa</h1>

<div class="versiculo" id="versiculo"></div>

<a class="botao" href="{{ ifood_link }}">
Pedir agora no iFood
</a>

<div class="contador" id="contador">
Abrindo iFood automaticamente...
</div>

<script>

// PALAVRAS BÍBLICAS (UMA POR DIA)
const versiculos = [
"Salmo 23:1 — O Senhor é meu pastor; nada me faltará.",
"Filipenses 4:13 — Tudo posso naquele que me fortalece.",
"João 3:16 — Porque Deus amou o mundo de tal maneira...",
"Provérbios 3:5 — Confia no Senhor de todo o teu coração.",
"Salmo 37:5 — Entrega o teu caminho ao Senhor.",
"Romanos 8:28 — Todas as coisas cooperam para o bem.",
"Josué 1:9 — Seja forte e corajoso.",
"Salmo 121:1 — Elevo os meus olhos para os montes.",
"Mateus 11:28 — Vinde a mim todos que estão cansados.",
"Salmo 46:1 — Deus é nosso refúgio e fortaleza."
];

// Escolhe automaticamente baseado no dia
const hoje = new Date().getDate();
const versiculoHoje = versiculos[hoje % versiculos.length];

document.getElementById("versiculo").innerText = versiculoHoje;

// CONTADOR
let tempo = 5;
const contador = document.getElementById("contador");

const timer = setInterval(() => {
tempo--;
contador.innerText = "Abrindo iFood em " + tempo + " segundos...";
if (tempo <= 0) clearInterval(timer);
}, 1000);

// Fallback caso meta refresh falhe
setTimeout(() => {
window.location.href = "{{ ifood_link }}";
}, 5000);

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, ifood_link=IFOOD_LINK)

# Health check (Render usa isso)
@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
