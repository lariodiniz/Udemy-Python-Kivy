#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from kivy.app import App
from kivy.uix.label import Label

def build():
    """    
        return Label(
        text="Curso de Python e Kivy", 
        italic=True,
        font_size=50
        )
    """
    lb = Label()
    lb.text="Curso de Python e Kivy"
    lb.italic=True
    lb.font_size=50
    return lb

app = App()
app.build = build
app.run()