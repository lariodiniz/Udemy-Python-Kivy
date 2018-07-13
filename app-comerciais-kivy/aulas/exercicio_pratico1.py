'''
#1 - Faça um algoritmo que apenas imprima o seu nome na tela e 
# em seguida finalize a aplicação.
print("Lário dos Santos Diniz")


#2 - Faça um algoritmo que solicite ao usuário digitar o seu 
# nome e em seguida envie a seguinte frase para a saída padrão: 
# "O seu nome é: [nome do usuário]".

nome = input("Digite o seu nome: ")
print("O seu nome é:", nome)

#3 - Faça um algoritmo que solicite o nome e a idade do usuário e então, 
# envie a seguinte frase para o Console: 
# "O seu nome é <nome> e a sua idade é <idade>".

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
print("O seu nome é", nome, "e a sua idade é ", idade)


#4 - Faça um algoritmo que solicite ao usuário informar um número. 
# Em seguida, armazene este número numa variável. 
# Por fim, envie esse número para a saída padrão.
num1 = int(input("Informe um numero: "))
print(num1)

#5 - Faça um algoritmo que solicite ao usuário informar um número. 
# Em seguida, escreva a seguinte mensagem: "O número digitado foi: ".
num1 = int(input("Informe um numero: "))
print("O numero digitado foi:", num1)

#6 - Faça um algoritmo que solicite ao usuário informar 3 números. 
# Em seguida, some-os e envie para a saída padrão a seguinte frase: 
# "A soma total é: "
num1 = int(input("Informe um numero: "))
num2 = int(input("Informe outro numero: "))
num3 = int(input("Informe mais um numero: "))
print("A soma total é:", num1+num2+num3)

# 7 - Faça um algoritmo que solicite ao usuário informar 2 números. 
# Em seguida, some os valores e envie para a saída padrão a seguinte frase: 
# "A soma entre <X> e <Y> é igual <total>".

num1 = int(input("Informe um numero: "))
num2 = int(input("Informe outro numero: "))

print("A soma entre", num1, "e", num2, "é igual", num1+num2)


# 8 - Faça um algoritmo que solicite a nota das 4 provas 
# semestrais do usuário. 
# Em seguida, calcule e envie para a saída padrão a média:

prova1 = float(input("Informe a nota da primeira prova: "))
prova2 = float(input("Informe a nota da segunda prova: "))
prova3 = float(input("Informe a nota da terceira prova: "))
prova4 = float(input("Informe a nota da quarta prova: "))

print((prova1+prova2+prova3+prova4)/4)

# 9 - Faça um algoritmo em que o usuário informe uma medida em metros. 
# Em seguida, converta essa medida para centímetros e envie 
# para a saída padrão:
metros = float(input("Informe uma medida em metros: "))

print(metros, "em centimetros é", metros*100)

#10 - Faça um algoritmo que calcule o cubo e o quadrado de um 
# determinado número:
print("O cubo de 9 é", 9**3, "e o quadrado é", 9**2)

# 11 - Faça um algoritmo que solicite ao usuário digitar 2 números. 
# Em seguida, imprima o total decimal da divisão e o 
# total inteiro (sem casas decimais):
num1 = int(input("Informe um numero: "))
num2 = int(input("Informe outro numero: "))

print("o total decimal da divisão é", num1/num2, "e o total inteiro é", num1//num2)

# 12 - Faça um algoritmo que solicite a largura e a altura de um retângulo. 
# Em seguida, imprima para o usuário quantos metros quadrados possui a 
# área total.
num1 = float(input("Informe a largura do quadrado: "))
num2 = float(input("Informe a altura do quadrado: "))

print("O quadrado possui", num1*num2, "metros quadrados.")

# 13 - Faça um algoritmo que solicite ao usuário informar uma quantidade de dias, 
# horas, minutos e segundos. Em seguida, converta tudo para segundos:

dias = int(input("Informe uma quantidade de dias: "))
horas = int(input("Informe uma quantidade de dias: "))
minutos = int(input("Informe uma quantidade de minutos: "))
segundos = int(input("Informe uma quantidade de segundos: "))

print(dias, "dias", horas,"horas",minutos,"minutos e ",segundos,"segundos", 
"equivale a",(segundos+(minutos*60)+((horas*60)+60)+(((dias*24)*60)*60)),"segundos.")
'''

#14 - Faça um algoritmo que solicite ao usuário informar o valor de uma compra. 
# Em seguida, aplique 10% de desconto e imprima na tela tanto o valor total e 
# também o valor com o desconto aplicado.

compra = float(input("Informe o valor da compra: "))
desconto = compra * 0.1

print("o valor da compra é de ", compra, ", com desconto fica:", compra-desconto)