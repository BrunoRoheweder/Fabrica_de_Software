class Retangulo():

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def mudar_valor_lados(self,mudar_base,mudar_altura):
        self.base = mudar_base
        self.altura = mudar_altura
        print(f"A base {self.base} e a altura {self.altura} foram mudadas. Valor do area é {self.base*self.altura}")

    def retornar_valor_lados(self):
        print(f"valor da base: {self.base}\nValor da altura: {self.altura}")

    def calcular_area(self):
        self.area = self.base*self.altura
        print(f"O valor da Area é {self.area}")
        
    def calcular_perimetro(self):
        print(f"O perimetro da area é {(self.base+self.altura)*2}")

    def rodape(self):
        print(f"o rodapé é de {(self.base*self.altura)*0.15}")