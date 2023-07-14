from class_conta_bancaria import*
from time import sleep
from pwinput import pwinput
import os

while True:
    op = input("1- cadastro\n2- deposito\n3- saque\n4- extrato\n0- Sair\n>>> ")

    if op == "1":
        os.system("cls")
        nome = input("Digite seu nome: ")
        try:
            cpf = int(input("Digite seu cpf: "))
            senha = int(pwinput("Digite sua senha: "))
        except ValueError:
            print("Use apenas numeros!!")

        c1 = Conta_Bancaria(nome, cpf, senha)
        print(8*"=-","Cadastro realizado com sucesso","=-"*8)
        os.system("pause")
        os.system("cls")

    elif op == "2":
        os.system("cls")
        try:
            deposito = float(input("Digite a quantidade para depositar: "))
        except ValueError:
            print("Use apenas numeros!!")
        c1.depositar(deposito)
        os.system("pause")
        os.system("cls")
    
    elif op == "3":
        os.system("cls")
        try:
            sacar = float(input("Digite a quantidade para o saque: "))
        except ValueError:
            print("Use apenas numeros!!")
        c1.saque(sacar)
        os.system("pause")
        os.system("cls")

    elif op == "4":
        os.system("cls")
        try:
            senha = int(pwinput("Digite seua senha: "))
        except ValueError:
            print("Use apenas numeros!!")
        c1.extrato(senha)
        os.system("pause")
        os.system("cls")

    elif op == "0":
        cont = 0
        os.system("cls")
        print("Saindo...")
        while cont <=2 :
            cont+=1
            print(f"{cont} ",end="",flush=True)
            sleep(0.8)
        os.system("cls")
        print("\nAté logo\n")
        break