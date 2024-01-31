nome = input("Nome do produto: ")
quant = float(input("Quantidade que ira comprar: "))
desc = float(input("Desconto: "))
valor = float(input("Valor do pruduto: "))
somaquant = (quant*valor)
soma = (somaquant * desc)/100

print ("A senhora(o) comprou",nome,", Comprou",quant,", o valor desses itens é",valor,", valor com desconto",soma,", valor dos itens pela quantidade",somaquant)