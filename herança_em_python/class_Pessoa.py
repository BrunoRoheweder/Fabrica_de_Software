from typing import Any


class Pessoa():
    def __init__(self, nome, idade, endereco, cidade, estado):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado

    def relatorio(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"endereco: {self.endereco}")
        print(f"Cidade: {self.cidade}")
        print(f"Estado: {self.estado}")

class Aluno(Pessoa):
    def __init__(self, mensalidade, nome, idade, endereco, cidade, estado):
        super().__init__(nome, idade, endereco, cidade, estado)
        self.mensalidade = mensalidade

        print(12*"=-") 
        super().relatorio()
        print(f"Mensalidade: {self.mensalidade}")
        print(12*"=-")

class Professor(Pessoa):
    def __init__(self, salario, nome, idade, endereco, cidade, estado):
        super().__init__(nome, idade, endereco, cidade, estado)
        self.salario = salario

        print(12*"=-") 
        super().relatorio()
        print(f"Salario: {self.salario}")
        print(12*"=-")


x = Professor("5000", "Ederson", "?", "Senac", "Campo Grande", "MS")

y = Aluno("TI", "Bruno", 18, "Senac", "Campo Grande", "MS")
