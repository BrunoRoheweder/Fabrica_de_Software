class Conta():
   
    def __init__(self,nome,cpf,fone,conta,agencia,saldo):
        self.nome = nome
        self.cpf = cpf
        self.fone = fone
        self.conta = conta
        self.agencia = agencia
        self.saldo = saldo
        
        
    def sacar(self,saque):
        self.saldo -= saque
        print(f"Saque feito: {saque}\nTotal do saldo: {self.saldo}")
    
    def deposito(self,deposito):
        self.saldo += deposito
        print(f"Deposito feito: {deposito}\nTotal do saldo: {self.saldo}")

    def extrato(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}\nTelefone: {self.fone}\nConta: {self.conta}\nAgencia: {self.agencia}\nSaldo: {self.saldo}")