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
print(texto3)'''

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

for b in range(nu1,nu2 + 1):
    print(b)

print()

