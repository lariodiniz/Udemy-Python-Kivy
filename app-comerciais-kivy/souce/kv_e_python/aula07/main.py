# -*- coding: utf-8 -*-

__author__ = "Lário dos Santos Diniz"

import kivy
#define a versão minima da aplicação kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MinhaTela(BoxLayout):

    def click(self):
        self.ids.lb1.text = ""
        self.ids.lb2.text = "10"

class Estudo4App(App):
    pass
    
janela = Estudo4App()
janela.run()