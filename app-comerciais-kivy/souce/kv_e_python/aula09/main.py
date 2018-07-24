# -*- coding: utf-8 -*-

__author__ = "Lário dos Santos Diniz"

import kivy
#define a versão minima da aplicação kivy
kivy.require('1.9.1')

from kivy.app import App

code = """

BoxLayout:
    Button:
        text: "1"
    Button:
        text: "2"
"""

from kivy.lang import Builder

class Estudo6App(App):
    def build(self):
        #para fazer load de um arquivo vc pode usar o Builder.load_file(arquivo) 
        return Builder.load_string(code)

janela = Estudo6App()
janela.run()