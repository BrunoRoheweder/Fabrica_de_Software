from class_conta_bancaria import*

nome = input("Digite seu nome: ")
saldo = input("Digite seu saldo: ")
cpf = input("Digite seu cpf: ")
senha = input("Digite sua senha: ")

c1 = Conta_Bancaria(nome, saldo, cpf, senha)

while True:
    op = input("1- cadastro\n2- saldo\n3- saque\n4- deposito\n0- Sair\n>>> ")

    if op == "1":
        c1.extrato()

    elif op == "2":
        depositar = float(input("Digite a quantidade para depositar: "))
        c1.depositar(depositar)
    
    elif op == "3":
        saque = float(input("Digite a quantidade para o saquq: "))
        c1.saque(saque)