class Usuario():

    def __init__(self,nome,senha,email):
        self.nome = nome
        self.senha = senha
        self.email = email

    def info_pessoal(self):
        print(f"""
|I Nome  | {self.nome} I|
|I Email | {self.email} I|
|I Senha | {self.__senha} I|""")

class Adm(Usuario):

    def __init__(self, cpf, nome, senha, email):
        super().__init__(nome, senha, email)
        self.cpf = cpf  
        self.adms = {}


    def cadastrar_adm(self):
        self.adms[self.nome] = self.senha
        

    def apagar_adm(self,nome):
        del self.adms[nome]
        print(f">> Adm {nome} foi apagado com sucesso <<")
    
    def info_pessoal(self):
        super().info_pessoal()
        print(f"|I cpf   | {self.cpf} I|")

class Comprante(Usuario):

    def __init__(self, nome, senha, email):
        super().__init__(nome, senha, email)
        self.comprates = {}

    def cadastrar_cliente(self): 
        self.comprates[self.__senha] = self.nome, self.email   


