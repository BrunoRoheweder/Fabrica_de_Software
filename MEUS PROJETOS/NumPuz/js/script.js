

// var num1 = 1
// var num2 = 2
// var num3 = 3
// var num4 = 4
// var num5 = 5
// var num6 = 6
// var num7 = 7
// var num8 = 8
// var num0 = 0
var num1;
var num2;
var num3;
var num4;
var num5;
var num6;
var num7;
var num8;
var num0;

function sortearNumeros(qtdNumeros, minimo, maximo) {
    // Cria um array com todos os números disponíveis
    var numerosDisponiveis = [];
    for (var i = minimo; i <= maximo; i++) {
        numerosDisponiveis.push(i);
    }

    // Verifica se há números suficientes disponíveis para sortear
    if (qtdNumeros > numerosDisponiveis.length) {
        console.log("Não há números suficientes disponíveis para sortear.");
        return;
    }

    // Array para armazenar os números sorteados
    var numerosSorteados = [];

    // Sorteia os números
    for (var j = 0; j < qtdNumeros; j++) {
        // Escolhe um índice aleatório dentro do array de números disponíveis
        var indiceSorteado = Math.floor(Math.random() * numerosDisponiveis.length);

        // Remove o número sorteado do array de disponíveis e adiciona ao array de sorteados
        numerosSorteados.push(numerosDisponiveis.splice(indiceSorteado, 1)[0]);
    }

    return numerosSorteados;
}

var numerosSorteados = sortearNumeros(8, 1, 8);
console.log(numerosSorteados)

var array = [[num1],[num2],[num3],
             [num4],[num5],[num6],
             [num7],[num8],[num0]];


numerosSorteados.forEach(function(valorAtual, index) {
    array[index][0] = valorAtual;
    array[8][0] = 0;
    console.log(array[0][0]);
});


(function(){
    array.forEach(function() {
        var random = (num) => Math.floor(Math.random() * num);
        // console.log(random(9));
    });
})();

//  CONFIRMANDO QUE TODOS ESTÃO IGUAIS OU SEJA TODOS ESTÃO NOS DEVIDOS LUGARES
//  VERIFICAÇÃO 

var array_confirm = [[1],[2],[3],
                     [4],[5],[6],
                     [7],[8],[0]];

var todosConfirmados = true;  

array_confirm.forEach(function(valorAtual, index) {
    if (array_confirm[index][0] !== array[index][0]) {
        todosConfirmados = false;
    }
});

if (todosConfirmados) {
    console.log("Você Ganhou");
} else {
    console.log("Pelo menos um número não está confirmado");
}
//  FIM DA VERIFICAÇÃO  
