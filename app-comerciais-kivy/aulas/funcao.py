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

"""
lista_de_argumentos(1,2,3,4,5,6)
lista_de_argumentos_associativos(a=1,b=2,c=3,d=4)

argumentos(1,2,3,4,5,6, a=1,b=2,c=3,d=4)
"""

#desapacotamento
def pessoa(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)

"""
tupla = ("eXcript", "Brasil", 20)
pessoa(*tupla)


d = {"nome": "eXcript", "idade":20, "sobrenome": "Brasil"} #o nome da chave precisa ser o mesmo nome do argumento da função
pessoa(**d)


lista = [11,10,12]

def funca(a,b,c):
    print(a)
    print(b)
    print(c)

funca(*lista)

"""

# aninhamento de funções

def funcao():
    print("func")

    def func_interna():
        print("Função interna")

    func_interna()

#Intrução NONLOCAL

def func1():

    var_local = 10

    def func_interna():
        nonlocal var_local
        var_local += 1
        print(var_local)
    
    func_interna()

#Intrução global
var_global = 5
def func2():
    
    def func_interna():
        global var_global # Se você quiser alterar um valor de uma variavel global  ou declarar uma variavel global, é necessario usar a palavra reservada global.
        var_global += 1
        print(var_global)
    
    func_interna()

#Bloco de codigo vazio

def func3():
    pass

if (True):
    pass

#Escopo global e local

globals() #retorna uma lista com toda as variaveis globais
locals() # retorna uma lista com todas as variaveis locais