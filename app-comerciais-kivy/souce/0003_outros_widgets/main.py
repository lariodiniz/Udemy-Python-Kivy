#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from kivy.app import App
from kivy.uix.button import Button

def click():
    print("O botão foi clicado")

def build():
    bt = Button(text="Clique aqui")
    bt.on_press = click
    return bt

janela = App()
janela.build = build
janela.run()