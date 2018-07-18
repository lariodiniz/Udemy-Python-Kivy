#1) Escreva um algoritmo que contenha uma função de nome estudo() e que quando 
# executada imprima na saída padrão a frase "Estamos estudando as funções":

def estudos():
    print("Estamos estudando as funções")

estudos()

#2) Escreva um código contendo uma função de nome estudo e defina que a mesma 
# deva receber um número como argumento. Chame este argumento de x. 
# No corpo da função imprima a seguinte frase na tela: 
# "Função invocada com sucesso. O valor passado pelo argumento x é: <valor de x>"

def estudo(x):
    print("Função invocada com sucesso.",
    "O valor passado pelo argumento x é:", x)

estudo(10)

#3) Escreva um algoritmo que receba dois números através da declaração 
# de dois parâmetros cujos nomes serão: x e y. No bloco de instrução faça a 
# soma de ambos valores e imprima o resultado no monitor:

def estudo(x, y):
    soma = x + y
    print("A soma de",
    x,
    "com",
    y,
    "é:", soma)

estudo(10, 15)

#4) Escreva um algoritmo contendo uma função que necessite de três argumentos. 
# Em seguida, imprima na tela os argumentos em ordem ascendente e, por fim, 
# imprima a média aritmética:

def estudo(x, y, z):
    numeros = [x, y, z]
    numeros.sort()
    print("os numeros na ordem ascendente são",
    *numeros)
    print("a média aritmédica é: ",(x+y+z) /3)

estudo(7, 5, 7)

#5) Escreva uma função que contenha dois parâmetros. 
# O primeiro deve ser obrigatório e o segundo facultativo:

def estudo(x, y=0):    
    pass

estudo(7)

#6) Escreva uma função que invocará outra função na qual tenha dois 
# parâmetros definidos. 
# Invoque a primeira função de ``func1()`` e a segunda de ``func2()``. 
# Em seguida, 
# invoque os parâmetros da segunda função de x e y. 
# Some x e y e retorne o resultado. 
# Em func1(), ao receber o resultado, 
# retorne-o também como valor de retorno da função. 
# Por fim, imprima na tela o valor que foi calculado por func2(), 
# retornado para func1() e retornado a quem invocou a função inicialmente:

def func1():

    def func2(x, y):
        return x + y

    return func2(10,20)

print(func1())

#7) Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros. 
# Em seguida, imprima os parâmetros recebidos na tela:

def func(*args):
    print(*args)

func(1,2,3,4,5,6)

#8) Escreva um algoritmo capaz de receber uma quantidade variável de parâmetros 
# que estejam associados a uma chave. Em seguida, 
# imprima na tela o nome da chave e o respectivo valor:

def func(**kwargs):
    for k in kwargs:
        print("Chave" ,k , end =' - ')
        print("Valor", kwargs[k])

d1 = {'a': 10, 'b':15}

func(**d1)

#9) Considere o trecho de código a seguir.

#def func(a, b, c, d)
#    print(a+b+c+d)
#lista = 1,2,3,4
#Invoque a função func(), passando como argumento os valores contidos em lista, 
# com a respectiva ordem, de forma a utilizar o conceito de desempacotamento:

def func(a, b, c, d):
    print(a+b+c+d)
lista = 1,2,3,4

func(*lista)

#10) Escreva um algoritmo que encontre o maior dentre 3 números. 
# Para facilitar a resolução do exercício utilize funções.

def maior_entre_tres_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort(reverse=True)
    return numeros[0]

print(maior_entre_tres_numeros(8,5,6))

#11) Escreva um função que some todos os números contidos numa lista.
#Lista: (1, 2, 3, 4, 5)
#Soma: 15

def soma_lista(*args):
    soma = 0
    for n in args:
        soma += n
    
    print(soma)

soma_lista(*(1, 2, 3, 4, 5))  

#12) Escreva uma função que multiplique todos os números de uma lista.
#Lista: (1, 2, 3, 4, 5)
#Multiplicação: 120

def multiplica_lista(*args):
    mult = 1
    for n in args:
        mult *= n
    
    print(mult)

multiplica_lista(*(1, 2, 3, 4, 5))  

