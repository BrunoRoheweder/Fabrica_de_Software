a = "Bruno"+"da"+"costa"+"roheweder"
print(len(a)) #fala quantidade de caracter tem, conta espaço tbm

print("\n")

a1 = "bruno da costa roheweder"
print(a1.capitalize()) #deixa a primeira letra em maiusculo

print("\n")

a2 = "bruno da costa roheweder"
print(a2.upper()) #deixa tudo em maiusculo

print("\n")

a3 = "BRUNO DA COSTA ROHEWEDER"
print(a3.casefold()) #tranforma tudo para minusculo

print("\n")

a4 = "BRUNO DA COSTA ROHEWEDER"
print(a4.lower()) #mesma coisa aque o casefold, tranforma tudo para minusculo

print("\n")

a6 = "bruno da costa roheweder"
print(a6.islower()) #Indentifica se e true(verdade) ou false(falso), se tiver minusculo e true, e se tiver maiusculo e false

print("\n")

a5 = "Bruno da costa roheweder"
print(a5.islower()) #Indentifica se e true(verdade) ou false(falso), se tiver minusculo e true, e se tiver maiusculo e false

print("\n")

a7 = "Bruno da costa roheweder"
print(a7.isupper()) #Indentifica se e true(verdade) ou false(falso), se tiver maiusculo e true , e se tiver minusculo e false

print("\n")

a8 = "bruno da costa roheweder"
print(a8.isupper()) #Indentifica se e true(verdade) ou false(falso), se tiver maiusculo e true , e se tiver minusculo e false

print("\n")

b = "1234"
print(b.isdigit()) #isdigit: Indentifica so numeros 
print(b)

print("\n")

c = "12345abc"
print(c.isdigit()) #isdigit: Indentifica so numeros, numeros com caracter da false
print(c)

print("\n")

d = "Bruno da Roheweder"
print(d.replace("Roheweder","Costa")) #troca o 'Roheweder' pelo 'costa'

print("\n")

d2 = "Bruno-Da-Costa-Roheweder"
print(d2.split("-")) #split: troca "-" por virgula ou qualquer coisa a sua escolha

print("\n")

d3 = "bruno da costa roheweder"
print(d3.find("b")) #conta a quantidade de caracter do5 ponto de partida da esquerda

print("\n")

d4 = "bruno da costa roheweder"
print(d4.rfind("r")) #conta a quantidade de caracter do ponto de partida de direita

print("\n")

e = "Bruno da Costa Roheweder"
print("Costa"in e)

print("\n")

e2 = "Bruno da costa roheweder"

print(e2.count("a")) #conta a quantidade de caracters informado
print("\n")


print("\n")

txt = input("Escreva um texto: ")
print(len(txt))
print(txt)

print("\n")

txt1 = input("Escreva texto 1: ")
print(len(txt1))
print(txt1)

print("\n")

txt2 = input("Escreva texto 2: ") 
print(len(txt2))
print(txt2)

print("\n")

somatxt = txt1 + txt2
print(len(somatxt))
print(somatxt)
