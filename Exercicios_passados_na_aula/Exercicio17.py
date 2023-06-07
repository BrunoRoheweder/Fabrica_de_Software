#============================
#lista de cadastro do cliente
lista_cadastro_cliente = []
lnome =[]
lsobrenome = []
lrg = []
lcpf = []
lendereco = []
lfone = []
lidade = []
#============================
#lista de cadastro de passagem
lista_cadastro_passagem =[]
ldestino = []
lorigem = []
lduracao = []
lvalor_passagem = []
desconto = []
#============================
#lista de cadastro do Avião
lista_cadastro_de_voo =[]
lmodelo = []
lano = []
lhoras_de_voo =[]
lcor = []
lquantidade_de_passageiros = []
#============================
#lista de cadastro de Tripulação
lista_cadastro_de_tripulacao = []
lnome_tripu = []
ldescricao_cargo = []
lidade_tripu = []
ldata_de_admissao = []
lfone_tripu = []
#============================
todasL = [lista_cadastro_cliente,lista_cadastro_passagem,lista_cadastro_de_voo,lista_cadastro_de_tripulacao]   # JUntando as listas


import os

while True:
    print("=-="*5+" Menu "+5*"=-=")
    try: 
        inicio = int(input("\n1 - Cadastro do Cliente\n2 - Cadastro de Passagem\
            \n3 - Cadastro do Avião\n4 - Cadastro de Tripulação\n5 - Mostrar Cadastros\n0 - Sair\nEscolha:"))        #Menu
        if inicio == 0:         # sair do programa
            break           
    
        if inicio == 5:
            print("\nMostrar os Cadastros")
            print("\n",lista_cadastro_cliente,"\n",lista_cadastro_passagem,"\n",lista_cadastro_de_voo,"\n",lista_cadastro_de_tripulacao)        # junta as lista de cada cadastro
            break
           
        while True:
            
            if inicio == 1:     #Cadastro do Cliente
                print("\nSeja Bem Vindo ao cadastro do Cliente")
                

                nome = input("Digite seu nome: ")           # nome
                lista_cadastro_cliente.append(nome)
                lnome.append(nome)
               
                os.system('cls')

                sobrenome = input("Digite seu sobrenome: ")     # sobrenome
                lista_cadastro_cliente.append(sobrenome)
                lsobrenome.append(sobrenome)
               
                os.system('cls')
                try:
                    rg = int(input("Digite seu RG: "))      #RG
                    lista_cadastro_cliente.append(rg)
                    lrg.append(rg)
                  
                    os.system('cls')
                except:
                    print("Usar apenas Numero\nTente Novamente.")
                    os.system('pause')
                    continue
                try:
                    cpf = int(input("Digite seu CPF: "))        #CPF
                    lista_cadastro_cliente.append(cpf)
                    lcpf.append(cpf)
                   
                    os.system('cls')
                except:
                    print("Usar apenas Numero\nTente Novamente.")
                    os.system('pause')
                    continue
                endereco = input("Digite seu endereço: ")       #Endereço
                lista_cadastro_cliente.append(endereco)
                lendereco.append(endereco)
               
                os.system('cls')
                try:
                    fone = int(input("Digite o numero de telefone: "))      #Telefone
                    lista_cadastro_cliente.append(fone)
                    lfone.append(fone)
                  
                    os.system('cls')
                except:
                    print("Usar apenas Numeros\nTente Novamente.")
                    os.system('pause')
                    continue
                try:
                    idade = int(input("Digite sua idade: "))        #Idade
                    lista_cadastro_cliente.append(idade)
                    lidade.append(idade)
                  
                    os.system('cls')
        
                except:
                    print("Usar apenas Numeros\nTente Novamente.")
                    os.system('pause')
                    continue
                print("Cadastro com sucesso!!!")
                break
            while True:
                if inicio == 2:       # Cadastro de Passagem

                    print("\nSeja Bem Vindo ao cadastro de Passagem")
                

                    destino = input("Digite seu destino: ")     #Destino
                    ldestino.append(destino)
                    lista_cadastro_passagem.append(destino)
                  
                    os.system('cls')

                    origem = input("Digite sua origem: ")       #Origem
                    lorigem.append(origem)
                    lista_cadastro_passagem.append(origem)
                    
                    os.system('cls')

                    duracao = input("Digite sua duração: ")     #Duração
                    lduracao.append(duracao)
                    lista_cadastro_passagem.append(duracao)
                    
                    os.system('cls')
                    try:

                        valor_passagem = float(input("Digite o valor da passagem: "))       #Valor da passagem
                        lvalor_passagem.append(valor_passagem)
                        lista_cadastro_passagem.append(valor_passagem) 
                    except:
                        print("Usar apenas Numeros\nTente Novamente.")
                        os.system('pause')
                    soma = (valor_passagem*5)/100       # soma de desconto de 5% da passagem
                    desconto.append(soma)
                    print(soma)

                    os.system('cls')
                    print("Cadastro com sucesso!!!")
                    break
            while True:
                if inicio == 3:           # Cadastro do Avião

                    print("\nSeja Bem Vindo ao cadastro do Avião")
                
                
                    modelo = input("Digite o modelo: ")         #modelo
                    lmodelo.append(modelo)
                    lista_cadastro_de_voo.append(modelo)
                   
                    os.system('cls')

                    ano = input("Digite o ano: ")           # Ano
                    lano.append(ano)
                    lista_cadastro_de_voo.append(ano)
                 
                    os.system('cls')
                    try:

                        horas_de_voo = int(input("Digite a quantidade de horas de voo: "))      #Horas De VOO
                        lhoras_de_voo.append(horas_de_voo)
                        lista_cadastro_de_voo.append(horas_de_voo)
                       
                        os.system('cls')
                    except:
                        print("Usar apenas Numeros\nTente Novamente.")
                        os.system('pause')
                        continue
                    cor = input("Digite a cor do Avião: ")          # Cor
                    lcor.append(cor)
                    lista_cadastro_de_voo.append(cor)
              
                    os.system('cls')

                    quantidade_de_passageiros = int(input("Digite a quantidade de passageiros: "))      # quantidade de passageiros
                    lquantidade_de_passageiros.append(quantidade_de_passageiros)
                    lista_cadastro_de_voo.append(quantidade_de_passageiros)
                 
                    os.system('cls')
                    print("Cadastro com sucesso!!!")
                    break
            while True:
                if inicio == 4:       # Cadastro de Tripulação

                    print("\nSeja Bem Vindo ao cadastro de Tripulação")
                

                    nome_tripu = input("Digite os nomes da tripulaçao: ")       # Nome da tripulação
                    lnome_tripu.append(nome_tripu)
                    lista_cadastro_de_tripulacao.append(nome_tripu)
                  
                    os.system('cls')

                    descricao_cargo = input("Digite a descrição de cargo: ")        # descrição do cargo
                    ldescricao_cargo.append(descricao_cargo)
                    lista_cadastro_de_tripulacao.append(descricao_cargo)
                 
                    os.system('cls')
                    try:

                        idade_tripu = int(input("Digite a idade da tripulação: "))      # Idade da tripulação
                        lidade_tripu.append(idade_tripu)
                        lista_cadastro_de_tripulacao.append(idade_tripu)
                   
                        os.system('cls')
                    except:
                        print("Usar apenas Numeros\nTente Novamente.")
                        os.system('pause')
                        continue
                    data_de_admissao = input("Digite a data de admissão: ")     # data de admissão
                    ldata_de_admissao.append(data_de_admissao)
                    lista_cadastro_de_tripulacao.append(data_de_admissao)
                 
                    os.system('cls')
                    try:

                        fone_tripu = int(input("Digite o telefone da tropulação: "))        # Telefone da tripulação
                        lfone_tripu.append(fone_tripu)
                        lista_cadastro_de_tripulacao.append(fone_tripu)
                   
                        os.system('cls')
                    except:
                        print("Usar apenas Numeros\nTente Novamente.")
                        os.system('pause')
                        continue
                    print("Cadastro com sucesso!!!")
                    break
            # while True:
            #     if inicio == 5:
            #         print("\nMostrar os Cadastros")
            #         print("\n",lista_cadastro_cliente,"\n",lista_cadastro_passagem,"\n",lista_cadastro_de_voo,"\n",lista_cadastro_de_tripulacao)        # junta as lista de cada cadastro
            #     break
           
    except :
        print("\nInvalido\nDigite apenas os numeros que estão no menu\n")
        