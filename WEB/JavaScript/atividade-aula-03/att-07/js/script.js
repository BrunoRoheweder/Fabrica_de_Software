var num = parseInt(prompt("Digite um numero: "));

if (num < 0) {
    alert(`O numero ${num} é negativo`)
}
else if (num > 0) {
    alert(`O numero ${num} é positivo`)
}

else if (num == 0) {
    alert(`O numero ${num} é neutro`)
}

else {
    alert(`O '${num}' não é um numero`)
}