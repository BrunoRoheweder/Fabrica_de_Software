class Carro():

    def __init__(self, nome, placa, cor, andar = False):
        self.nome = nome
        self.placa = placa
        self.cor = cor
        self.andar = andar


    def andando(self):
        if self.andar:
            print(f"O {self.nome} ja esta andando")
            return
        print(f"O {self.nome} esta andando")
        self.andar = True
        
    def para_andar(self):
        if not self.andar:
            print(f"O {self.nome} ja porou de andar")
            return
        print(f"O {self.nome} parou de andar")
        self.andar = False
        

car = Carro("Uno", "JAH-3456", "Prata")
car.andando()
car.andando()
car.para_andar()
car.andando()