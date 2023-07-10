nomee = input("Digite seu nome: ")
print(nomee.capitalize())

print("\n")

nome1 = input("Digite seu nome: ")
print(nome1.upper())

print("\n")

nome2 = input("Digite seu nome completo: ")
print(nome2[0:9])

nome3 = input("Digite seu nome: ")
print(nome3.count("a"))

print("\n")

num = float(input("Escreva um numero: "))
print("Seu numero foi %.2f "%num)

print("\n")

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
soma = (num1 + num2)
print("Os numeros digitados somados foi %s"% soma)

print("\n")


nome = input("\nEscreva seu nome: ")
serie = int(input("\nEscreva sua série: "))
escola = input("\nEscreva o nome de sua escola: ")
cidade = input("\nInforme a sua cidade: ")
nota1 = float(input("\nDigite a primeira nota: "))
nota2 = float(input("\nDigite a segunda nota: "))
nota3 = float(input("\nDigite a terceira nota: "))
nota4 = float(input("\nDigite a quarta nota: "))
soma3 = (nota1 + nota2 + nota3 + nota4)/4

print("\nSeu nome é %s, e sua serie é %d, o nome de sua escola é %s, e voçê mora na cidade %s, a sua nota é %.1f."% (nome, serie, escola, cidade, soma3))

print("\n")

raio = float(input("Escreva o raio: "))
area = 3.14 * (raio**5)
print("O valor da area é %.1f "% area)

print("\n")

quad = float(input("Digite o lado: "))
soma2 = quad ** 2
dobro = soma * 2
print("O valor do quadadro é %.2f, e o valor do dobro do quadrado é %.2f "% (soma2, dobro))

print("\n")

salariohora = float(input("Digite o seu salario por hora: "))
horastraba = float(input("Digite a quantidade de horas trabalhadas no mês: "))

soma4 = salariohora * horastraba

print("Seu salario por hora é %f, Horas trabalhadas por mês %f, O total do seu salario de todo mês é %.4d"%(salariohora, horastraba,soma4))

print("\n")

inteiro = int(input("Digite um numero inteiro 1°: "))
inteiro1 = int(input("Digite um numero inteiro 2°: "))
real = float(input("Digite um numero quebrado/real: "))

print ("O 1° é %d, e o 2° é %d, o numero quabrado/real é %f"% (inteiro, inteiro1 ,real))