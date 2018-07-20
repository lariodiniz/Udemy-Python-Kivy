#coding: utf-8

__author__ = "Lário dos Santos Diniz"

class Retangulo:
    """Classe com as Regras que definem um retangulo"""

    def __init__(self, largura, altura):
        self._altura = 0
        self._largura = 0
        self.altura = altura
        self.largura = largura

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, num):
        if( not (isinstance(num, int) and (num > 0))):
            raise ValueError("Altura é inválida: {}".format(num))

        self._altura = num

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, num):

        if( not (isinstance(num, int) and (num > 0))):
            raise ValueError("Largura é inválida: {}".format(num))
                        
        self._largura = num

    @property
    def area(self):
        return self._altura * self._largura

r = Retangulo(largura=5, altura=5)

print(r.area)

class A:
    def __init__(self):
        self._var = 0
    
    def _get_var(self):
        return self._var

    def _set_var(self, x):
        self._var = x

    #Criando propriedade
    #var = property(fget=_get_var, fset=_set_var)
    @property
    def var(self):
        return self._var

    @var.setter
    def var(self, x):
        self._var = x

a = A()
a.var = 10

print(a.var)