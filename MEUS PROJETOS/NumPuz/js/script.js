

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

// Criando numeros aleatorios

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

// Fim da criação de numeros


// Adicionando o numero no array necessario para o jogo inicial em posições aleatorias

// console.log(numerosSorteados)

var array = [[num1],[num2],[num3],
             [num4],[num5],[num6],
             [num7],[num8],[num0]];


numerosSorteados.forEach(function(valor, index) {
    array[index][0] = valor;
    array[8][0] = 0;
    // array[6][0] = 0;
    // console.log(array[0][0]);
});

// Fim da adicão dos numeros




// Verificando se pode se mover e mover

// var array = [[num1],[num2],[num3],[num4],[num5],[num6],[num7],[num8],[num0]];
//      index =   0   ,  1   ,  2   ,  3   ,  4   ,  5   ,  6   ,  7   ,  8   .

// var array = [[num1],[num2],[num3],
//              [num4],[num5],[num6],
//              [num7],[num8],[num0]];
//      index =   0   ,  1   ,  2   ,
//                3   ,  4   ,  5   ,
//                6   ,  7   ,  8   .
//      Verificar um index anterior e um posterior e o terceiro index apos o seu proprio index

function mover_1() {
    array.forEach(function(valor, index) {
        if (index == 0) { // index 0 numero 1
            if (array[1][0] == 0) {
                // Condição de movimento
            }

            else if (array[3][0] == 0) {
                // Condição de movimento
            }
        }
    })
}

function mover_2() {
    array.forEach(function(valor, index) {
        
        if (index == 1) { // index 1 numero 2
            if (array[0][0] == 0) {
                // Condição de movimento
            }
            else if (array[2][0] == 0) {
                // Condição de movimento
            }
            else if (array[4][0] == 0) {
                // Condição de movimento
            }
        }
    })
}

function mover_3() {
    array.forEach(function(valor, index) {
        
        if (index == 2) { // index 2 numero 3
            if (array[1][0] == 0) {
                // Condição de movimento
            }
            else if (array[5][0] == 0) {
                // Condição de movimento
            }
        }
    })
}

function mover_4() {
    array.forEach(function(valor, index) {
        
        if (index == 3) { // index 3 numero 4
            if (array[0][0] == 0) {
                // Condição de movimento
            }
            else if (array[4][0] == 0) {
                // Condição de movimento
            }
            else if (array[6][0] == 0) {
                // Condição de movimento
            }
        }
    })
}

function mover_5() {
    array.forEach(function(valor, index) {
        
        if (index == 4) { // index 4 numero 5
            if (array[1][0] == 0) {
            // Condição de movimento
            }
            else if (array[3][0] == 0) {
            // Condição de movimento
            }
            else if (array[5][0] == 0) {
            // Condição de movimento
            }
            else if (array[7][0] == 0) {
            // Condição de movimento
            }
        }
    })
}

function mover_6() {
    array.forEach(function(valor, index) {
        
        if (index == 5) { // index 5 numero 6
            if (array[2][0] == 0) {
                // Condição de movimento
            }
            else if (array[4][0] == 0) {
                // Condição de movimento
            }
            else if (array[8][0] == 0) {
                // Condição de movimento
                var numero8 = document.getElementById("num6");
                numero8.innerHTML = " "

                var numero9 = document.getElementById("num9");
                numero9.innerHTML = "6"
            }
        }
    })
}

function mover_7() {
    array.forEach(function(valor, index) { 

        if (index == 6) { // index 6 numero 7
            if (array[3][0] == 0) {
                // Condição de movimento
            }
            else if (array[7][0] == 0) {
                // Condição de movimento
                array[7][0] = array[6][0]
                array[6][0] = 0

                var numero8 = document.getElementById("num8");
                numero8.innerHTML = "8"

                var numero7 = document.getElementById("num7");
                numero7.innerHTML = " "
            }
        }
    })
}

function mover_8() {
    array.forEach(function(valor, index) {
        
        if (index == 7) { // index 7 numero 8
            if (array[4][0] == 0) {
                // Condição de movimento
            }
            else if (array[6][0] == 0) {
                // Condição de movimento
                array[6][0] = array[7][0]
                array[7][0] = 0

                var numero7 = document.getElementById("num7");
                numero7.innerHTML = "8"

                var numero8 = document.getElementById("num8");
                numero8.innerHTML = " "
            }
            else if (array[8][0] == 0) {
                // Condição de movimento

                array[8][0] = array[7][0]
                array[7][0] = 0

                var numero8 = document.getElementById("num8");
                numero8.innerHTML = " "

                var numero9 = document.getElementById("num9");
                numero9.innerHTML = "8"
            }
        }
    })
}

function mover_9() {
    array.forEach(function(valor, index) {

        if (index == 8) { // index 6 numero 7
            if (array[7][0] == 0) {
                // Condição de movimento
                array[7][0] = array[8][0]
                array[8][0] = 0

                var numero9 = document.getElementById("num9");
                numero9.innerHTML = " "

                var numero8 = document.getElementById("num8");
                numero8.innerHTML = "8"
            }
            else if (array[5][0] == 0) {
                // Condição de movimento
            }
        }
    })
}

// Fim da vereficação de mover e mover


//  CONFIRMANDO QUE TODOS ESTÃO IGUAIS OU SEJA TODOS ESTÃO NOS DEVIDOS LUGARES
//  VERIFICAÇÃO 

var array_confirm = [[1],[2],[3],
                     [4],[5],[6],
                     [7],[8],[0]];

var todosConfirmados = true;  

array_confirm.forEach(function(valor, index) {
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
