alert("Seja bem vindo ao cadastro do SUS/Escola");

var nome = prompt("Preencha todas os campos em branco\nNome:");
var idade = prompt("Idade:");
var sexo = prompt("Sexo:");

alert(`Olá ${nome}, agora informe as suas notas`);

var nota1 = parseFloat(prompt("Primeira nota:"));
var nota2 = parseFloat(prompt("Segunda nota:"));
var media = ((nota1+nota2)/2);

document.write(`Muito bem ${nome} sua media foi<br>Media: ${media}<br>`);

var total = media >= 7? "Aprovado" : "Reprovado";

document.write(`${total}`)