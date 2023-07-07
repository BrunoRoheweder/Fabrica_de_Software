import os
from class_controle_POO import *

marca = input("Digite a marca do controle: ")
tv = ControleRemoto(marca)
# while True:
#     op = int(input("1- ligar\n2- Desligar\n3- canal\n4- aumentar volume\n5- baixar volume\n>>> "))

#     if op == 1:
#         tv.ligarTV()
#     elif op == 2:
#         tv.desligarTV()
#     elif op == 3:
#         canal = input("Escolhar canal: ")
#         tv.mudar_canal(canal)
#     elif op == 4:
#         aumentar = input("Aumentar até: ")
#         tv.aumentarVolume(aumentar)
#     elif op == 5:
#         baixar = input("Baixar até: ")
#         tv.baixarVolume(baixar)
#     else:
#         print("Opção invalida")
# while True:
#     opcao = input("Você quer ligar ou desligar a tv: ")
#     opcao.upper()

#     if opcao == "ligar":

#         tv.ligarTV()
#         os.system("pause")
#         os.system("cls")

#     elif opcao == "desligar":

#         tv.desligarTV()
#         os.system("pause")
#         os.system("cls")

#     else:
#         print("Opção invalida!!!\nTente novamente")
#         os.system("cls")


tv.ligarTV()
tv.ligarTV()
tv.desligarTV()
tv.ligarTV()
tv.aumentarVolume(75)

