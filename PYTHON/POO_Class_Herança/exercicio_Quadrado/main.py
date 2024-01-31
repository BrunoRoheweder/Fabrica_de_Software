from quadrado import*
from time import sleep 
import os

print(8*"=-","Tamanho do Quadrado","=-"*8)
try:
    tamanho = int(input("Digite o valor do quadrado: "))
except ValueError:
    print("Use apenas numeros!!!")
else:
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
        try:
            mudar = int(input("Digite o valor para mudar: "))
        except ValueError:
            print("Use apenas numeros!!!")
        os.system("cls")
        q1.mudar_valor_lado(mudar)
        os.system("pause")
        os.system("cls")

    elif op == "0":
        cont = 0
        os.system("cls")
        print("Saindo...")
        while cont <=4 :
            cont+=1
            print(f"{cont} ",end="",flush=True)
            sleep(0.8)
        os.system("cls")
        print("\nAté logo")
        break

    else:
        print("Opção invalida!!!")