var eleitores = parseInt(prompt("Quantidade de eleitores:"));
var candi_1 = 0;
var candi_2 = 0;
var candi_3 = 0;

for (var cont = 1; cont <= eleitores; cont++) {
    var voto = parseInt(prompt("Qual candidato você irá votar?\n1 - Zé da Manga\n2 - Bob Esponja\n3 - O cara da maçã"));

    switch (voto) {
        case 1:
            candi_1++;
            console.log(`Voto ${cont} para Zé da Manga`);
            break;
        case 2:
            candi_2++;
            console.log(`Voto ${cont} para Bob Esponja`);
            break;
        case 3:
            candi_3++;
            console.log(`Voto ${cont} para O cara da maçã`);
            break;
        default:
            console.log("Voto inválido!");
    }
}

if (candi_1 > candi_2 && candi_1 > candi_3) {
    console.log(`O Zé da Manga ganhou com ${candi_1} votos`);
} else if (candi_2 > candi_1 && candi_2 > candi_3) {
    console.log(`O Bob Esponja ganhou com ${candi_2} votos`);
} else if (candi_3 > candi_1 && candi_3 > candi_2) {
    console.log(`O Cara da maçã ganhou com ${candi_3} votos`);
} else {
    console.log("Houve empate ou nenhum voto foi registrado para nenhum candidato.");
}
