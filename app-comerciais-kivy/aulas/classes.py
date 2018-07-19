#coding: utf-8

__author__ = "Lário dos Santos Diniz"

class Estudo1():
    pass

class Pessoa:
    pass

p1 = Pessoa()
p2 = Pessoa()

print(id(p1))
print(id(p2))


class A:

    def __init__(self):
        print(id(self))

a = A()
print(id(a))

