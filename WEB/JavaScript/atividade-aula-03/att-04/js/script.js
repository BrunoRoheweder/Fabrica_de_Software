var num_01 = parseInt(prompt("Digite o primeiro numero:"));
var num_02 = parseInt(prompt("Digite o segundo numero:"));
var num_03 = parseInt(prompt("Digite o terceiro numero:"));


if (num_01 > num_02 && num_01 > num_03) { // numero 1 
    alert(`O numero maior é '${num_01}'`);
    if (num_02 < num_03) {
        alert(`O numero menor é '${num_02}'`);
    } else {
        alert(`O numero menor é '${num_03}'`);
    }
}

else if (num_02 > num_01 && num_02 > num_03) { // numero 2 
    alert(`O numero maior é '${num_02}'`);
    if (num_01 < num_03) {
        alert(`O numero menor é '${num_01}'`);
    } else {
        alert(`O numero menor é '${num_03}'`);
    }
}

else if (num_03 > num_01 && num_03 > num_02) { // numero 3
    alert(`O numero maior é '${num_03}'`);
    if (num_01 < num_02) {
        alert(`O numero menor é '${num_01}'`);
    } else {
        alert(`O numero menor é '${num_02}'`);
    }
}

else {
    alert(`Os numeros ${num_01} ${num_02} ${num_03} são todos iguais`);
}