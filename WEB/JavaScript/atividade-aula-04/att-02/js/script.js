var inicio = parseInt(prompt("Inicio: "))
var fim = parseInt(prompt("Fim: "))

contando_apartir(inicio, fim)

function contando_apartir(inicio, fim){
    for (inicio; inicio <= fim; inicio++){
        console.log(inicio);
    };
};


