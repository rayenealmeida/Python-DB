import sqlite3
from pathlib import Path 

ROOT_PATH =Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()

def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, Nome VARCHAR(100), email VARCHAR(150))"
    )
    conexao.commit()

# Inserir Registro
def inserir_registro(conexao, cursor, Nome, email):
    data = ("Maria", "maria@gmail.com")
    cursor.execute("INSERT INTO clientes(nome, email) VALUES(?,?);", data)
    conexao.commit()

# Atualizar Registro
def atualizar_registro(conexao, cursor, Nome, email, id):
    data = (Nome, email, id)
    cursor.execute("UPDATE clientes SET Nome=?, email=? WHERE id=?;", data)
    conexao.commit()

atualizar_registro(conexao, cursor, 'Joana Domingos', 'jomingos@gmail.com', 5)

# Remover Registro
def remover_registro(conexao, cursor, Nome, email, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()

remover_registro(conexao, cursor, 7)