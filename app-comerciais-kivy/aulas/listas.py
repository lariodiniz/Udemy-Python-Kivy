#uma lista em python é uma estrutura separada com virgulas e delimitado por colchetes
lista = [1,2,8,5,15,3,6,8]

print(lista)
print(lista[0])

l = ['a', 'b', 'c', 'd', 'e']

lista = list("eXcript")
print(lista)

lista = list(("eXcript",))
print(lista)

#uma lista pode conter elementos de tipos diferentes
lista = ['a', 3]

#uma lista pode conter outras listas
lista = [['a','b','c'],[5,8,2],[]]
print(lista[0][1])
print(lista[1][1])

#Função que retorna o tamanho de uma lista
print("o tamanho da lista é ", len(lista))
print("a palavra Teste tem", len("Teste"), "letras.")

#o ultimo elemento de uma lista é sempre acessado com o indice -1
print(lista[0][-1])

#adicionando elementos em uma lista

lista = [1,2,3,4,5]
lista =  lista + [6]
print(lista)
lista = [0] + lista
print(lista)
lista = lista + [7,8,9,10]
print(lista)

#A função append adiciona um elemento no final da lista
lista.append(11)
print(lista)

lista.append([11])
print(lista)

# A função del deleta um elemento de uma lista
del(lista[-1])
print(lista)
#Você pode multiplicar uma lista
lista = 10*[0]
print(lista)

#interando uma lista
lista_nums = [100,200,300,400]
for item in lista_nums:
    print(item)

#utilizando um indice
lista_indice = [0,1,2,3]
for item in lista_indice:
    lista_nums[item] += 1000

print(lista_nums)

lista_nums = [100,200,300,400, 500]

for item in range(len(lista_nums)):
    lista_nums[item] += 1000

print(lista_nums)

#A função enumerate retorna uma lista de tulas que contem um valor inteiro e  cada elemento da lista

l = ['aaa','bbb','ccc','ddd']
print(list(enumerate(l)))

#usando enumerate para o laço

lista_nums = [100,200,300,400, 500]

for indice, item in enumerate(lista_nums):
    lista_nums[indice] += 1000

print(lista_nums)

#fatiando listas
#lista[inicio_da_fatia,final_da_fatia,passo_da_fatia]
lista = "PYTHON"
#invertendo uma lista
print(lista[::-1])

lista = "Bem-vindo ao Curso de Python"
print(lista[10])
print(lista[2])
print(lista[20])
print(lista[:20])
print(lista[10:20])
print(lista[::2])
print(lista[::-1])

#incluindo, alterando e excluindo elementos de uma lista
l = ['aaa','bbb','ccc','ddd']
l.append('eee')
print(l)

l.insert(0,'aaa')
print(l)

l[1] = 'bbbb'
print(l)

l.clear()
print(l)

l = ['aaa','bbb','ccc','ddd']
l.pop()

print(l)

l.pop(0)

print(l)

l = ['aaa','bbb','ccc','ddd', 'eee']

del(l[2:4])
print(l)

l = ['aaa','bbb','ccc','ddd', 'eee']
del(l[::2])
print(l)


lista = ['Claudio', 'Jose','Maria', 'Beltrano', 'João', 'Fulano', 'Ciclano']
print(lista)

#invertendo lista
lista.reverse()
print(lista)
lista.reverse()
print(lista)

#Ordenando Lista acesdente
lista.sort()
print(lista)

#Ordenando Lista descendente
lista.sort(reverse=True)
print(lista)

#Quantidade de elementos em uma lista
lista = ['Claudio', 'Jose','Maria', 'Beltrano', 'João', 'Fulano', 'Ciclano']
print(lista)

print(len(lista))

#verifiando se existe elementos repitidos
lista.insert(5,'Jose')

lista.append('Jose')

print(lista.count('Jose'))
print(lista.count('Maria'))

#Qual o indice de um elemento em uma lista
print(lista.index('Maria'))