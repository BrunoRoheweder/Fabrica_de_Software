class Conta_Bancaria():

    def __init__(self,nome,saldo,cpf,senha):

        self.nome = nome
        self.__saldo = saldo
        self.__cpf = senha
        self.__senha = senha

    def extrato(self,senha):
        if senha == self.__senha:
            print(f"Extrato\nNome: {self.nome}\nCPF: **********\nSaldo: *****\nSenha: **********")
        else:
            print("Senha Errada\nTente novamente.")

    def depositar(self,deposito):
        self.deposito = deposito
        self.__saldo = self.__saldo + self.deposito
        print(f"O valor depositado foi {deposito}")

    def saque(self,sacar):
        self.__saldo = self.__saldo - sacar
        print(f"o valor sacado foi {sacar}")
