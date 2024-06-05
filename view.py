
import sqlite3

try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('Conexao com o banco de dados realizado com sucesso!')
except sqlite3.Error as e:
    print("Erro ao conectar com o banco de dados:", e)


#Tabela de Cursos ---------------------------

#Criar Cursos ( CREATE C )
def criar_curso(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Cursos (nome, duracao, preco) VALUES (?, ?, ?)"
        cur.execute(query, i)


#criar_curso(['Python', 'Semanas', 50])

# Ver todos os cursos ( READ R ) CRUD
def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Cursos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista


# Atualizar os Cursos ( UPDATE C ) CRUD
def atualizar_cursos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id=?"
        cur.execute(query, i)



#atualizar_cursos(l)

# Deletar os cursos ( Delete D ) CRUD
def deletar_curso(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Cursos WHERE id=?"
        cur.execute(query,i)
        
#deletar_curso([1])

# Tabela de Turmas -----------------------------------

# Criar Turmas ( CREATE C )
def criar_turma(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO turmas (nome, curso_nome, data_inicio) VALUES (?, ?, ?)"
        cur.execute(query, i)

# Ver todas as turmas ( READ R )
def ver_turmas():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM turmas')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

# Atualizar as Turmas ( UPDATE U )
def atualizar_turma(i):
    with con:
        cur = con.cursor()
        query = "UPDATE turmas SET nome=?, curso_nome=?, data_inicio=? WHERE id=?"
        cur.execute(query, i)

# Deletar as Turmas ( DELETE D )
def deletar_turma(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Turmas WHERE id=?"
        cur.execute(query,i)


# Tabela Alunos --------------------------------

#criar Alunos ( CREATE C )
def criar_alunos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Alunos (nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)


# Ver Alunos ( READ R )
def ver_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Alunos")
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

# Atualizar Alunos ( UPDATE U )
def atualizar_alunos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE alunos SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, turma_nome=? WHERE id=?"
        cur.execute(query, i)
    
# Deletar Aluno( DELETE D )
def deletar_aluno(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Alunos WHERE id=?"
        cur.execute(query, i)
        