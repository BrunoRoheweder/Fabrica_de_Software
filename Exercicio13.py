'''lista = ["Olá", "Mundo", "Python", "é", "incrível",1,2,3]

# Extraindo múltiplos elementos da lista
texto1 = lista[0]
texto2 = lista[1]
texto3 = lista[2]                       # forma de tirar o texto da lista 
texto4 = lista[3]
texto5 = lista[4]
texto6 = lista[5]
texto7 = lista[6]
texto8 = lista[7]

# Imprimindo os textos extraídos
print(texto1,texto2,texto3,texto4,texto5,texto6,texto7,texto8)
print(texto2)
print(texto3)

nomes = ['Pedro','Joâo','Leticia',[1]]
sub = nomes[-1]
for n in sub:   # tirando da sub lista para printar com for
    print(n)

print()

nomes = ['Pedro','Joâo','Leticia']
for n in nomes:     #printa os nomes com for
    print(n)

print()

sem_lista = ("Ola Mundo!")  
for sl in sem_lista:
    print(sl)           #printa uma string

print()

nome = ["Pedro","Joao","Leticia"]
for na in nome:
    print(na)           # quando o for achar a string Joao ele entrara no if e ira para o for com break
    if na == "Joao": 
        break

print()

n1 = ["Pedro","Joao","Leticia"]
for a in n1:
    if a == "Joao":             # quando o for achar a string Joao ele entrara no if e ira continuar o programa e n printara o Joao
        continue
    print(a)

print()

for x in range(6):          #conta a quantidade de vezes q vc quiser
    print(x)

print()

for x1 in range(2,6):       # conta de um ponto de inicio ate o ponto do fim que estão determinado
    print(x1)

print()

for x2 in range(-1,100,2):  # contador de impar com for
    print(x2)

print()

for x2 in range(0,102,2):   # contador de par com o for
    print(x2)

print()

for i in range(1,10):  # for q entra dentro do  outro for contagem vai ser 00 01....
    for j in range(10):
        print(i,j)

print()

for num in range(1,10):
    for num1 in range(1,11):    #Calculadora simples e simplificada facil e td mais
        print(f"{num} * {num1} = {num*num1}")

print()

for z2 in range(0,102,2):   # contador de par com o for
    print(z2)

print()

nu1 = int(input("Digite o primeiro numero: "))          # O usuario digita os dois numeros e conta do ponto de partida onde o usuario
nu2 = int(input("Digite o segundo numero: "))           # escreveu primeiramente e vai ate no segundo ponto onde o usuario determinou onde chegar

for b in range(nu1,nu2+1):
    for b1 in range(nu1,nu2+1):
         print(b,"+",b1,"=",b1+b)  #somando o b e b1 
print()

a = 1
nu11 = int(input("Digite o primeiro numero: "))          # O usuario digita os dois numeros e conta do ponto de partida onde o usuario
nu21 = int(input("Digite o segundo numero: "))           # escreveu primeiramente e vai ate no segundo ponto onde o usuario determinou onde chegar

for b in range(nu11,nu21+1):
    for b1 in range(a):
         print(b,"+",b,"=",b+b)   # somando o b

print()

cont = 0
l = int(input("Digite um numero: "))
l1 = int(input("Digite um numero: "))

for k in range(l,l1):
    cont = cont + 1
print(cont)  

print()

numer = int(input("Digite o primeiro numero: "))
numer1 = int(input("Digite o segundo numero: "))

for p in range(numer,numer1+1):
     print(p)

print()

numer2 = int(input("Digite o primeiro numero: "))
numer3 = int(input("Digite o segundo numero: "))

for p1 in range(numer2,numer3 + 1):
    print(p1,end=" ")

print()


numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))
numero4 = int(input("Digite o quarto numero: "))
numero5 = int(input("Digite o quinto numero: "))
li = [numero1,numero2,numero3,numero4,numero5]
for f in range(1):
    print(sum(li)/5)

print()

menor = 0
maior = 0
cont = int(input("Digite um numero para escolhar\n1 para maior menor soma\n2 para continuar\nEscolha:  "))


if cont == 1:
    
    for aon in range(cont):

        while True:
            di = str(input("Digite um numero: "))
            
            if di == 'x':
                soma = maior+menor
                print("soma:",soma)
                break

            di = int(di)

            if di < maior:
                menor = di  
                print("menor:",menor) 

            elif di > menor:
                maior = di
                print("maior: ",maior)

if cont == 2: 
    print("Ok... Vamos continuar\nEscolha seu destino.")


print()

menor1 = 0
maior1 = 0
while True:
    

    di1 = str(input("Digite um numero: "))


    if di1 == 'x':
        soma = maior+menor
        print("soma:",soma)
        break

    di1 = int(di1)

    if di1 < maior1:
        menor1 = di1  
        print("menor:",menor1) 

    elif di1 > menor1:
        maior1 = di1
        print("maior: ",maior1)


print()

lidade = []
cont = -1
while True:
    idade = int(input("Digite 0 para parar\nEscreva sua idade: "))
    lidade.append(idade)
    soma = sum(lidade)
    cont = (cont + 1)
    print(f"Na sua turma tem {cont+1} pessoa.\n")
    
    if idade == 0:
        som = (soma/cont)
        print(som)
        if som > 0 and som <=25: 
            print("A sua turma é jovem!")
            break
        elif som >= 26 and som < 60:
            print("A sua turma é adulta!")
            break
        else:
            print("A sua turma é idosa!")
            break
'''
print()


quant = int(input("Digite quantas pessoas tem na turma: "))
lidade = []
cont = -1
quant1 = quant-quant-quant

for aond in range(quant):
    
    idade = int(input("Digite 0 para parar\nEscreva sua idade: "))
    lidade.append(idade)
    soma = sum(lidade)
    cont = (cont + 1)

    print(f"Na sua turma tem {cont+1} pessoa.\n")

    quant1 = (quant1 + 1) +1

    if quant1 == quant:
        som = (soma/quant)
        print(som)
        if som > 0 and som <=25: 
            print("A sua turma é jovem!")
            break
        elif som >= 26 and som < 60:
            print("A sua turma é adulta!")
            break
        else:
            print("A sua turma é idosa!")
            break

print()
