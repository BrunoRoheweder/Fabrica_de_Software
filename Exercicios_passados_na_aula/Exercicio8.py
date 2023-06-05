num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))

met = num2/2
dobro = (num1*2)*met

triplo = (num1*3)+num3

elevado = num3**3

print(f"O dobro do primeiro é {dobro}, O triplo do primeiro {triplo}, Terceiro elevado ao cubo {elevado}.")

print("\n")

altura = float(input("Insira sua altura aqui para saber seu peso ideal: "))
soma = (72.7*altura)-58
print("Seu peso ideal é %.2f "% soma)

print("\n")

a = [10,20,30,40,50]
print(a)
print(type(a))

print("\n")

b= ["python",3.5,True,1]
print(b)
print(type(b))

print("\n")

lista = ["Ederson", 20 , 20.2, 2,20]
print(lista)
print(type(lista))

print("\n")

sublist = [10,1,True,[1,2,3]]
print(sublist)

print("\n")

sublist1 = [10,1,True,"a",[1,2,3]]
print (len(sublist1))

print("\n")

lista1 = [print("Ola"),[input("Digite um numero: ")]]
print(lista1)

print("\n")

lista2 = [3,67,"gato",[56,57,"cachorro"],[],3.14,False]
print(lista2[3][1])

print("\n")

animais = ["gato","cachorro"]
print ("gato" in animais)

print("\n")

animais1 = ["gato","cachorro"]
print ("gato" not in animais1)

print("\n")

d = [1,2,3,4,5,6,7,8,9]
print(d)
print(max(d))
print(min(d))
print(sum(d)) # soma tudo q esta dentro

print("\n")

e = [1,3,5]
f = [2,4,6]
print(e + f)

print("\n")

t = [1,2,3,4,5,6,7,8,9]
print(sum(t)/len(t))

print("\n")

uma_lista = ['a','b','c','d','e','f']
print(uma_lista[1:3])
print(uma_lista[:4])
print(uma_lista[3:])
print(uma_lista[:])
print(uma_lista[0:6])

print("\n") 

frutas = ["bananas","maça","careja"]

frutas[0] = "pera"
frutas[-1] = "laranja"
print(frutas)

print("\n")

listaa = ["flor","azul",[1,"casa"]]
listaa[2][1] = "Escola"
print(listaa)

print("\n")

listinha = ["a","b","c","d","e","f"]
print(listinha)
listinha[1:3] = ["x","y"]
print (listinha)

print("\n")

m = ["a","b","c","d","e","f"]
print(m)
print(len(m))

m[1:3] = []
print(m)
print(len(m))

print("\n")

k = ["a","d","f"] #add em local expecifico
print(k)
k[1:1] = ["b","c"]
print(k)
k[4:4] = ["e"]
print(k)

print("\n")

i = ["um","dois","três"]
del i[1]
print(i)

o = ["a","b","c","d","e","f"]
del o[1:5] #apaga o que vc quiser expecificamente expecifico
print(o)

print("\n")

j = ["81","82","83"]
j.append(5) #add no final do texto sempre
print(j)

print("\n")

h = [2,4,6,8,3,1,54,5,7,99,56,34,23,42,]
h.sort() #sort coloca em ordem crescente e decrescente
print(h)

g = [2,4,6,8,3,1,54,5,7,99,56,34,23,42,]
g.sort(reverse=True) #sort coloca em ordem crescente e decrescente
print(g)

print("\n")

q = [1,2,3,4,5,6,7,8,9]
print(q.index(4)) #index mostra a posição

print("\n")

y = [88,81,82,83]
y.insert(1,100)   # insirir no texto facilmente, por cordenadas 1 para colocar 100
print(y)

u = [1,2,3,4,5,6,7]
print(u)
print(u.count(4)) #mostra quantas vezes '(4)' esta dentro dos [] da lista

e = [1,2,3,4]
e.pop()
print(e) #remove dentro do [] espesifico que escolher

e.pop(0) #remove dentro do [] espesifico que escolher
print(e)