#coding: utf-8

__author__ = "Lário dos Santos Diniz"

class Retangulo:

    def __init__(self, largura, altura):
        self.a = altura
        self.l = largura

    def area(self):
        return self.a * self.l

r1 = Retangulo(10, 5)

def func():
    print("teste")

r1.teste = func
r1.teste

print(r1.area())