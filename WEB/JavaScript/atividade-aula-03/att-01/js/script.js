alert("Seja bem vindo(a) ao calculadora de notas parciais");

var nota_01 = parseFloat(prompt("Primeira nota:"));
var nota_02 = parseFloat(prompt("Segunda nota:"));

let media = ((nota_01 + nota_02)/2);

alert(media >= 7 || media == 10 ? "Aprovado" : "Reprovado");