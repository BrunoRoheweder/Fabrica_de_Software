lcand1 = []
lcand2 = []
lcand3 = []

elei = int(input("Digite quanto eleitores tem: "))


for cand in range(elei):
    
    vot = int(input("\nCandidatos:\n1 - Michael Jackson\n2 - Otavio Mesquita\n3 - Zé da Marreta\nDigite o numero do candidato: "))
    

    if vot == 1:
        cand1 = vot
        lcand1.append(cand1)
    elif vot == 2:
        cand2 = vot
        lcand2.append(cand2)
    elif vot == 3:
        cand3 = vot
        lcand3.append(cand3)
    
    else:
        print("\nNumero invalido\nTente Novamente.")
        
arm1 = len(lcand1)
arm2 = len(lcand2)
arm3 = len(lcand3)

if arm1 > arm2 and arm1 > arm3:
    quant1 = arm1
    print(f"\n\nTotal de eleitores: {elei}\nOs Candidatos votados foi:\n1 - Michael Jackson {len(lcand1)}\
    \n2 - Otavio Mesquita {len(lcand2)} \n3 - Zé da Marreta {len(lcand3)}\nO Candidato mais votado foi: Michael Jackson com {quant1} de votos")

elif arm2 > arm1 and arm2 > arm3:
    quant2 = arm2
    print(f"\n\nTotal de eleitores: {elei}\nOs Candidatos votados foi:\n1 - Michael Jackson {len(lcand1)}\
    \n2 - Otavio Mesquita {len(lcand2)} \n3 - Zé da Marreta {len(lcand3)}\nO Candidato mais votado foi: Otavio Mesquita com {quant2} de votos")

elif arm3 > arm1 and arm3 > arm2:
    quant3 = arm3
    print(f"\n\nTotal de eleitores: {elei}\nOs Candidatos votados foi:\n1 - Michael Jackson {len(lcand1)}\
    \n2 - Otavio Mesquita {len(lcand2)} \n3 - Zé da Marreta {len(lcand3)}\nO Candidato mais votado foi: Zé da Marreta com {quant3} de votos")
else:
    print("\nNenhum candidato foi votado ou deu empate\nPor Favor Tente Novamente.")