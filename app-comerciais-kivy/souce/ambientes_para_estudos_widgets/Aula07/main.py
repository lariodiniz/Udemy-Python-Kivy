 #coding: utf-8
#author: Lário dos Santos Diniz
__author__ = "Lário dos Santos Diniz"

from kivy.app import App
from kivy.lang import Builder

from kivy.core.window import Window

#Window.clearcolor = [1,1,1,1]

#usando hexadecimal
from kivy.utils import get_color_from_hex
Window.clearcolor = get_color_from_hex("#FFFFFF")

import kivy
#define a versão minima da aplicação kivy
kivy.require('1.9.1')

kvcode = """
#:import C kivy.utils.get_color_from_hex
<FVerde@FloatLayout>:
    size_hint: .3, .3

    canvas.before:
        Color:
            rgba: C("#22FFAA")
        Rectangle:
            pos: self.pos
            size: self.size
FloatLayout:
    FVerde:
        pos_hint:{"x": .4, "y": .4}
"""

#Builder.load_string(kvcode)

class JanelaApp(App):
    def build(self):
        return Builder.load_string(kvcode)
    
janela = JanelaApp()
janela.run()