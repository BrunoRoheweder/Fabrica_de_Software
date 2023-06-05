num = [[1,2],[3],[4,5,6]]
soma = num[0]+num[1]+num[2]
print(sum(soma))

print("\n")

t = [1,2,3,4]
print(t[1:3]) # ele esta printando a lista sem um numero mas n tera da lista

del t[0] #apaga o numero escolhido dentro do [0]
del t[2] #apaga o numero escolhido dentro do [2]
print(t) #ele imprime uma nova lista

print("\n")

idade = int(input("Digite sua idade: "))
if idade <20: #if: 'se' for verdadeiro printar....
    print("Voçê é jovem")
else:  #else: 'senao' printar....
    print("voçê é velho de mais(com todo respeito)")
print("vc esta gaga")

print("\n")

a = int(input("Digite sua idade2: ")) #Exemplo do slide do prof
if a == 16:
    print("Pode Votar")   
else:
    if a >= 16:
        print("Pode Dirigir")  
    else:
        if a <16: 
            print("Apenas Estude")  

print("\n")

b = int(input("Digite sua idade2: ")) #Exemplo do slide do prof
if b >= 16 and b <= 18:
    print("Pode Votar")
elif b <16:
    print("Apenas estude")
else:
    print("Pode Digirir se tiver CNH")

print("\n")

num1 = int(input("Digite um numero 1º: "))
num2 = int(input("Digite um numero 2º: "))

if num1 > num2:
    print(f"O numero {num1} e maior que {num2}")
elif num2 >num1:
    print(f"O numero {num2} e maior que {num1}")
else:
    print("Os numeros são identicos!!! tente novamente mas difentes!")

print("\n")

p = int(input("Digite um numero: "))

if p >0:
    print("O numero digitado é positivo")
elif p < 0:
    print("O numero digitado é negativo")
else:
    print("O numero digitado é neutro")

print("\n")

l = float(input("Digite a nota 1º: "))
k = float(input("Digite a nota 2º: "))

j = (l + k) /2

if j >= 7:
    print("Voçê foi Aprovado")
elif j >= 5 and j <= 6.99:
    print("Recuperação")
else:
    print("Reprovado")

print("\n")

l1 = float(input("Digite a nota 1º: "))
k1 = float(input("Digite a nota 2º: "))

y = (l1 + k1)/2

if y >= 7:
    print(f"Voçê foi Aprovado com {y}")
elif y >= 5 and y <= 6.99:
    print(f"Reprovado com {y}")
else:
    print(f"Voçê durmiu na aula é tirou {y}. Reprovado, volte para a serie anterior")

print("\n")

salario = float(input("Digite seu salario atual: "))

if salario <= 500:
    soma_sal = salario*15/100
    som = soma_sal+salario
    print(f"O seu salario com 15% de Reajustamento é {soma_sal}, Total: {som}")
elif salario >= 1000:
    soma_sal = salario*5/100
    som = soma_sal+salario
    print(f"O seu salario com 5% de Reajustamento é {soma_sal}, Total: {som}")
else:
    soma_sal = salario*10/100
    som = soma_sal+salario
    print(f"O seu salario com 10% de Reajustamento é {soma_sal}, Total: {som}")

print("\n")

print("Digite\nF- Feminino\nM- Masculino\nO- Outros")
z = input("Escolha seu sexo: ")

if z == 'M':
    print("Voçê é Masculino")

elif z == 'F':
    print("Voçê é Feminina")

elif z == 'O':
    input("Defina seu sexo: ")
else:
    print("Sexo invalido")

print("\n")