#13) Escreva uma função que inverta a ordem dos elementos de uma lista manualmente. 
# Não utilize a função interna do Python que faz inverção, 
# crie o algoritmo que faça a inversão.
#Lista: "1234abcd"
#Saída: "dcba4321"

def inverte_lista(lista):
    nova_lista = []
    i = len(lista) -1
    while i >= 0 :
        nova_lista.append(lista[i])
        i -= 1
    return nova_lista

print(inverte_lista([1,2,3,4,"a","b","c","d"]))

#14) Escreva uma função que calcule o fatorial de um número 
# (um inteiro não negativo). Envie o valor do número que será calcula como 
# argumento da função.

def fatorial(x):
    if x == 1:
        return 1
    else:
        return x * fatorial(x-1)

print(fatorial(4))


#15) Escreva uma função que verifique se um número está num intervalo determinado.

def numero_em_intervalo(num, intervalo1 = 0, intervalo2 = 10):
    if (num >= intervalo1) and (num <= intervalo2):
        print("O número esta dentro do intervalo")
    else:
        print("O número não esta dentro do intervalo")

numero_em_intervalo(11)

#16) Escreva uma função que aceite Strings e calcule a quantidade de letras 
# em mauisculas e minúsculas que a String possui.

def verifica_letras(letras):
    maiusculas = 0
    minusculas = 0
    for letra in letras:
        if letra in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N",
                    "O","P","Q","R","S","T","U","W","V","X","Y","Z"]:
            maiusculas +=1
        elif letra in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
                    "o","p","q","r","s","t","u","w","v","x","y","z"]:
            minusculas +=1
    
    print("A palavra", letras, "tem", minusculas,"letras minusculas e", maiusculas, "letras maiusculas.")
verifica_letras("LArio")

#17) Escreva uma função que receba como argumento uma lista que poderá ter valores 
# duplicados e retorne uma nova lista sem que haja valores iguais.
#Lista: [1,2,3,3,3,3,4,5]
#Retorno: [1, 2, 3, 4, 5]

def remove_duplicados(lista):
    nova_lista = []

    for item in lista:
        if nova_lista.count(item) == 0:
            nova_lista.append(item)
    
    return nova_lista

print(remove_duplicados([1,2,5,6,5,4,6,6, "Casa", "Carro", "barco", "Carro", "Barco"]))    

#18) Escreva uma função capaz de receber uma quantidade indeterminada de 
# parâmetros e imprima na telas os números primos contidos nessa lista.

def imprime_primos(*args):

    def eh_divisor(numero1, numero2):
        return (numero1 % numero2 == 0)

    def eh_primo(numero):       
        div = 0
        for num in range(1,numero+1):
            if eh_divisor(numero, num):
                div += 1  

        return (div == 2)

    imprimir = []
    for numero in args:
        if eh_primo(numero) and (imprimir.count(numero) == 0):
            imprimir.append(numero)
    print("Os numeros primos são: ", end=" ")

    for numero in imprimir:
        print(numero, end=", ")

imprime_primos(1,2,3,4,5,6,7,8,9,10)

#19) Escreva uma função que imprima somente os números pares
#Lista: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Saída: [2, 4, 6, 8]

def imprime_pares(lista):

    def eh_par(numero1):
        return (numero1 % 2 == 0)    

    imprimir = []
    for numero in lista:
        if eh_par(numero) and (imprimir.count(numero) == 0):
            imprimir.append(numero)
    print("Os numeros pares são: ", end=" ")

    for numero in imprimir:
        print(numero, end=", ")

imprime_pares([1, 2, 3, 4, 5, 6, 7, 8, 9])

#20) Escreva uma função que verifica se uma String enviada é um palíndromo ou não.

def eh_palindromo(frase):
    return frase.replace(" ", "") == frase[::-1].replace(" ", "")

print(eh_palindromo("socorram me subi no onibus em marrocos"))

#21) Escreva uma função que tenha definida uma função em seu escopo. 
# Invoque a função aninhada, retorne algum valor, 
# imprima esse valor na tela e finalize a aplicação.

def func():
    def func2():
        return 10
    print(func2())
func()