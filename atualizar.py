# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('dados.db')

cursor = conn.cursor()

print("--------Atualizar: Livros--------")

id = int(input("Id: "))

cursor.execute("select * from livros where id == ?", [id])

result = cursor.fetchone()

print(result)
while True:
    op = int(input("Selecione o campo a ser atualizado: - 1: Título - 2: Autor - 3: Ano - 4: Editora - 5: Descrição - 0: Sair"))
    if(op == 0):
        break;
    elif(op == 1):
        titulo = input("Novo título: ")
        cursor.execute("update livros set titulo = ? where id == ?", [titulo, id])
        conn.commit()
    elif(op == 2):
        autor = input("Novo autor: ")
    elif(op == 3):
        ano = int(input("Novo ano: "))


conn.close()