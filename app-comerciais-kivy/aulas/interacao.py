# -*- coding: utf-8

#Enquanto
"""
x = 0
while( x <= 10):
    print(x)
    x += 1

#Enquanto com Else
x = 0
print("while")
while(x<10):
    print(x)
    x+= 1
else:
    print("else")
print("fim")

#Laço For

#For em python sempre trabalha com lista
for c in "python":
    print(c)

#range
range(0,10,2) # devolve um objeto do tipo range, para ter o objeto em tipo list precisa-se converter
#Você pode passar somente o ultimo elemento do intervalo na função range
range(10)
#o range pode retornar uma lista descendo ou negativa
range(100,0,-3)
range(-100,0-3)

#for com range
for i in range(10):
    print(i)

#for com range negativo
for i in range(-10,0,1):
    print(i)


#Instrução break. Pode ser usado com for e com while
print("Antes de entrar no laço")

for item in range(10):
    print(item)
    if(item==6):
        print("A condição estabelecida retornou true")
        break
print("depois de entrado no laço")
"""
#instrução continue. pode ser usado com for e com while. ela finaliza um unico ciclo
print()
print("inicio")
i = 0
while(i<10):
    i+=1
    if (i%2==0):
        continue
    if(i>5):
        break #break não executa o else.
    print(i)
else:
    print("else")
print("fim")