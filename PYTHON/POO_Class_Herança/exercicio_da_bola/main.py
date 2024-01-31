from bola import*
import os
def menu():
    while True:
        try:
            print(8*"=-","Menu da sua bola","=-"*8)
            op = int(input("1- cadastro da bola\n2- trocar cor\n3- mostrar cor\n0- Sair\n>>> "))
        except ValueError:
            os.system("cls")
            print("Digite apenas numeros!!!")
            os.system("pause")
            os.system("cls")
            continue
        if op == 1:
            os.system("cls")
            print(8*"=-","Cadastro da sua bola","=-"*8)

            cor = input("Digite a cor da sua bola: ")
            circunferencia = input("Digite a circunferencia da sua bola: ")
            material = input("Digite o material da sua bola: ")
            os.system("cls")
            print(8*"=-","Cadastro da sua bola esta concluida","=-"*8)

            b1 = Bola(cor,circunferencia,material)
            os.system("pause")
            os.system("cls")

        elif op == 2:
            os.system("cls")
            b1.trocar_cor()
            os.system("pause")
            os.system("cls")

        elif op == 3:
            os.system("cls")
            b1.mostrar_cor()
            os.system("pause")
            os.system("cls")

        elif op == 0:
            break

        else: 
            print("Opção não existente")
            os.system("pause")
            os.system("cls")
            continue
menu()