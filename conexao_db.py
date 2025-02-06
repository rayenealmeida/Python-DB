import sqlite3
from pathlib import Path 

ROOT_PATH =Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, Nome VARCHAR(100), email VARCHAR(150))')

data = ("Joana", "jota@gmail.com")
cursor.execute("DELETE INTO clientes(nome, email) VALUES(?,?);", data)
conexao.commit()