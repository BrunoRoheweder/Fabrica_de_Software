num = float(input("Digite o 1º numero: "))
num1 = float(input("Digite o 2º numeoro: "))
soma = (num+num1)
print(f"A soma é {soma}")

print()
lcp = []
lco = []
lca = []

while True:

    opcao = int(input("Digite 1 para consulta tal1\n2 para consulta tal2\n3 para a consulta tal3\n4 para relatorio\n5 sair\nEscolha: "))
    if opcao == 1:
        cp = input("Digite aqui: ") 
        lcp.append(cp)
    elif opcao == 2:
        co = input("Digite aqui: ") 
        lco.append(co)
    elif opcao == 3:
        ca = input("Digite aqui: ")
        lca.append(ca)
    elif opcao == 4:
        print(lco,lcp,lca)
    elif opcao == 5:
        break
    
print()

try: 
    num2 = int(input("Digite o 1º numero: "))
    num3 = int(input("Digite o 2º numero: "))

    soma1 = (num2/num3)
    print(f"A divisão é {soma1}")
except:
    print("Use somente numeros.")

print()

for par in range(0,102,2):
    print(par)

print()

for impar in range(1,100,2):
    print(impar)

print()



