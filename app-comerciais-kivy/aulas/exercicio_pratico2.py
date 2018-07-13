#1) Faça um algoritmo que leia um número e mostre se o mesmo é positivo, 
# negativo ou zero.

num = int(input('Digite um número: '))

if (num > 0):
    print("O numero é positivo.")
elif (num < 0):
    print("O numero é negativo.")
else:
    print("O numero é zero.")    

#2) Faça um algoritmo que leia um número e mostre se o mesmo é par ou ímpar.
num = 10

if ((num % 2) == 0):
    print("O numero é par.")
else: 
    print("O numero é impar.")

#3) Faça um algoritmo que leia dois números e imprima o maior.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if (num1 > num2):
    print("O numero %d é o maior." %(num1))
elif (num1 < num2):
    print("O numero %d é o maior." %(num2))
else:
    print("Os numeros são do mesmo tamanho.")

#4) Faça um algoritmo que peça a idade de uma pessoa e imprima na tela se a 
# mesma já é maior de idade ou então, se a mesma é de menor.
idade = int(input('Digite a sua idade: '))

if (idade >= 18):
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

#5) Faça um algoritmo que peça a idade do usuário e a idade da sua mãe. 
# Em seguida, imprima na tela com quantos anos sua mãe o teve.
idade = int(input('Digite a sua idade: '))
idade_mae = int(input('Digite a idade da sua mãe: '))

print("Sua mãe o teve com %d anos" %(idade_mae - idade))

#6) Faça um algoritmo que imprima 50 vezes o caractere "-" na tela 
# (sem a utilização de laços de repetição).
print(50*"-")

#7) Faça um algoritmo que peça um número ao usuário e verifique se o 
# mesmo é par ou então ímpar.
num = int(input('Digite um número: '))

if ((num % 2) == 0):
    print("O numero é par.")
else: 
    print("O numero é impar.")

#8) Faça um algoritmo que peça dois números. Primeiro, imprima o maior e, em seguida, 
# o menor.
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
numeroMaior = num1
numeroMenor = num2
if (num1 < num2):
    numeroMaior = num2
    numeroMenor = num1

print("O numero %d é o maior." %(numeroMaior))
print("O numero %d é o menor." %(numeroMenor))

#9) Faça um algoritmo que verifica se um determinado valor é um número inteiro.
valor = 10
if(type(valor) == int):
    print("É um numero inteiro.")
else:
    print("não é um numero inteiro")

#10) Faça um algoritmo que verifica se um determinado valor é uma String.
valor = '10'
if(type(valor) == str):
    print("É uma string.")
else:
    print("não é uma string")
  
#11) Faça um algoritmo que verifica se um determinado valor é do tipo decimal.
valor = 10.0
if(type(valor) == float):
    print("É do tipo decimal.")
else:
    print("não é do tipo decimal")
#12) Faça um algoritmo que peça um valor numérico. 
# Em seguida, verifique se o número é inteiro ou decimal.

num = input('Digite um número: ')
try:
    num = int(num)
    print('É inteiro')    
    
except:
    try:
        num = float(num)
        print('É decimal')
    except:
        print('É string')

#13) Faça um algoritmo que leia três números e imprima na tela o maior deles.
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))

if ((num1 > num2) and (num1 > num3)):
    print("O numero %d é o maior." %(num1))
elif ((num2 > num1) and (num2 > num3)):
    print("O numero %d é o maior." %(num2))
else:
    print("O numero %d é o maior." %(num3))

#14) Faça um algoritmo que leia três números e imprima-os em ordem crescente.
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
maiorNumero = 0
menorNumero = 0
Numero = 0
if ((num1 > num2) and (num1 > num3)):
    maiorNumero = num1
    if (num2 > num3):
        Numero = num2
        menorNumero = num3
    else:
        menorNumero = num2
        Numero = num3        
elif ((num2 > num1) and (num2 > num3)):
    maiorNumero = num2
    if (num1 > num3):
        Numero = num1
        menorNumero = num3
    else:
        menorNumero = num1
        Numero = num3   
else:
    maiorNumero = num3
    if (num1 > num2):
        Numero = num1
        menorNumero = num2
    else:
        menorNumero = num1
        Numero = num2  
print(maiorNumero, Numero, menorNumero)

#15) Faça um algoritmo que leia um caractere e informe se o mesmo é uma vogal ou não.
caractere = input('Digite um caractere: ')

if ((caractere == 'a') or (caractere == 'e') or (caractere == 'i') or (caractere == 'o') or (caractere == 'u') or
(caractere == 'A') or (caractere == 'E') or (caractere == 'I') or (caractere == 'O') or (caractere == 'U')):
    print("É uma vogal.")
else:
    print("É uma consoante.")
#16) Os endereços IP versão 4 são divididos em cinco classes: A, B, C, D e E. 
# Os endereços no intervalo de 0 à 127 são classe A, de 128 a 191 são classe B, 
# de 192 a 223 são classe C, de 224 à 239 são classe D e a partir de 240 são classe E. 
# Faça um algoritmo que leia o primeiro octeto, 
# no formato decimal de um endereço IP, e informe a sua classe.

ip = "255.168.0.1"
primeiro_octeto = int(ip[0:3])
if (primeiro_octeto > 0 and primeiro_octeto <= 127):
    print("ip da classe A")
elif (primeiro_octeto > 127 and primeiro_octeto <= 191):
    print("ip da classe B")
elif (primeiro_octeto > 191 and primeiro_octeto <= 223):
    print("ip da classe C")
elif (primeiro_octeto > 223 and primeiro_octeto <= 239):
    print("ip da classe D")
elif (primeiro_octeto > 239):
    print("ip da classe E")

#17) Faça um algoritmo que receba um número inteiro, 
# que represente um determinado mês do ano, e mostre o nome do mês correspondente. 
# Por exemplo, se for informado o número 2, o algoritmo deverá exibir: 
# fevereiro. O algoritmo também deve validar se a entrada está correta.
mes = input('Digite um número: ')
try:
    mes = int(mes)

    if (mes == 1):
        print("janeiro")
    elif (mes == 2):
        print("fevereiro")        
    elif (mes == 3):
        print("março")
    elif (mes == 4):
        print("abril")
    elif (mes == 5):
        print("maio")
    elif (mes == 6):
        print("junho")
    elif (mes == 7):
        print("julho")
    elif (mes == 8):
        print("agosto")
    elif (mes == 9):
        print("setembro")
    elif (mes == 10):
        print("outubro")
    elif (mes == 11):
        print("novembro")
    elif (mes == 12):
        print("dezembro")
    else:
        print("Numero Invalido")
except:
    print("Voc~e não informou um numero inteiro.")

#18) Faça um algoritmo que valide uma data. 
# A mesma deve ser formada por dia, mês e ano. Por exemplo, 
# se o usuário digitar a data 10/8 a mesma será inválida. 
# Porém, caso a data seja 01/10/2018, a mesma deve ser considerada válida.
data = input('Digite uma data: ')
if ((len(data) != 10)  or (data[2:3] != '/') or (data[5:6] != '/')):
    print("Data invalida")
else:
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:])

    if ((dia > 31 or dia < 1) or (mes > 12 or mes < 1)):
        print("Data invalida")
    else:
        print("Data valida")
    


