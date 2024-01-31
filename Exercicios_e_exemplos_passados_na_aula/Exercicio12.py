lnome = []
lsobrenome = []
lendereco = []
lbairro = []
lcidade = []
lestado = []
lpais = []
lfone = []
lcpf = []
lpeso = []
laltura = []
lidade = []
ln_do_cartao = []
lemail = []
lcep = []
lnota1 = []
lnota2 = []
lnota3 = []
lnota4 = []
lserie = []
lclasse = []
lsexo = []
lcor = []
lmedia = []

cont = 0


while True:
  
    c = int(input("\nDigite 1 cadastro\nDigite 2 para consulta: "))
    if c == 1:
        nome = (input("Digite seu nome: "))
        lnome.append(nome)
        sobrenome = input("Digite seu sobrenome: ")
        lsobrenome.append(sobrenome)
        idade = input("Digite seu idade: ")
        lidade.append(idade)
        endereco = input("Digite seu endereço: ")
        lendereco.append(endereco)
        bairro = input("Digite seu bairro: ")
        lbairro.append(bairro)
        cidade = input("Digite seu cidade: ")
        lcidade.append(cidade)
        estado = input("Digite seu estado: ")
        lestado.append(estado)
        pais = input("Digite seu pais: ")
        lpais.append(pais)
        fone = input("Digite seu fone: ")
        lfone.append(fone)
        cpf = input("Digite seu CPF: ")
        lcpf.append(cpf)
        peso = input("Digite seu peso: ")
        lpeso.append(peso)
        altura = input("Digite seu altura: ")
        laltura.append(altura)
        n_do_cartao = input("Digite seu numero do cartão: ")
        ln_do_cartao.append(n_do_cartao)
        email = input("Digite seu email: ")
        lemail.append(email)
        cep = input("Digite seu CEP: ")
        lcep.append(cep)
        serie = input("Digite sua serie: ")
        lserie.append(serie)
        classe = input("Digite sua classe: ")
        lclasse.append(classe)
        sexo = input("Digite seu sexo: ")
        lsexo.append(sexo)
        cor = input("Digite sua cor: ")
        lcor.append(cor)
        nota1 = float(input("Digite a primeira nota: "))
        lnota1.append(nota1)
        nota2 = float(input("Digite a segunda nota: "))
        lnota2.append(nota2)
        nota3 = float(input("Digite a terceira nota: "))
        lnota3.append(nota3)
        nota4 = float(input("Digite a quarta nota: "))
        lnota4.append(nota4)
        media = ((nota1+nota2+nota3+nota4)/4)
        lmedia.append(media)
        print(lmedia)
       
        c = int(input("\nDigite 1 para continuar\nDigite 2 para consulta\nDigite 0 para sair:  "))
        
    elif c == 2:
        busca = int(input("Digite o numero da matricula: "))

        print("\nNome:",lnome[busca-1] ,"\nSobrenome: ",lsobrenome[busca-1],"\nIdade: ",lidade[busca-1],"\nEndereço: ",lendereco[busca-1],"\nBairro: ",lbairro[busca-1],"\nCidade: ",lcidade[busca-1]\
        ,"\nEstado: ",lestado[busca-1],"\nPaís: ",lpais[busca-1],"\nFone: ",lfone[busca-1],"\nCPF: ",lcpf[busca-1],"\nPeso: ",lpeso[busca-1],"\nAltura: ",laltura[busca-1]\
        ,"\nNumero do cartão: ",ln_do_cartao[busca-1],"\nEmail: ",lemail[busca-1],"\nCEP: ",lcep[busca-1],"\nNota1: ",lnota1[busca-1],"\nNota2: ",lnota2[busca-1],"\nNota3: ",lnota3[busca-1],"\nNota4: ",lnota4[busca-1]\
        ,"\nSerie: ",lserie[busca-1],"\nClasse: ",lclasse[busca-1],"\nSexo: ",lsexo[busca-1],"\nCor: ",lcor[busca-1],"\nMedia: ",lmedia[busca-1])

        c = int(input("Digite 1 para continuar o cadastro\nDigite 2 para continuar a consulta\nDigite 0 para sair: "))
    
    elif c == 3:
        delete = int(input("Digite a matricula a ser excluida: "))

        del(lnome[delete-1] ,lsobrenome[delete-1],lidade[delete-1],lendereco[delete-1],lbairro[delete-1],\
        lcidade[delete-1],lnome[delete-1],lpais[delete-1],lfone[delete-1],lcpf[delete-1],lpeso[delete-1],\
        laltura[delete-1],ln_do_cartao[delete-1],lemail[delete-1],lcep[delete-1],lnota1[delete-1],lnota2[delete-1],\
        lnota3[delete-1],lnota4[delete-1],lserie[delete-1],lclasse[delete-1],lsexo[delete-1],lcor[delete-1],lmedia[delete-1])

    elif c == 0:
        print("Obrigado volte sempre...")
        break
    else:
        print("\nNumero invalido\n-----Tente Novamente-----\n")