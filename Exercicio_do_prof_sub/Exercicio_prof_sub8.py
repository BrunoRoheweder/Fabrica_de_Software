num1 = []
num2 = []
soma = 0
cont = 0

for a in range(5):
    cont = cont + 1
    num1.append(int(input(f"Digite o {cont}º numero: ")))
    num2 = num1

for i in num2:

    soma = (i * i)
    num2 = [soma]
    print("Lista 2 é: ",soma)