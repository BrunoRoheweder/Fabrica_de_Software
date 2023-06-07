num = []

for a  in range(10):
    num.append(int(input("Digite um numero: ")))

for neg in num:
    if neg < 0:
        print("Negativo: ",neg)
for pos in num:
    if pos > 0:
        print("Positivo: ",pos)        

