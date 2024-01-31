while (true) {
    var letra = prompt("Escolha F, M ou O: ")

    if ("F" == letra || "f" == letra) {
        alert(`A letra digita foi '${letra}'\nFeminino`)
        break
    }

    else if ("M" == letra || "m" == letra) {
        alert(`A letra digita foi '${letra}'\nMasculino`)
        break
    }

    else if ("O" == letra || "o" == letra) {
        alert(`A letra digita foi '${letra}'\nOutros`)
        break
    }

    else {
        alert(`A letra '${letra}' não é uma opção.`)
        break
    }
};