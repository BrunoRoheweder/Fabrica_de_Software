from classs import Pessoa
p1 = Pessoa(input("Digite seu nome: "),int(input("Digite sua idade: ")))
op = input("Você quer comer a maçã que esta na sua frente? ('y'(sim), 'n'(não))\n>>> ")

if op == 'y':
    p1.comer("maçã")

if op == 'n':
    print("você não comeu a maçã")

op = input("Você quer parar de comer? ('y'(sim), 'n'(não))\n>>> ")

if op == 'y':
    p1.parar_comer()

if op == 'n':
    print("Você continua comendo")

op = input("Alguem se aproxima e te pergunta onde esta o controle da tv\nVocê quer falar com esta pessoa? ('y'(sim), 'n'(não))\n>>> ")

if op == 'y':
    p1.falar()
if op == 'n':
    print("Você não fala nada e este alguem fica bravo\nReclama muito e vai embora")

op = input("Você esta falando onde esta o controle\nÉ quando você lembra que foi por sua causa que o controle foi quebrado\nVocê decide em continuar falando ou não? ('y'(sim), 'n'(não))\n>>> ")

if op == 'y':

    p1.falar()

if op == 'n':
    print("Vocês não falou para essa pessoa")