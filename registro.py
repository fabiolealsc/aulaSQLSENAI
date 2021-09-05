import sqlite3
from typing import Literal

conn = sqlite3.connect('bankRegister.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS dadosBanc (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, sobrenome text, idade INTEGER, saldo FLOAT)')



while True:


    nome = str(input('Digite o nome: '))
    sobrenome = str(input('Digite o sobrenome: '))
    idade = str(input('Digite a idade: '))
    saldo = str(input('Digite o saldo: '))
    
    cursor.execute('INSERT INTO dadosBanc VALUES("'+nome+'","'+sobrenome+'", "'+idade+'", "'+saldo+'")')


    
