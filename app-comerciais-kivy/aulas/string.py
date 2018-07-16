#Para o python toda string é uma lista de caracteres imutavel.

s = "Para o python toda string é uma lista imutavel."

#primeiro caractere de uma string
print(s[0])

#ultimo caractere de uma string
print(s[-1])

#parte de uma string
print(s[5:10])

print(s[5:])

#reverter uma string
print(s[::-1])

#mostrar de dois em dois caracteres
print(s[::2])

#verificar qual caracter é de um código da tabela asci
print(chr(100))

#verifica qual é o código da tabela asci referente a um caracter
print(ord('d'))

#dividindo uma string
print(s.split(" "))

s = "Para o python toda string é uma lista imutavel."
#substitui caracteres
print(s.replace("lista", ""))
print(s)



#laço
s = "interando Strings"

for c in s:
    print(c)

indice = 0
while indice < len(s):
    print(indice, s[indice])
    indice += 1


for k, v in enumerate("interando Strings"):
    print(k, v)
