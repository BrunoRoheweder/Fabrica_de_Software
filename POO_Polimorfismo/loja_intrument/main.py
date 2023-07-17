from cadastro import*
from Instru_cadastro import*
from pwinput import pwinput
import os

adm_master = Adm("000.000.000-00","Pedrin","4101","CheiraVelha@gmail.com")
adm_master.cadastrar_adm()

class telas:
    def tela_adm():
        while True:
            print(f"""
+=====================================+
|I            Area do ADM            I|
|I [1] >> Adicionar novo ADM         I|
|I [2] >> Cadastar novo instrumento  I|
|I [3] >> Apagar ADM                 I|
|I [4] >> Info pessoal               I|
|I [0] >> Sair                       I|""")
            escolha = input("|I>>")
            if escolha == "1":
                print("""+===================+       
|I     Novo ADM    I|""")
                nome = input(" |I Informe o nome  I|\n|I>> ")
                email = input("|I Informe o email I|\n|I>> ")
                senha = input("|I Informe a senha I|\n|I>> ")
                cpf = input("  |I Informe o CPF   I|\n|I>> ")
                adm = Adm()
                adm.cadastrar_adm()
                print(">> Novo ADM foi cadastrado <<")

        
    def tela_cliente():
        print(f"""
+========================+
|I Loja de Instrumentos I|
|I [1] >> Comprar       I|
|I [0] >> Sair          I|""")

    def menu ():
        while True:
            print("""
+========================+
|I Loja de instrumentos I|
|I [1] >> Cadastro      I|
|I [2] >> Login         I|
|I [0] >> Sair          I|
+========================+""")
            escolha =  input("|I>> ")
            if escolha == "1":
                print("        |I    Cadastro     I|")
                nome = input(" |I Informe o nome  I|\n|I>> ")
                email = input("|I Informe o email I|\n|I>> ")
                senha = input("|I Informe a senha I|\n|I>> ")
                cliente = Usuario(nome, senha, email)
                cliente
                print(">> Cadastro concluido <<")
            elif escolha == "2":
                informe = input("""+======================+
|I        Login       I|
|I Informe o seu nome I|\n|I>> """)
                if informe in adm_master.adms:
                    print(">> Nome encontrado <<")
                    os.system("pause")
                    senha = input("|I Informe sua senha I|\n|I>> ")
                    if adm_master.adms[informe] == senha:
                        print(">> Login concluido <<")
                        os.system("pause")
                        os.system("cls")
                        telas.tela_adm
                    else:
                        print(">> senha incorreta <<")
                else:
                    print(">> nome não encontrado <<")


            print("Cad adm ")
            nome = input("Informa o nome ai \n >>")
            if nome == "0":
                break
            cpf = input("Da seu cpf ai \n >>")
            email = input("Digita seu email ai \n >>")
            senha = int(pwinput("Da sua senha ai, confia \n >>"))
            adm = Adm(cpf,nome , senha, email)
            adm.cadastrar_adm()
        print(adm.adms)
telas.menu()