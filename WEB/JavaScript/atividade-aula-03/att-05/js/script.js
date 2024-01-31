var num_01 = parseInt(prompt("Digite o primeiro numero:"));
var num_02 = parseInt(prompt("Digite o segundo numero:"));

if (num_01 > num_02) { // numero 1 
    alert(`O numero maior é '${num_01}'`);
}

else if (num_02 > num_01) { // numero 2 
    alert(`O numero maior é '${num_02}'`);
}

else {
    alert(`Os numeros ${num_01} ${num_02} são todos iguais`);
}