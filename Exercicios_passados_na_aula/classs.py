class Pessoa():
    def __init__(self, nome, idade, falando=False, comendo=False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo

    def comer(self,alimento):
        if self.comendo:
            print(f"{self.nome} Ja esta comendo.")
            return
        if self.falando:
            print(f"{self.nome} não pode comer falando")

        print(f"{self.nome} esta comendo {alimento}.")
        self.comendo = True

    def falar(self):
        if self.falando:
            print(f"{self.nome} Ja esta falando.")
            return
        
        if self.comendo:
            print(f"{self.nome} não pode falar comendo.")
            return
        
        print(f"{self.nome} esta falando.")
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f"{self.nome} não esta falando.")
            return
        print(f"{self.nome} parou de falar.")
        self.falando = False

    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não esta comendo. ")
            return
    
        print(f"{self.nome} parou de comer.")
        self.comendo = False