import os
from controle import *

marca = input("Digite a marca do controle: ")
tv = ControleRemoto(marca)


tv.ligarTV()
tv.ligarTV()
tv.desligarTV()
tv.ligarTV()
tv.aumentarVolume(75)

