import sqlite3

#conecta ao banco, caso o banco não exista cria o mesmo.
conn = sqlite3.connect('bd_estudo.db')

#cria uma consulta
cursor = conn.execute('select * from estados')

#executa uma consulta
rows = cursor.fetchall()

#imprime todas as linhas
for row in rows:
	print(row)
	

