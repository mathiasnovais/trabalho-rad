#criando_banco_de_dados.py
import sqlite3

# CRIANDO CONEXAO
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('Conexão com banco de dados realizada com sucesso!')
except sqlite3.Error as e:
    print("Erro ao conectar com banco de dados:", e)

#criando Tabela de cursos
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS cursos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            duracao TEXT,
            preco REAL                      
        )""" )

        print("Tabela Cursos criado com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar a tabela cursos:", e)

# Criando tabela de turmas
try:
    with con:
        cur = con.cursor()
        con.execute(""" CREATE TABLE IF NOT EXISTS turmas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            curso_nome TEXT,
            data_inicio DATE,
            FOREIGN KEY (cursos_nome) REFERENCES cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE      
        )""")

        print("Tabela Turmas criada com sucesso!")

except sqlite3.Erro as e:
    print("Erro ao criar a tabela turmas: ", e)

# Criando tabela de alunos
try:
    with con:
        cur = con.cursor()
        con.execute(""" CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone TEXT,
            sexo TEXT,
            imagem TEXT,
            data_nascimento DATE,
            cpf TEXT,
            turma_nome TEXT,
            FOREIGN KEY (turma_nome) REFERENCES turmas (nome) ON DELETE CASCADE
        )""")

        print("Tabela Alunos criada com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar a tabela Alunos:", e)
    
