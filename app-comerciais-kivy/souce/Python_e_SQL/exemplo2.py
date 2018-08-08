import sqlite3

path = r'C:\Udemy\Udemy-Python-Kivy\app-comerciais-kivy\souce\Python_e_SQL'
conn = sqlite3.connect(path+r'\teste.db')
conn.close()


