par=[]
impar=[]
for x in range(10):
    num=int(input("Digite um valor inteiro: "))
    if num%2==0:
        par.append(num)
    elif num%2!=0:
        impar.append(num)
    else:
        ("Número invalido, tente novamente!!!")
print(f"Números impares: {len(impar)}\nNúmeros pares: {len(par)}")

# entender depois