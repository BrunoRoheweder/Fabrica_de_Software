# def somaImposto(taxaImposto, custo):
#     soma  = (taxaImposto + taxaImposto * custo/100)
#     return soma


# taxaS = float(input("sem imposto: "))
# taxaC = float(input("Taxa do impoto: "))

# print(somaImposto(taxaS,taxaC))

# def conversao_horas(horas, minutos):
#     try:
#         if horas >= 12 <= 24:  # P.M para A.M
#             horas = horas - 12
#             print(f"{horas}:{minutos} A.M")

#         elif horas >= 1 < 12 :  # A.M para P.M
#             horas = horas + 12
#             print(f"{horas}:{minutos} P.M")

#         else:
#             print(f"{horas}:{minutos} A.M")
#     except:
#         print()
# try:
#     horas = int(input("Horas: "))
#     minutos = int(input("Minutos: "))

#     conversao_horas(horas, minutos)
# except:
#     print("Ultilizar apenas numeros")

lvalor = []
lnum_dias = []
lsoma = []
lmulta = []
def valorPagamento(valor_pre, num_dias_atras):

    if dias > num_dias_atras:
        soma_um_pocent = ((num_dias_atras*1)/100) + valor_pre
        lsoma.append(soma_um_pocent)
      
    if dias < num_dias_atras:
        multa = (num_dias_atras*3)/100
        lmulta.append(multa)

    print(f"Valor a ser pago {lsoma + lmulta}")
while True:
    valor = float(input("Valor das prestações: "))
    num_dias = int(input("Numero de dias em atraso: "))


    lvalor.append(valor)
    lnum_dias.append(lnum_dias)

    valorPagamento(valor, num_dias)