class ControleRemoto():

    def __init__(self,marca,ligar = False,mudarCanal = False,volume = False):

        self.marca = marca
        self.ligar = ligar
        self.mudarCanal = mudarCanal
        self.volume = volume

    def ligarTV(self):
        if self.ligar:
            print(f"O controle da marca {self.marca} ja ligou a TV")
            return
        print(f"O controle da marca {self.marca} ligou a TV")
        self.ligar = True

    def desligarTV(self):
        if not self.ligar:
            print(f"O controle da marca {self.marca} ja desligou a TV")
            return
        print(f"O controle da marca {self.marca} desligou a TV")
        self.ligar = False
        
    def mudar_canal(self,canal):
        
        self.canal = canal
        print(f"O controle da marca {self.marca} mudou de canal para o canal {self.canal}")
        self.mudarCanal = True

    def aumentarVolume(self,aumentar):
        self.aumentar = aumentar
        print(f"O controle da marca {self.marca} aumentou o volume para {self.aumentar}")
        self.volume = True
    
    def baixarVolume(self,aumentar):
        self.aumentar = aumentar
        print(f"O controle da marca {self.marca} abaixou o volume para {self.aumentar}")
        self.volume = False
