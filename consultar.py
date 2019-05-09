# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('dados.db')

cursor = conn.cursor()

while (True):
    print("-Consultar: Livros- 1: Todos - 2: Por id - 3: Por título - 4: Por autor - 5: Por editora - 0: Sair")
    opcao = int(input(": "))
    
    if (opcao == 0):
        break
    elif (opcao == 1):
        cursor.execute("select * from livros;")
        linhas = cursor.fetchall()
        
        for linha in linhas:
            print(linha)
    elif (opcao == 2):
        id = int(input("Id: "))
        cursor.execute("select * from livros where id == ?", [id])
        result = cursor.fetchone()
        print(result)
    elif (opcao == 3):
        titulo = input("Título: ")
        cursor.execute("select * from livros where titulo like ?", [('%' + titulo + '%')])
        result = cursor.fetchall()
        
        for linha in result:
            print(linha)
    elif (opcao == 4):
        autor = input("Autor: ")
        cursor.execute("select * from livros where titulo like ?", [('%' + autor + '%')])
        result = cursor.fetchall()
        
        for linha in result:
            print(linha)
    elif (opcao == 5):
        editora = input("Editora: ")
        cursor.execute("select * from livros where titulo like ?", [('%' + editora + '%')])
        result = cursor.fetchall()
        
        for linha in result:
            print(linha)
    
    
conn.close()