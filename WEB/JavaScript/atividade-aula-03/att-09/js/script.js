var salario = parseInt(prompt("Digite seu salario: "))

if (salario < 280) {
    var aumento_280 = (salario*0.20)
    alert(`O salario antes do ajuste: ${salario}\nO percentual de aumento aplicado: 20%\nValor do aumento: ${aumento_280}\nNovo salario: ${salario+aumento_280}`)
}
else if (salario > 280 && salario < 700) {
    var aumento_280_700 = (salario*0.15)
    alert(`O salario antes do ajuste: ${salario}\nO percentual de aumento aplicado: 20%\nValor do aumento: ${aumento_280_700}\nNovo salario: ${salario+aumento_280_700}`)
}
else if (salario > 700 && salario < 1500) {
    var aumento_700_1500 = (salario*0.10)
    alert(`O salario antes do ajuste: ${salario}\nO percentual de aumento aplicado: 20%\nValor do aumento: ${aumento_700_1500}\nNovo salario: ${salario+aumento_700_1500}`)
}
else if (salario >= 1500) {
    var aumento_1500 = (salario*0.5)
    alert(`O salario antes do ajuste: ${salario}\nO percentual de aumento aplicado: 20%\nValor do aumento: ${aumento_1500}\nNovo salario: ${salario+aumento_1500}`)
}

else {
    alert("Digite apenas numeros.")
}
