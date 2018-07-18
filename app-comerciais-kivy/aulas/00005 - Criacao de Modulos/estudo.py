#coding: utf-8

#módulo estudo
#a = 10
#b = "modulo personalizado"

print("Módulo executado")

#Variaveis que não serão importados com o codigo
# from estudos import *
_a = 10
_b = 20
_c = 30

soma = _a + _b + _c

#define quais variaveis serão copiados ao se utilizar a instrução
# from estudos import *
__all__ = ["aa", "ab"]
aa = 0
ab = 1

ba = 2
bb = 3