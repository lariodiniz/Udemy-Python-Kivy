# -*- coding: utf-8 -*-

a = 10
b = 25
c = 66

x = int(input("Digite um numero: "))

#if(x == a or x == b or x == c):
if (x in [a,b,c]):
    print("Esta contido.")
else:
    print("Não esta contido")


cores = ["azul", "amarelo", "vermelho", "branco"]

while True:
    cor = input("Digite o nome de uma cor ou então, 0 para sair do programa: ")

    if (cor=="0"):
        break
    elif cor in cores:
        print("Essa cor está contida!")
    else:
        print("Essa cor não está contida!")