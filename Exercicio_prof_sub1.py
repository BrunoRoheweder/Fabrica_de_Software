lista = []
cont = 0
for a in range(10):
    lista.append(input("Escreva seu nome: "))

for nomes in lista:
    cont = cont + 1
    print(cont,nomes)