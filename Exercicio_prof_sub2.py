lista = []
num = 0

for a in range(10):
    num = num + 1
    lista.append(int(input(f"Digite o {num}º numero: ")))
print(sum(lista))
