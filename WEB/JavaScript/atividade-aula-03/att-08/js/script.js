var salario = parseInt(window.prompt("Digite o seu salario atual: ")) 

if (salario < 500) {
    var multi_15 = (salario*1.5);
    alert(`O salario é de ${multi_15}`);
}
else if(salario > 500 && salario<=1000) {
    var multi_10 = (salario*1.0);
    alert(`O salario é de ${multi_10}`);
}
else if(salario>1000) {
    var multi_1000 = (salario*0.5);
    alert(`O salario é de ${multi_1000}`);
}
else{
    alert(`O '${salario}' não é um numero`);
}