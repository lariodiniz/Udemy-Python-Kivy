#1) Faça um algoritmo que imprima os números no intervalo entre 1 e 100:

for i in range(1,101):
    print(i)

#2) Evolua o algoritmo no qual imprimimos os números num intervalo pré-definido para um algoritmo que pergunte ao usuário qual o intervalo que o mesmo deseja que seja impresso:

numero_inicial = int(input("Informe o inicio do intervalo: "))
numero_final = int(input("Informe o final do intervalo: "))

for i in range(numero_inicial,numero_final+1):
    print(i)

#3) Faça um algoritmo que imprima os números no intervalo entre 1 e 10 em ordem inversa:

for i in range(10,0, -1):
    print(i)

#4) Faça um algoritmo que imprima os números pares entre 0 e 100:

for i in range(0,101,2):
    print(i)

#5) Faça um algoritmo que some a quantidade de números pares encontrados no 
# intervalo entre 0 e 100:

soma = 0
for i in range(0,101,2):
    soma+=i
print(soma)

#6) Faça um algoritmo que imprima os números primos entre 0 e 100:

for num in range(0,101):
    div = 0
    for n in range(1,num+1):
        if (num % n == 0):
            div += 1
    
    if (div == 2):
        print(num,"é um numero primo!")

#7) Faça um algoritmo que calcule os número primos num intervalo 
# pré-determinado pelo usuário:

numero_inicial = int(input("Informe o inicio do intervalo: "))
numero_final = int(input("Informe o final do intervalo: "))
for num in range(numero_inicial,numero_final+1):
    div = 0
    for n in range(1,num+1):
        if (num % n == 0):
            div += 1
    1
    if (div == 2):
        print(num,"é um numero primo!")

#8) Faça um algoritmo que imprima os valores no intervalo definido 
# pelo usuário e permita que o mesmo possa definir 3 números que deverão 
# ser ignorados, ou seja, que não serão impressos na tela:

numero_inicial = int(input("Informe o inicio do intervalo: "))
numero_final = int(input("Informe o final do intervalo: "))
numero_ignorado1 = int(input("Informe o primeiro numero que será ignorado: "))
numero_ignorado2 = int(input("Informe o segundo numero que será ignorado: "))
numero_ignorado3 = int(input("Informe o terceiro numero que será ignorado: "))

for num in range(numero_inicial,numero_final+1):
    if (num == numero_ignorado1) or (num == numero_ignorado2) or (num == numero_ignorado3):
        continue
    print(num)

#9) Faça um algoritmo que imprima a frase "estou em looping" e, 
# em seguida, solicite ao usuário digitar uma letra. 
# Caso a letra seja o "q" finalize a aplicação. 
# Do contrário, imprima novamente a mesma frase até que o caractere "q" seja enviado:


while(True):
    print("estou em looping")
    c = input("Digite uma letra: ")

    if ( c == "q"):
        break
