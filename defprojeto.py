import sqlite3

# Função para conectar ao banco de dados
def connect():
    conn = sqlite3.connect('biblioteca.db')
    return conn

#Função para criar as tabelas do banco de dados (se não tiver)
def create_tables():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS livros (\
                id INTEGER PRIMARY KEY,\
                titulo TEXT,\
                autor TEXT,\
                editora TEXT,\
                ano_publicacao INTEGER,\
                isbn TEXT)')

# Criar uma tabela para os usuarios
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (\
                id INTEGER PRIMARY KEY,\
                nome TEXT,\
                sobrenome TEXT,\
                endereco TEXT,\
                email TEXT,\
                telefone TEXT)')

# Criar uma tabela para os emprestimos
    cursor.execute('CREATE TABLE IF NOT EXISTS emprestimos (\
                id INTEGER PRIMARY KEY,\
                id_livro INTEGER,\
                id_usuario INTEGER,\
                data_emprestimo TEXT,\
                data_devolucao TEXT,\
                FOREIGN KEY(id_livro) REFERENCES livros(id),\
                FOREIGN KEY(id_usuario) REFERENCES usuarios(id))')

    conn.commit()
    conn.close()

# Função para inserir um novo livro na tabela "livros"
def insert_book(title, author, publisher, year, isbn):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn) VALUES (?, ?, ?, ?, ?)",
                       (title, author, publisher, year, isbn))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao inserir livro: {e}")
    finally:
        conn.close()

# Função para inserir um novo usuário na tabela "usuarios"
def insert_user(first_name, last_name, address, email, phone):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, sobrenome, endereco, email, telefone) VALUES (?, ?, ?, ?, ?)",
                       (first_name, last_name, address, email, phone))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao inserir usuário: {e}")
    finally:
        conn.close()

# Função para inserir um novo empréstimo na tabela "emprestimos"
def insert_loan(book_id, user_id, loan_date, return_date):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)",
                       (book_id, user_id, loan_date, return_date))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao realizar empréstimo: {e}")
    finally:
        conn.close()

# Função para recuperar todos os livros emprestados no momento
def pegar_livros_emprestados():
    conn = connect()
    try:
        result = conn.execute('''SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, 
                                 emprestimos.data_emprestimo, emprestimos.data_devolucao 
                                 FROM emprestimos
                                 JOIN usuarios ON emprestimos.id = usuarios.id   
                                 JOIN livros ON emprestimos.id_livro = livros.id''').fetchall()
    except sqlite3.Error as e:
        print(f"Erro ao pegar livros emprestados: {e}")
        result = []
    finally:
        conn.close()
    return result


# Função para atualizar a data de devolução de um empréstimo
def update_loan_return_date(loan_id, return_date):
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?",
                       (return_date, loan_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar data de devolução: {e}")
    finally:
        conn.close()

def listar_livros():
    conn = connect()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros")
        livros = cursor.fetchall()
        return livros
    except sqlite3.Error as e:
        print(f"Erro ao listar livros: {e}")
        return []
    finally:
        conn.close()


