# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('dados.db')

cursor = conn.cursor()

print("--------Atualizar: Livros--------")

while True:
    id = int(input("Id: "))
    
    cursor.execute("select * from livros where id == ?", [id])
    
    result = cursor.fetchone()
    
    print(result)
    while True:
        print("Selecione o campo a ser atualizado: - 1: Título - 2: Autor - 3: Ano - 4: Editora - 5: Descrição - 0: Sair")
        op = int(input(": "))
        if(op == 0):
            break;
        elif(op == 1):
            titulo = input("Novo título: ")
            cursor.execute("update livros set titulo = ? where id == ?", [titulo, id])
            conn.commit()
        elif(op == 2):
            autor = input("Novo autor: ")
            cursor.execute("update livros set autor = ? where id == ?", [autor, id])
            conn.commit()
        elif(op == 3):
            ano = int(input("Novo ano: "))
            cursor.execute("update livros set ano = ? where id == ?", [ano, id])
            conn.commit()
        elif (op == 4):
            editora = input("Nova editora: ")
            cursor.execute("update livros set editora = ? where id == ?", [editora, id])
            conn.commit()
        elif (op == 5):
            descricao = input("Nova descricao: ")
            cursor.execute("update livros set descricao = ? where id == ?", [descricao, id])
            conn.commit()
        print("---Dados atualizados---")
    
    
    while True:
        continuar = input("Atualizar outro?(y\\n): ")
        if (continuar in ['Y', 'y', 'N', 'n']):
            break;
            
    if (continuar == 'n' or continuar == 'N'):
        break;

conn.close()