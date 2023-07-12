class Quadrado():

    def __init__(self,tamanho_do_lado):
        self.tamanho = tamanho_do_lado

    def mostrar_area(self):
        print(f"\nO tamanho do quadrado é {self.tamanho}\n")

    def mudar_valor_lado(self, mudar_valor):
        self.tamanho = mudar_valor**2
        print(f"\nTamanho do quadrado mudado foi: {self.tamanho}\n")