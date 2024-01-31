import wikipedia

buscar = input("Digite sua pesquisa: ")
wiki = wikipedia.set_lang("pt")
resposta = wikipedia.summary(buscar)
print(resposta)
