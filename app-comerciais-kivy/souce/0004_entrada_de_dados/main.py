#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from kivy.app import App
from kivy.uix.textinput import TextInput

def build():    
    return TextInput(
        text="Componente TextInput"
    )

janela = App()
janela.build = build
janela.run()