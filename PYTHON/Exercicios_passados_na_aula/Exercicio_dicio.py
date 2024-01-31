# a = {"apple":"maça","ola":"tchau"}

# print(a.values())
# print(a.keys())
# print(a.items())

# for k,v in a.items():

#     print(f"{k},{v}")



# arm = "tchau" in a.values()
# arm1 = "ola" in a.values()

# if arm == False:
#     print("askjdgkajshgdjhkas   false")

# if arm == True:
#     print("askhdkjas   true")


# if arm1 == True:
#     print("td   true")

# if arm1 == False:
#     print("lalalal   false")

# def va():
#     print("olaoaloalaoaloalaoalaoao")

# def main():
#     while True:
#         op = input(">>> ")

#         s = {
#             "ola":va,
            
#         }
#         acao = s.get(op)

#         if acao:
#             acao()
#         else:
#             print("Esta errado. tente novamente")
# main()


# exercicio 1

# nomes = {"Reginaldo": 32,"Igor": 26,"Bruno": 18, "João": 24, "Nicholas": 23}
# print(nomes["Bruno"])
# print(nomes.values())
# print(nomes)

# for k,v in nomes.items():
#     print(k,  v)
  

# exercicio 2

# semana = {"Segunda":"Ederson","Terça":"Mauricio","Quarta":"Ederson","Quinta":"Mauricio","Sexta":"Ederson","Sabado":"python","Domingo":"pyt"}
# for k, v in semana.items():
#     print(k,"=",v)

# exercicio 3

# cpf = input("Digite seu cpf: ")
# num = len(cpf)
# print(num)
c1 =[]
c2 = []
c3 = []
td = []
while True:
    
    menu = int(input("Digite 1 para cadastro e 2 para consultar cadastro\n>>> "))

    if menu == 1:
        cadastro_n = input("\n========-Cadastro-=======\nDigite seu nome:")
        try:
            cadastro_i = int(input("Digite sua idade: "))
        except:
            print("\nUse apenas numeros")
            continue
        try:
            cadastro_f = int(input("Digite seu numero de telefone: "))
        except:
            print("\nUse apenas numeros")
            continue
        td.append(cadastro_n,cadastro_i,cadastro_f)
        c1.append(cadastro_n)
        c2.append(cadastro_i)
        c3.append(cadastro_f)
        try:
            cadastro_c = int(input("Digite seu cpf: "))
            
        except:
            print("\nUse apenas numeros")
            continue
        print("\nCadastro concluido\n")
    if menu == 2:
        try:
            enter = int(input("\n\nDigite seu cpf para consultar o cadastro: "))
        except:
            print("\nUse apenas numeros")
            continue

        if enter == cadastro_c:
            
            for i in td:
                print(i)
            


            vol = input("Digite 0 para voltar ao menu\n>>> ")

            if vol == 0:
                continue
