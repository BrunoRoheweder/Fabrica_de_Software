from class_Quadrado import*
import os

print(8*"=-","Tamanho do Quadrado","=-"*8)
tamanho = int(input("Digite o valor do quadrado: "))
q1 = Quadrado(tamanho)

while True:
    op = input("1- mostrar tamanho\n2- mudar o valor do tamnho(novo tamanho)\n0- Sair\n>>> ")
    if op == "1":
        os.system("cls")
        q1.mostrar_area()
        os.system("pause")
        os.system("cls")
    elif op == "2":
        os.system("cls")
        mudar = int(input("Digite o valor para mudar: "))
        os.system("cls")
        q1.mudar_valor_lado(mudar)
        os.system("pause")
        os.system("cls")
    elif op == "0":
        break
    else:
        print("Opção invalida!!!")