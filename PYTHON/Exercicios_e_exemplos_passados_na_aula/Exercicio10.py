print("-- Resevartório de Água --") # falta de parenteses

altura=float(input(" Digite a altura (cm):"))
largura=float(input(" Digite a largura (cm): ")) # falta de parenteses
comprimento=float(input(" Digite o comprimento (cm): "))
c_diario = float(input("Digite o valor do consumo médio diário(litros/dia)= ")) #falta de '='

cap_total=((altura*largura*comprimento)/1000); #o resultado seria em cm3 por isso, dividimos por mil para passar de cm3 para litros  # faltou multiplicar largura * comprimento
auton_reser=cap_total/c_diario #falta de acento

print("Capacidade do Reservatório= ",cap_total, "litros ")
print("Autonomia do reservatório= ",auton_reser," dias") #Agora, vamos classificar o consumo
if(auton_reser<2):
    print("Consumo Elevado") # falta de identação
elif(auton_reser>=2 and auton_reser<=7): #auton_reser tem que estar menor q 7
    print("Consumo Moderado")
elif(auton_reser>7):
    print("\n Consumo Baixo")

print("\n")

letras = input("Digite uma letras: ")   # não simplicafado

if letras == 'a'or letras == 'A' or letras == 'e' or letras == 'E' or letras == 'i' or letras == 'I' or letras == 'o' or letras == 'O' or letras == 'u' or letras == 'U':
    print("A letra digita e vogal")
else:
    print("A letra digita e consoante")

print("\n")

letras1 = input("Digite uma letras: ")    # simplificado
letras1 = letras1.capitalize()

if letras1 == 'A'or letras1 == 'E'or letras1 == 'I'or letras1 == 'O'or letras1 == 'U':
    print("A letra digita e vogal")

else:
    print("A letra digita e consoante")

print("\n")

nota1 = float(input("Digite a 1º nota: "))
nota2 = float(input("Digite a 2º nota: "))

media = (nota1+nota2)/2

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
if media == 10:
    print("Distinção")

print("\n")

num_maior1 = int(input("Digite o 1º numero: "))
num_maior2 = int(input("Digite o 2º numero: "))
num_maior3 = int(input("Digite o 3º numero: "))

lista = [num_maior1,num_maior2,num_maior3]

print(max(lista))


nume1 = int(input("Digite: "))
nume2 = int(input("Digite: "))
nume3 = int(input("Digite: "))

if nume1>nume2 and nume1>nume3:
    print(nume1)
elif nume2>nume1 and nume2>nume3:
    print(nume2)
else:
    print(nume3)

print("\n")

nu1 = int(input("Digite o 1º numero: "))
nu2 = int(input("Digite o 2º numero: "))
nu3 = int(input("Digite o 3º numero: "))

print (min(nu1,nu2,nu3))
print (max(nu1,nu2,nu3))

print("\n")

n1 = float(input("Digite o 1º valor do produto: "))
n2 = float(input("Digite o 2º valor do produto: "))
n3 = float(input("Digite o 3º valor do produto: "))

deve_c = (min(n1,n2,n3))

print(f"Comparando....\nO preço de melhor custo beneficio é {deve_c}")

p4 = input("\nEscrave o nome do 1º produto: ")
n4 = float(input("Digite o 1º valor do produto: "))

p5 = input("\nEscrave o nome do 2º produto: ")
n5 = float(input("Digite o 2º valor do produto: "))

p6 = input("\nEscrave o nome do 3º produto: ")
n6 = float(input("Digite o 3º valor do produto: "))

if n4 < n5 and n4 < n6 :
    print(f"\nO produto mais barato é {p4}, valor: {n4}")
elif n5 < n4 and n5 < n6:
    print(f"\nO produto mais barato é {p5}, valor: {n5}")
else:
    print(f"\nO produto mais barato é {p6}, valor: {n6}")

print("\n")

numero1 = int(input("Digite o 1º numero: "))
numero2 = int(input("Digite o 2º numero: "))
numero3 = int(input("Digite o 3º numero: "))

decre = [numero1,numero2,numero3]

decre.sort(reverse=True)
print(decre)

print("\n")

turno = input("Digite so a 1º letra do turno que voçê estuda: ")
turno = turno.capitalize()
if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Invalido\n Tente Novamente.")