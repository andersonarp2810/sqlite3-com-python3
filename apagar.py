# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('dados.db')

cursor = conn.cursor()

print("--------Apagar: Livros--------")

while True:
    id = int(input("Id: "))
    
    cursor.execute("select * from livros where id == ?", [id])
    
    result = cursor.fetchone()
    
    print(result)
    while True:
        op = input("Confirmar remoção desses dados?(y\\n): ")
        if (op in ['y', 'Y', 'n', 'N']):
            break
    
    if(op == 'y' or op == 'Y'):
        cursor.execute("delete from livros where id  == ?", [id]);
        conn.commit()
        print("---Dados apagados---")
    
    while True:
            continuar = input("Apagar outro?(y\\n): ")
            if (continuar in ['Y', 'y', 'N', 'n']):
                break;
                
    if (continuar == 'n' or continuar == 'N'):
        break;

conn.close()