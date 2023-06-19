# def hello(a, b):
#     s = a + b
#     print(s)
    
# hello(int(input("Digite o primeiro numero: ")),int(input("Digite o segundo numero: ")))

# def cli(nome, idade):
#     print(f"{nome} tem {idade} de idade.")

# cli(input("digite seu nome: "),int(input("Digite sua idade: ")))


# def calcular_pag(quant_horas, valor_horas):
#     horas = float(quant_horas)
#     taxa = float(valor_horas)

#     if horas<= 40:
#         salario = horas*taxa
#     else:
#         h_excd = horas - 40

#         salario = 40*taxa+(h_excd*(1.5*taxa))
#     print(salario)

# qh = input("Quantidades de horas: ")
# vh = input("Digite o valor da hora: ")
# calcular_pag(qh , vh)


# def soma(x,y):
#     result = x + y
#     return result
# a = float(input("1º : "))
# b = float(input("2º : "))

# c = soma(a, b)
# print(f"soma: {c}")

# def inverte(nome,sobrenome):
#     nomeinvarso = sobrenome+","+nome
#     return nomeinvarso
# nome = input("Nome: ")
# sobrenome = input("Sobrenome: ")
# invertido = inverte(nome,sobrenome)
# print("Olá", invertido)


# def par(x):
#     if (x%2)==0:
#         return True
#     else:
#         return False
    
# while True:
#     num = int(input("Digite um numero: "))
#     if par(num):
#         print("É par")
#     else:
# #         print("É impar")

# def cadastro():
#     name = input("Digite seu nome: ")
#     age = int(input("Digite sua idade: "))
#     return name, age

# print("iniciando cadastro...")
# nome, idade = cadastro()
# print("Cadastro Realizado com sucesso...")

# print(f"Seu nomer é {nome} e você tem {idade} anos de idade.")

# def soma(a=0,b=0,c=0):
#     s = a + b + c
#     print(s)
# soma(int(input("1º : ")),int(input("2º : ")),int(input("3º : ")))
# # num1 = int(input("1º : "))
# # num2 = int(input("2º : "))
# # num3 = int(input("3º : "))

def p_n(n):
    
    if n > 0:
        print("Positivo")
    elif n < 0:
        print("Negativo")
    elif n == 0:
        print("Zero")
    return n

p_n(n = int(input("Digite um numero: ")))