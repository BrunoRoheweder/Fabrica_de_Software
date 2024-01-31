alert("Seja Bem vindo a conversão de dolares");

var reais = parseFloat(prompt("Digite o valor de reais:"));
var dolar = parseFloat(prompt("Digite o valor do dolar:"));
var conversao = (reais/dolar);
alert(`valor do reais em dolares ${conversao.toFixed(2)}`);
