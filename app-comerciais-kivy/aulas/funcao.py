# coding: utf-8

#declarando uma função
def minha_func():
    print("Helo World")

#parametro de uma Função
def soma(x, y):
    total = x + y
    print("O total da soma de x + y é:", total)

#parametros default
def login(sistema, usuario="root", senha="123"):
    print("Usuario:", usuario)
    print("Senha:", senha)

#parametros nomeados
def dados_pessoais(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}"
    .format(nome, sobrenome, idade, sexo))
"""
dados_pessoais(
    nome="Claudio", 
    idade=30, 
    sobrenome="Carvalho",     
    sexo=True)
"""

#retorno de valores

def multiplicacao(x, y):
    num = x * y
    return num

#retorno de valores multiplos
def func():
    return 1, 2

def potencia(x):
    quadrado = x ** 2
    cubo = x ** 3

    return quadrado, cubo

q, c = potencia(10)

# função variadica
def lista_de_argumentos(*args):
    print(args)

def lista_de_argumentos_associativos(**kwargs):
    print(kwargs)

def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)

lista_de_argumentos(1,2,3,4,5,6)
lista_de_argumentos_associativos(a=1,b=2,c=3,d=4)

argumentos(1,2,3,4,5,6, a=1,b=2,c=3,d=4)