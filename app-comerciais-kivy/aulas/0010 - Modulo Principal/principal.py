#coding: utf-8

#author:Lário dos Santos Diniz

import modulo

if __name__ == "__main__":
    print("A aplicação pode ser inicializada")

#recarregando modulo

import importlib

importlib.reload(modulo)

from pprint import pprint

pprint(modulo.__dict__)