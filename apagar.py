# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('dados.db')

cursor = conn.cursor()

print("--------Apagar: Livros--------")

id = int(input("Id: "))

cursor.execute("select * from livros where id == ?", [id])

result = cursor.fetchone()

print(result)
while True:
    op = input("Confirmar remoção desses dados?(y\\n)")
    if (op in ['y', 'Y', 'n', 'N']):
        break

if(op == 'y' or op == 'Y'):
    cursor.execute("delete from livros where id  == ?", [id]);
    conn.commit()
    print("---Dados apagados---")



conn.close()