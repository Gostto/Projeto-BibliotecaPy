import sqlite3

# Conectar ao banco de dados ou criar um novo
conn = sqlite3.connect('biblioteca.db')

# Inserir um novo livro
conn.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn) VALUES ('O Senhor dos Aneis', 'J.R.R. Tolkien', 'Editora Martins Fontes', 1954, '9788578270691')"),
conn.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn) VALUES ('Game of Thrones', 'George R. R. Martin', 'Bantam Books', 1996, '9780553381689')"),
conn.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn) VALUES ('O Hobbit', 'J.R.R. Tolkien', 'Evertype', 1937, '9781782010913')"),
conn.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn) VALUES ('Harry Potter e a Pedra Filosofal', 'J. K. Rowling', 'Bloomsbury', 2001, '9789654487658')"),
conn.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn) VALUES ('A Arte da Guerra', 'Sunzi bing fa', 'Barnes & Noble', 1994, '9781566192989')"),

# Selecionar todos os livros
livros = conn.execute("SELECT * FROM livros").fetchall()
print(livros)

# Fechar a conexao com o banco de dados
conn.close()
