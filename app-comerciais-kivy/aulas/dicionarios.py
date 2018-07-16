#Um dicionario é uma lista não ordenada especealizada onde cada elemento esta associado a uma chave
print(type({}))

d1 = {}
print(type(d1))

d1['aaa'] = 1000
print(d1)

d2 = {1.1: "teste1", 2.2:"teste2", 3: "teste3"}
print(d2)

print(d2[1.1])

#Funções de Dicionario

tel = {
    30301122: "Pericles",
    33547877: "Menelau",
    33381245: "Atreu",
    36458899: "Tieste"
}

print(tel)

#quantidade de elementos
len(tel)

#remover um elemento
del(tel[36458899])

#lista de chaves
tel.keys()

#lista de valores
tel.values()

#retornar um valor
tel.get(30301122)

#remove e retorna um elemento
tel.popitem()

#verifica se uma chave existe
33547877 in tel

#mescla dois dicionarios
tel.update({
    99999999: "teste1",
    55551111: "teste2"
})