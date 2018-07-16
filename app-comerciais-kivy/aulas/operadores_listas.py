# verifica se o valor de uma variavel esta em uma lista
x = 'b'

lista = ['a', 'b', 'c']
print(x in lista)

print(2 in (1,2,3,4,5))
print(6 in (1,2,3,4,5))
print(6 not in (1,2,3,4,5))

print(1 in range(1,6))

print( 3 and 5 in range(1,6))

print(((1 and 6) or(5 and 6)) in range(1,6))
print(((1 and 3) or(5 and 6)) in range(1,6))

print((10 or 2) in range(1,6))
print((2  or 10) in range(1,6))