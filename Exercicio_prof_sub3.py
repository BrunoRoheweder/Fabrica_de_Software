lista = []
cont = 0 

for a in range(10):
    lista.append(input("Digite o nome do item para adicionar no 'carrinho': "))

for itens in lista:
    cont  = cont + 1
    print(cont, itens)