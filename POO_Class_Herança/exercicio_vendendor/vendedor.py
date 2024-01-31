class Vendedor():
    
    def __init__(self,nome,vendas):

        self.nome = nome
        self.vendas = vendas
    
    def vendeu(self,vendas):
        self.vendas = vendas
        print(f"{self.nome} vendeu {self.vendas}")

    def bateu_meta(self,meta):
        if self.vendas > meta:
            print(f"{self.nome} bateu a meta")
        else:
            print(f"{self.nome} não bateu a meta.")
    
