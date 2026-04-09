"""Nível Básico (Aquecimento)
1- Soma Infinita: Crie uma função soma_total(*args) que receba qualquer quantidade de números e 
retorne a soma deles.

2- Saudação Personalizada: Crie uma função que receba um nome fixo e, em seguida,
vários "títulos" via *args (ex: "Doutor", "Mestre"). A função deve imprimir: "Olá [títulos] [nome]".

3- Dicionário de Carro: Crie uma função descrever_carro(marca, modelo, **kwargs) 
que receba a marca e modelo obrigatoriamente, e características extras (cor, ano, teto_solar) 
via **kwargs. Imprima o dicionário final."""

#Exercício 1:
def soma_total(*args):
    total = 0
    for item in args:
        total += item
    return total

print(soma_total(1, 59, 10, 100, 3))



#Exercício 2:
def saudacao(nome, *args):
    titulos = " ".join(args)
    print(f"Olá {titulos} {nome}")

saudacao("Fulano", "Doutor", "Mestre")

#Exercício 3:
def descrever_carro(marca, modelo, **kwargs):
    print(f"Veículo {marca.upper()} {modelo.capitalize()}\nCaracterísticas:\n", end="")
    for key, value in kwargs.items():
        formated_key = key.replace("_", " ").capitalize()
        print(f"- {formated_key}: {str(value).capitalize()}")

descrever_carro("volks", "voyage", cor="prata", ano=2013, teto_solar="nao")