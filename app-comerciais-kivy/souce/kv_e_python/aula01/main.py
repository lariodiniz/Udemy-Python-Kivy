#coding: utf-8

__author__ = "Lário dos Santos Diniz"

import kivy
#define a versão minima da aplicação kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Tela1(BoxLayout):

    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela2())

    def __init__(self, **kwargs):
        super(Tela1, self).__init__(**kwargs)

        self.orientation = "vertical"
        bt1 = Button(text="Clique")
        bt1.on_press = self.on_press_bt
        self.add_widget(bt1)
        self.add_widget(Button(text="bt1"))
        self.add_widget(Button(text="bt2"))

class Tela2(BoxLayout):

    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela1())

    def __init__(self, **kwargs):
        super(Tela2, self).__init__(**kwargs)        

        self.orientation = "vertical"
        bt = Button(text="Clique")
        bt.on_press = self.on_press_bt
        self.add_widget(bt)


class KVvsPy(App):
    def build(self):
        return Tela1()

janela = KVvsPy()
janela.run()