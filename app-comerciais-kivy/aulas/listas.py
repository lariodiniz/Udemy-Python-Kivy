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