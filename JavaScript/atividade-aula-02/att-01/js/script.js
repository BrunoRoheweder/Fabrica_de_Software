alert("Seja Bem Vindo a vendinha do seu zé")
var confirmar = confirm("deseja comprar algo?")
if (!confirmar) {
    alert("Ok! Volte sempre")
} else {
    var nome = prompt("Digite o nome do produto:")
    var qtnd = parseFloat(prompt("Digite a quantidade comprada:"))
    var valor = parseFloat(prompt("Digite o valor unitario:"))
    var percentual = parseFloat(prompt("Digite o percentual de desconto a ser aplicado:"))
    var soma = ((percentual*valor*qtnd)/100)
    var total = (qtnd * valor) - soma
    alert(`O produto comprado foi ${nome}, com o valor total de ${total}.`)
    alert("Volte sempre\nAqui na vendinha do seu zé todos são sempre bem vindos.")
}
