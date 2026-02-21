<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Marmitex da Rosa</title>

<meta name="description" content="Marmitex da Rosa - comida caseira em Mogi das Cruzes. Peça agora no iFood.">
<meta name="robots" content="index,follow">

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
  padding:20px;
}

h1{
  font-size:2.5rem;
  margin-bottom:5px;
}

.frase{
  font-size:1.2rem;
  margin-bottom:10px;
}

.versiculo{
  font-size:0.9rem;
  opacity:0.8;
  margin-top:10px;
}

.contador{
  margin-top:15px;
  font-size:0.9rem;
  opacity:0.7;
}
</style>
</head>

<body>

<h1 id="titulo"></h1>
<div class="frase" id="frase"></div>
<div class="versiculo" id="versiculo"></div>
<div class="contador" id="contador">Abrindo iFood em 3s...</div>

<script>
const linkIfood = "https://www.ifood.com.br/delivery/mogi-das-cruzes-sp/marmitex-da-rosa---sabor-jardim-marica/0c36497f-001e-4a37-ae6d-e57d04370966";

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

const hoje = new Date().getDate();
const versiculo = versiculos[hoje % versiculos.length];
const frase = frases[Math.floor(Math.random()*frases.length)];
const emoji = emojis[Math.floor(Math.random()*emojis.length)];

document.getElementById("titulo").innerText = emoji + " Marmitex da Rosa";
document.getElementById("frase").innerText = frase;
document.getElementById("versiculo").innerText = versiculo;

let tempo = 3;

const intervalo = setInterval(()=>{
  tempo--;

  if(tempo >= 0){
    document.getElementById("contador").innerText =
    "Abrindo iFood em " + tempo + "s...";
  }

  if(tempo < 0){
    clearInterval(intervalo);
    window.location.href = linkIfood;
  }

},1000);
</script>

</body>
</html>



