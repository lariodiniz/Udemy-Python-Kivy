#coding: utf-8
#author: Lário dos Santos Diniz
__author__ = "Lário dos Santos Diniz"

import kivy
#define a versão minima da aplicação kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.button import Button

from kivy.core.window import Window

#Window.clearcolor = [1,1,1,1]

#usando hexadecimal
from kivy.utils import get_color_from_hex
Window.clearcolor = get_color_from_hex("#FFFFFF")

class JanelaApp(App):
    def build(self):
        return Button(
            text="Funcionou :D",
            size_hint=(.2,.2),
            pos_hint={"center_x": .5, "center_y": .5}
        )
    
if __name__ == '__main__':
    janela = JanelaApp()
    janela.run()