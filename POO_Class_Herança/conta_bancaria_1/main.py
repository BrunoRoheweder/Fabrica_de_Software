from conta import *
import os

def menu():
    while True:
        try:
            op = int(input("1- Cadastro\n2- Saque\n3- Deposito\n4- Extrato\n0- Sair\n>>> "))
        except ValueError:
            print("Use apenas numeros!!!")
            os.system("pause")
            os.system("cls")
            continue

        if op == 1:
            print(8*"=-","Informe seus dados par ao cadastro","=-"*8)

            nome = input("Nome: ")
            try:
                cpf = int(input("CPF: "))
            except ValueError:
                print("Use apenas numeros!!!")
                os.system("pause")
                os.system("cls")
                continue
            try:
                fone = int(input("Telefone: "))
            except ValueError:
                print("Use apenas numeros!!!")
                os.system("pause")
                os.system("cls")
                continue
            try:
                conta = int(input("Conta: "))
            except ValueError:
                print("Use apenas numeros!!!")
                os.system("pause")
                os.system("cls")
                continue
            try:
                agencia = int(input("Agencia: "))
            except ValueError:
                print("Use apenas numeros!!!")
                os.system("pause")
                os.system("cls")
                continue
            try:
                saldo = int(input("Saldo: "))
            except ValueError:
                print("Use apenas numeros!!!")
                os.system("pause")
                os.system("cls")
                continue

            print(8*"=-","Cadastro concluido","=-"*8)
            c1 = Conta(nome,cpf,fone,conta,agencia,saldo)

            os.system("pause")
            os.system("cls")

        elif op == 2:
            try:
                sacar = int(input("Digite a quantia para o saque: "))
                os.system("pause")
                os.system("cls")
                try:
                    c1.sacar(sacar)
                except:
                    os.system("cls")
                    print("Você não tem conta\nCrie uma conta para conseguir sacar")
                    os.system("pause")
                    os.system("cls")
            except ValueError:
                print("Use apenas numeros!!!")
                os.system("pause")
                os.system("cls")

        elif op == 3:
            try:
                deposito = int(input("Digite a quantia para o deposito: "))
                try:
                    c1.deposito(deposito)
                except:
                    os.system("cls")
                    print("Você não tem conta\nCrie uma conta para conseguir depositar")
                    os.system("pause")
                    os.system("cls")
                    continue
               
            except ValueError:
                os.system("cls")
                print("Use apenas numeros!!!")
                os.system("pause")
                os.system("cls")
                continue
            os.system("pause")
            os.system("cls")

        elif op == 4:
            try:
                c1.extrato()
            except:
                os.system("cls")
                print("Conta não existente\nCrie uma conta para conseguir ver o extrato")
                os.system("pause")
                os.system("cls")
                continue


        elif op == 0:
            break   

        else:
            os.system("cls")
            print("Opção não existente!!!\nTente Novamente")
            os.system("pause")
            os.system("cls")
            continue
 
        
menu()