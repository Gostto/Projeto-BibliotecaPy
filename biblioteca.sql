--
-- File generated with SQLiteStudio v3.4.4 on qui mai 23 15:23:45 2024
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: emprestimos
CREATE TABLE IF NOT EXISTS emprestimos (                id INTEGER PRIMARY KEY,                id_livro INTEGER,                id_usuario INTEGER,                data_emprestimo TEXT,                data_devolucao TEXT,                FOREIGN KEY(id_livro) REFERENCES livros(id),                FOREIGN KEY(id_usuario) REFERENCES usuarios(id));
INSERT INTO emprestimos (id, id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (1, 1, 1, '12-05-2024', '22-05-2024');
INSERT INTO emprestimos (id, id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (2, 2, 2, '05-05-2024', '02-06-2024');
INSERT INTO emprestimos (id, id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (3, 3, 3, '15-06-2024', '20-06-2024');
INSERT INTO emprestimos (id, id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (4, 4, 4, '05-06-2014', '25-02-2025');

-- Table: livros
CREATE TABLE IF NOT EXISTS livros (                id INTEGER PRIMARY KEY,                titulo TEXT,                autor TEXT,                editora TEXT,                ano_publicacao INTEGER,                isbn TEXT);
INSERT INTO livros (id, titulo, autor, editora, ano_publicacao, isbn) VALUES (1, 'O Senhor dos Aneis', 'J.R.R. Tolkien', 'Editora Martins Fontes', 1954, '9788578270691');
INSERT INTO livros (id, titulo, autor, editora, ano_publicacao, isbn) VALUES (2, 'O Hobbit', 'J.R.R. Tolkien', 'Evertype', 1937, '9781782010913');
INSERT INTO livros (id, titulo, autor, editora, ano_publicacao, isbn) VALUES (3, 'Harry Potter e a Pedra Filosofal', 'J. K. Rowling', 'Bloomsbury', 2001, '9789654487658');
INSERT INTO livros (id, titulo, autor, editora, ano_publicacao, isbn) VALUES (4, 'A Arte da Guerra', 'Sunzi bing fa', 'Barnes & Noble', 1994, '9781566192989');
INSERT INTO livros (id, titulo, autor, editora, ano_publicacao, isbn) VALUES (10, 'O Pequeno Princípe', 'Matheus Ronaldo', 'Globo', 1996, '1231243124');

-- Table: usuarios
CREATE TABLE IF NOT EXISTS usuarios (                id INTEGER PRIMARY KEY,                nome TEXT,                sobrenome TEXT,                endereco TEXT,                email TEXT,                telefone TEXT);
INSERT INTO usuarios (id, nome, sobrenome, endereco, email, telefone) VALUES (1, 'Gustavo', 'Carvalho', 'Rua das Bolinhas, 123', 'gustavocarvalho123@gmail.com', '(21) 96485-0884');
INSERT INTO usuarios (id, nome, sobrenome, endereco, email, telefone) VALUES (2, 'Roberto', 'Afonso', 'Rua das Lagoas, 456', 'robertoafonso@gmail.com', '(22) 95643-5744');
INSERT INTO usuarios (id, nome, sobrenome, endereco, email, telefone) VALUES (3, 'Ronaldo', 'Nobre', 'Rua do Palacio, 756', 'nobre@gmail.com', '(21) 3123-4151');
INSERT INTO usuarios (id, nome, sobrenome, endereco, email, telefone) VALUES (4, 'Isabela', 'Souza', 'Rua das Flores, 134', 'isabela@gmail.com', '(21) 3233-4121');
INSERT INTO usuarios (id, nome, sobrenome, endereco, email, telefone) VALUES (5, 'Laura', 'Morais', 'Rua Girassol, 56', 'laura@gmail.com', '(21) 3412-4145');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
