import sqlite3
banco = sqlite3.connect('./bd/banco.db')
cursor = banco.cursor()
idobra = input("Digite ")
consulta = 'SELECT * FROM obra WHERE id=?'
cursor.execute(consulta, (idobra,))

dados_lidos = cursor.fetchall()

endobra = dados_lidos[0][1]

print(endobra)