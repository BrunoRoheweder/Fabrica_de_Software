var num_01 = parseInt(prompt("Digite o primeiro numero:"));
var num_02 = parseInt(prompt("Digite o segundo numero:"));
var num_03 = parseInt(prompt("Digite o terceiro numero:"));

if (num_01 > num_02 && num_01 > num_03) { // número 1
    if (num_02 < num_03) {
        alert(`Crescente: ${num_02}, ${num_03}, ${num_01}\nDecrescente: ${num_01}, ${num_03}, ${num_02}`);
    } else {
        alert(`Crescente: ${num_03}, ${num_02}, ${num_01}\nDecrescente: ${num_01}, ${num_02}, ${num_03}`);
    }
}

else if (num_02 > num_01 && num_02 > num_03) { // número 2
    if (num_01 < num_03) {
        alert(`Crescente: ${num_01}, ${num_03}, ${num_02}\nDecrescente: ${num_02}, ${num_03}, ${num_01}`);
    } else {
        alert(`Crescente: ${num_03}, ${num_01}, ${num_02}\nDecrescente: ${num_02}, ${num_01}, ${num_03}`);
    }
}

else if (num_03 > num_01 && num_03 > num_02) { // número 3
    if (num_01 < num_02) {
        alert(`Crescente: ${num_01}, ${num_02}, ${num_03}\nDecrescente: ${num_03}, ${num_02}, ${num_01}`);
    } else {
        alert(`Crescente: ${num_02}, ${num_01}, ${num_03}\nDecrescente: ${num_03}, ${num_01}, ${num_02}`);
    }
}

else {
    alert(`Os numeros ${num_01}, ${num_02} e ${num_03} são todos iguais`);
}