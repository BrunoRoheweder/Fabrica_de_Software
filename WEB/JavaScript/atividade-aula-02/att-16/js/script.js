var valor = prompt("Digite um numero:");

if (valor>=1) {
    document.write(`Maior`);
}

else if (valor == 0) {
    document.write(`Neutro`);
}

else {
    document.write(`Menor`);
}