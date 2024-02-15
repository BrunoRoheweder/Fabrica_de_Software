var inicio = parseInt(prompt("Inicio: "))
var fim = parseInt(prompt("Fim: "))

contando_apartir(inicio, fim)
var soma = 0
function contando_apartir(inicio, fim){
    for (inicio; inicio <= fim; inicio++){
        soma += 1 
        console.log(soma)
    };
    console.log(soma)
};


