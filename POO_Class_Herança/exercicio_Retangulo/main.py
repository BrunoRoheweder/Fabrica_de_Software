from retangulo import*
from time import sleep
import os

base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

r1 = Retangulo(base,altura)

while True:
    op = input("1- mudar valor dos lados\n2- mostrar valor dos lados\
\n3- calcular a area\n4- calcular perimetro\n5- redapé\n0- Sair\n>>> ")
    
    if op == "1":
        base = float(input("Digite o valor para mudar da base: "))
        altura = float(input("Digite o valor para mudar da altura: "))
        r1.mudar_valor_lados(base,altura)

    elif op == "2":
        r1.retornar_valor_lados()

    elif op == "3":
        r1.calcular_area()

    elif op == "4":
        r1.calcular_perimetro()

    elif op == "5":
        r1.rodape()

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
        print("Opção Invalida!!!")