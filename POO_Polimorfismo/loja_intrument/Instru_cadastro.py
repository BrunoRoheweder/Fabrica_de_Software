from random import randint

class Instrumento():
    
    def __init__(self, nome, valor):
        self.nome = nome
        self.id = (randint(1,10000))
        self.valor = valor
        self.instrumento = {}


    def cadastrar_instru(self):
        self.instrumento[self.id] = self.nome, self.valor
        return self.id


    def apagar_instru(self,id):
        del self.instrumento[id]


    def mostrar_instrumentro(self):
        print(self.instrumento)
