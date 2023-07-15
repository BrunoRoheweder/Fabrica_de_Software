from pwinput import pwinput

class Conta_Bancaria():

    def __init__(self, nome, cpf, senha, saldo = 0):

        self.nome = nome
        self.__saldo = saldo
        self.__cpf = senha
        self.__senha = senha

    def extrato(self,senha):
        try:
            cpf = int(input("Digite seu cpf: "))
        except ValueError:
            print("Use apenas numeros!!")
        if senha == self.__senha and cpf == self.__cpf:
            print(f"Extrato\nNome: {self.nome}\nCPF: {self.__cpf}\nSaldo: {self.__saldo}\n")
        else:
            print("Senha errada ou cpf errados\nTente novamente.")

    def depositar(self,deposito):
        self.__saldo += deposito
        print(f"O valor depositado foi {deposito}")

    def saque(self,sacar):
        self.__saldo -= sacar
        try:
            senha = int(pwinput("Digite sua senha: "))
        except ValueError:
            print("Use apenas numeros!!")
        if senha == self.__senha:
            print("senha correta")

        if self.__saldo > -1: 
            print(f"o valor sacado foi {sacar}")

        elif self.__saldo <= 0:
            print("Saldo insuficiênte")
            self.__saldo += sacar