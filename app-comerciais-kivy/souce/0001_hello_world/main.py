#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from kivy.app import App
from kivy.uix.label import Label

class MeuPrograma(App):   

    def build(self):    
        return Label(text = "Hello World")

MeuPrograma().run()

