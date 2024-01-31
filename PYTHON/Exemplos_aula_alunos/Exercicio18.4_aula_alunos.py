from tkinter import *
import tkinter as tk

def tela2():
    tela2 = Tk()
    tela2.geometry("400x400")
    tela2.config(bg="lightBlue")
    textin = Label(tela2,text="""
    Tkinter é uma biblioteca da linguagem Python
    que acompanha a instalação padrão e permite 
    desenvolver interfaces gráficas. Isso 
    significa que qualquer computador que tenha
    o interpretador Python instalado é capaz de
    criar interfaces gráficas usando o Tkinter,
    com exceção de algumas distribuições Linux, 
    exigindo que seja feita o download do módulo
    separadamente.""",bg="lightblue").pack(fill=BOTH,expand=True)
    botao_volta = Button(tela2,text="Voltar", command=tela2.destroy,bg="Red")
    botao_volta.pack(side="right")

def tela3():
    tela3 = Tk()
    tela3.geometry("400x400")
    tela3.config(bg="lightblue")
    textin = Label(tela3,text="""
    Um dos motivos de estarmos usando o Tkinter 
    como exemplo é a sua facilidade de uso e 
    recursos disponíveis. Outra vantagem é que
    é nativo da linguagem Python, tudo o que
    precisamos fazer é importá-lo no momento
    do uso, ou seja, estará sempre disponível.
    """,bg="lightblue").pack(fill=BOTH,expand=True)
    botao_volta = Button(tela3,text="Voltar", command=tela3.destroy,bg="Red")
    botao_volta.pack(side="right")
    
def tela4():
    tela4 = Tk()
    tela4.geometry("400x400")
    tela4.config(bg="lightblue")
    textin = Label(tela4,text="""
    Um dos motivos de estarmos usando o Tkinter 
    como exemplo é a sua facilidade de uso e 
    recursos disponíveis. Outra vantagem é que
    é nativo da linguagem Python, tudo o que
    precisamos fazer é importá-lo no momento
    do uso, ou seja, estará sempre disponível.
    """,bg="lightblue").pack(fill=BOTH,expand=True)
    botao_volta = Button(tela4,text="Voltar", command=tela4.destroy,bg="Red")
    botao_volta.pack(side="right")


tela_principal = Tk()
tela_principal.geometry("300x300")

botao = Button(tela_principal,text="O que é o Tkinter?", command=tela2, bg="yellow",fg="Blue")
botao.pack(fill=BOTH,expand=True)

botao2= Button(tela_principal,text="Porque usar Tkinter?", command=tela3, bg="Blue",fg="yellow")
botao2.pack(fill=BOTH,expand=True)

botao3= Button(tela_principal,text="Conceitos de GUI", command=tela4, bg="lightblue")
botao3.pack(fill=BOTH,expand=True)

botao_sair =Button(tela_principal,text="Sair", command=tela_principal.quit, bg="lightblue")
botao_sair.pack(fill=BOTH,expand=True)

tela_principal.title("Tkinter")
tela_principal.mainloop()