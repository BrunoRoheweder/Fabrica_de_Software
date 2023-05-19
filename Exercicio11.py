'''while True:
    valor = int(input("Digite o valor 1 ou 0 para encerrar: "))
    if valor == 1:
        print("Valor correto")
    else:
        print("Valor para sair")
        break

while True:
    valor1 = int(input("Digite o valor 1 ou 0 para encerrar: "))
    if valor1 >=1:
        continue
    print("Maior que um")
    if valor1 >=1:
        print("Maior qur um")

cont = 101

while cont <= 101:
    cont = cont - 1
    print(cont)
    if cont == 0:
        break
'''

while True:
    
    print("*",70*"-","*")
    print("|",70*" ","|")
    print(("|"+13*" "+"Seja Bem Vindo a Calculadora feita para você!!"+13*" "+"|")) # seja bem vindo
    print("|",70*" ","|")
    print("*",70*"-","*")

    print()
    # aqiu vai ser o numeros e etc...
    print("* ",68*"="," *\n")
    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print(("|"+7*" "+"A.Q"+7*" "+"|"+7*" "+"R.Q"+8*" "+"|"+8*" "+"/"+8*" "+"|"+8*" "+"*"+8*" "+"|")) 
    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print("* ",68*"-"," *")

    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print(("|"+7*" "+"V.C"+7*" "+"|"+8*" "+"9"+9*" "+"|"+8*" "+"+"+8*" "+"|"+8*" "+"-"+8*" "+"|"))
    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2) 
    print("* ",68*"-"," *")

    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print(("|"+7*" "+"M.4"+7*" "+"|"+8*" "+"6"+9*" "+"|"+8*" "+"7"+8*" "+"|"+8*" "+"8"+8*" "+"|"))
    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print("* ",68*"-"," *")

    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print(("|"+8*" "+"F"+8*" "+"|"+8*" "+"3"+9*" "+"|"+8*" "+"4"+8*" "+"|"+8*" "+"5"+8*" "+"|"))
    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print("* ",68*"-"," *")

    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print(("|"+8*" "+"E"+8*" "+"|"+8*" "+"0"+9*" "+"|"+8*" "+"1"+8*" "+"|"+8*" "+"2"+8*" "+"|"))
    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print("* ",68*"="," *")

    print()

    print("* ",68*"="," *")
    caracter = (input(" "*8+"Escolha qual a operação que ira usar a parte\nAviso:Apos escolher esta operaçâo desconsidere a escolha de numeros.\nOperações permitidas: \nM.4 - Media de 4 números\n:"))
    print("* ",68*"="," *")

    print()

    print("* ",68*"="," *")
    print("|"+36*" "+35*" "+"|") 
    num1 = int(input(" "*20+" "))
    caracte = input(" "*20+" ")
    num2 = int(input(" "*20+" "))
    print("|"+36*" "+35*" "+"|") 
    print("* ",68*"="," *")

    print()

    if caracte == '+':
        soma = (num1+num2)

        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print(" "*30+f"{num1} + {num2} = {soma}")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")
        break
    
    elif caracte == '-':
        soma = (num1-num2)

        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print(" "*30+f"{num1} + {num2} = {soma}")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")
        break

    elif caracte == '*':
        soma = (num1*num2)

        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print(" "*30+f"{num1} + {num2} = {soma}")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")
        break
    elif caracte == '/':
        soma = (num1/num2)

        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print(" "*30+f"{num1} + {num2} = {soma}")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")
        break
    elif caracte == 'E':
        soma = (num1 ** num2)

        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print(" "*30+f"{num1} elevado {num2} = {soma}")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")
        break
    elif caracte == 'F':


        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print(" "*30+f"{num1} + {num2} = {soma}")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")
        break
    elif caracte == "R.Q":
        soma = (num1**0.5)

        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print(" "*30+f"{num1} = {soma}")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")
        break
    elif caracte == 'A.Q':
        soma = (num1*num2)

        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print(" "*30+f"'lado'{num1} * 'lado'{num2} = {soma}")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")
        break
    elif caracte == 'V.C':
        

        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print(" "*30+f"{num1} + {num2} = {soma}")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")
        break
    elif caracter == 'M.4':
        nota1 = float(input("Primeira nota: "))
        nota2 = float(input("Segunda nota: "))
        nota3 = float(input("Terceira nota: "))
        nota4 = float(input("Quarta nota:  "))
        soma = ((nota1+nota2+nota3+nota4)/4)

        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print(" "*30+f" as suas notas foram {nota1},{nota2},{nota3},{nota4} é a sua media foi :{soma}")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")
        break
