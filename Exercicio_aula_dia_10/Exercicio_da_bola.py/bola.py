class Bola:
    
    def __init__(self,cor,circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self):
        trocar = input("Escreva uma cor para trocar: ")
        self.cor = trocar
        print(f"A cor da sua bola trocada com sucesso\nCor trocada para {trocar}")

    def mostrar_cor(self):
        print(f"A cor da sua bola é {self.cor}")
