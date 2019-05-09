# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('dados.db')

cursor = conn.cursor()

while True:
    print("--------Inserir dados: Livros--------")
    
    titulo = input("Título: ")
    
    autor = input("Autor: ")
    
    ano = int(input("Ano: "))
    
    editora = input("Editora: ")
    
    descricao = input("Descrição: ")
    
    cursor.execute("insert into livros (titulo, autor, ano, editora, descricao) values (?, ?, ?, ?, ?);", [titulo, autor, ano, editora, descricao])
    
    conn.commit()
    
    print("--------Dados inseridos--------")
    while True:
        op = input("Inserir novamente?(y\\n): ")
        if (op in ['y', 'Y', 'n', 'N']):
            break;
    if (op == "n" or op == "N"):
        break;

conn.close