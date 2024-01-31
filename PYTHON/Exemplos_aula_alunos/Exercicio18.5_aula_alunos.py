# import matplotlib.pyplot as plt

# x = [2023,2022,2021,2020]
# y = [1302, 1212, 1200, 1045]

# plt.plot(x,y,"y")
# plt.grid()
# plt.scatter(x,y)
# plt.xlabel("x")
# plt.xlabel("y")
# plt.bar(x,y)
# plt.show()


# import secrets
# import os

# a = "a"
# sorteios = []
# while a != '0':
#     a = input("Digite algo para colocar no sorteio: ")
#     sorteios.append(a)
#     os.system("cls")

# sorteios.pop(-1)
# os.system("pause")
# os.system("cls")
# print(secrets.choice(sorteios))


# import enum

# class Animal(enum.Enum):
#     cachorro = 1
#     gato = 2
#     pantera = 2

# if Animal.cachorro is Animal.gato:
#     print("Cão e gato são os mesmos animais")
# else:
#     print("Cão e gato são animais diferentes")

# if Animal.pantera != Animal.gato:
#     print("Leão e gatos são diferentes")
# else:
#     print("Pantera e gatos são iguais")



# class Pessoa:

#     def __init__(self, nome, idade, andando = False):
#         self.nome = nome
#         self.idade = idade
#         self.andando = andando

        
#     def andar(self):
#         if self.andando:
#             print(f"{self.nome} não pode andar pq ja esta andando.")
#             return
#         print(f"{self.nome} comecou a andar...")
#         self.andando = True

#     def para(self):
#         if not self.andando:
#             print(f"{self.nome}parou de andar pq caiu")
#             return
#         print(f"{self.nome} parou de andar.")
#         self.andando = False

# a = Pessoa(input("Digite seu nome: "), input("Digite sua idade: "))
# a.andar()
# a.andar()
# a.para()
# a.para()
# a.andar()
