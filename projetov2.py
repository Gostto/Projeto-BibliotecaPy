import sqlite3 
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog 
from defprojeto import * # import das funções
# from PIL import Image, ImageTk # biblioteca de import de imagens

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

# Criação da tabela para os usuarios
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (\
                id INTEGER PRIMARY KEY,\
                nome TEXT,\
                sobrenome TEXT,\
                endereco TEXT,\
                email TEXT,\
                telefone TEXT)')

# Criação da tabela para os emprestimos
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

#Janela principal
janela = tk.Tk()
janela.title("Sistema de Biblioteca")
janela.configure(bg="red")
janela.geometry("350x400")
janela.grid_columnconfigure(0,weight=1) #Centralizado 
janela.grid_rowconfigure(0, weight=1)

frames = {}
def show_frame(frame):
    frame.tkraise()

#Geração de cada frame
for frame_name in ("main_menu", "inserir_livro", "inserir_usuario", "realizar_emprestimo", "atualizar_devolucao", "livros_emprestados", "listar_livros"):
    frame = tk.Frame(janela)
    #frame = tk.Frame(janela, bg="#deb0f5")
    frame.grid(row=0, column=0, sticky="nsew")
    frames[frame_name] = frame


#Função para criar o menu principal
def criar_menu_principal(frame):
    # Carregar a imagem do livro
    # img = Image.open("ProjetoBiblioteca/livro2.png")
    # img = img.resize((50, 50))  # Redimensionar conforme necessário
    # photo = ImageTk.PhotoImage(img)
    
    # Adicionar a imagem no topo do frame
    # img_label = tk.Label(frame, image=photo, bg="#deb0f5")
    # img_label.image = photo  # Manter uma referência para a imagem
    # img_label.pack(pady=10)

    tk.Label(frame, text="Bem-vindo(a) à Biblioteca").pack(pady=10)
    tk.Label(frame, text="Selecione uma opção:").pack(pady=10)
    tk.Button(frame, text="Inserir um novo livro", command=lambda: show_frame(frames["inserir_livro"]), bg="blue", fg="white").pack(pady=5)
    tk.Button(frame, text="Inserir um novo usuário", command=lambda: show_frame(frames["inserir_usuario"]), bg="green", fg="white").pack(pady=5)
    tk.Button(frame, text="Realizar um empréstimo", command=lambda: show_frame(frames["realizar_emprestimo"]), bg="purple", fg="white").pack(pady=5)
    tk.Button(frame, text="Atualizar a data de devolução", command=lambda: show_frame(frames["atualizar_devolucao"]), bg="orange", fg="white").pack(pady=5)
    tk.Button(frame, text="Exibir livros emprestados", command=lambda: show_frame(frames["livros_emprestados"]), bg="brown", fg="white").pack(pady=5)
    tk.Button(frame, text="Listar todos os livros", command=lambda: show_frame(frames["listar_livros"]), bg="black", fg="white").pack(pady=5)
    tk.Button(frame, text="Sair", command=janela.quit, bg="gray", fg="white").pack(pady=5)


# Criar as funções para cada funcionalidade
def criar_frame_inserir_livro(frame):
    tk.Label(frame, text="Inserir Livro").pack(pady=10)

    tk.Label(frame, text="Título").pack()
    title_entry = tk.Entry(frame)
    title_entry.pack()

    tk.Label(frame, text="Autor").pack()
    author_entry = tk.Entry(frame)
    author_entry.pack()

    tk.Label(frame, text="Editora").pack()
    publisher_entry = tk.Entry(frame)
    publisher_entry.pack()

    tk.Label(frame, text="Ano de Publicação").pack()
    year_entry = tk.Entry(frame)
    year_entry.pack()

    tk.Label(frame, text="ISBN").pack()
    isbn_entry = tk.Entry(frame)
    isbn_entry.pack()

    def submit():
        title = title_entry.get()
        author = author_entry.get()
        publisher = publisher_entry.get()
        year = year_entry.get()
        isbn = isbn_entry.get()
        insert_book(title, author, publisher, year, isbn)
        messagebox.showinfo("Sucesso", "Livro inserido com sucesso!")
        show_frame(frames["main_menu"])

    tk.Button(frame, text="Inserir", command=submit).pack(pady=10)
    tk.Button(frame, text="Voltar", command=lambda: show_frame(frames["main_menu"])).pack(pady=5)

def criar_frame_inserir_usuario(frame):
    tk.Label(frame, text="Inserir Usuário").pack(pady=10)

    tk.Label(frame, text="Primeiro Nome").pack()
    first_name_entry = tk.Entry(frame)
    first_name_entry.pack()

    tk.Label(frame, text="Sobrenome").pack()
    last_name_entry = tk.Entry(frame)
    last_name_entry.pack()

    tk.Label(frame, text="Endereço").pack()
    address_entry = tk.Entry(frame)
    address_entry.pack()

    tk.Label(frame, text="E-mail").pack()
    email_entry = tk.Entry(frame)
    email_entry.pack()

    tk.Label(frame, text="Telefone").pack()
    phone_entry = tk.Entry(frame)
    phone_entry.pack()

    def submit():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        address = address_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        insert_user(first_name, last_name, address, email, phone)
        messagebox.showinfo("Sucesso", "Usuário inserido com sucesso!")
        show_frame(frames["main_menu"])

    tk.Button(frame, text="Inserir", command=submit).pack(pady=10)
    tk.Button(frame, text="Voltar", command=lambda: show_frame(frames["main_menu"])).pack(pady=5)

def criar_frame_realizar_emprestimo(frame):
    tk.Label(frame, text="Realizar Empréstimo").pack(pady=10)

    tk.Label(frame, text="ID do Livro").pack()
    user_id_entry = tk.Entry(frame)
    user_id_entry.pack()

    tk.Label(frame, text="ID do Usuário").pack()
    book_id_entry = tk.Entry(frame)
    book_id_entry.pack()

    tk.Label(frame, text="Data de Emprestimo (DD-MM-AAAA)").pack()
    loan_date_entry = tk.Entry(frame)
    loan_date_entry.pack()

    tk.Label(frame, text="Data de Devolução (DD-MM-AAAA)").pack()
    return_date_entry = tk.Entry(frame)
    return_date_entry.pack()

    def submit():
        user_id = user_id_entry.get()
        book_id = book_id_entry.get()
        loan_date = loan_date_entry.get()
        return_date = return_date_entry.get()
        insert_loan(user_id, book_id, loan_date, return_date)
        messagebox.showinfo("Sucesso", "Empréstimo realizado com sucesso!")
        show_frame(frames["main_menu"])

    tk.Button(frame, text="Realizar", command=submit).pack(pady=10)
    tk.Button(frame, text="Voltar", command=lambda: show_frame(frames["main_menu"])).pack(pady=5)

def criar_frame_atualizar_devolucao(frame):
    tk.Label(frame, text="Atualizar Data de Devolução").pack(pady=10)

    tk.Label(frame, text="ID do Empréstimo").pack()
    loan_id_entry = tk.Entry(frame)
    loan_id_entry.pack()

    tk.Label(frame, text="Nova Data de Devolução (AAAA-MM-DD)").pack()
    return_date_entry = tk.Entry(frame)
    return_date_entry.pack()

    def submit():
        loan_id = loan_id_entry.get()
        return_date = return_date_entry.get()
        update_loan_return_date(loan_id, return_date)
        messagebox.showinfo("Sucesso", "Data de devolução atualizada com sucesso!")
        show_frame(frames["main_menu"])

    tk.Button(frame, text="Atualizar", command=submit).pack(pady=10)
    tk.Button(frame, text="Voltar", command=lambda: show_frame(frames["main_menu"])).pack(pady=5)

def atualizar_frame_livros_emprestados(frame):
    for widget in frame.winfo_children():
        widget.destroy()  # Limpa todos os widgets do frame para evitar duplicação

    tk.Label(frame, text="Livros Emprestados").pack(pady=10)
    livros_emprestados = pegar_livros_emprestados()

    if not livros_emprestados:
        tk.Label(frame, text="Nenhum livro emprestado no momento.").pack(pady=10)
    else:
        output = ""
        for dados in livros_emprestados:
            output += f"Título: {dados[0]}\nCliente: {dados[1]} {dados[2]}\nData do empréstimo: {dados[3]}\nData da devolução: {dados[4]}\n\n"

        text_widget = tk.Text(frame, wrap=tk.WORD, height=15, width=50)
        text_widget.pack(pady=10)
        text_widget.insert(tk.END, output)
        text_widget.config(state=tk.DISABLED)

    tk.Button(frame, text="Atualizar", command=lambda: atualizar_frame_livros_emprestados(frame)).pack(pady=5)
    tk.Button(frame, text="Voltar", command=lambda: show_frame(frames["main_menu"])).pack(pady=5)

def criar_frame_livros_emprestados(frame):
    atualizar_frame_livros_emprestados(frame)

def criar_frame_listar_livros(frame):
    for widget in frame.winfo_children():
        widget.destroy()  # Limpa todos os widgets do frame para evitar duplicação

    tk.Label(frame, text="Lista de Livros").pack(pady=10)
    livros = listar_livros()  # Função para buscar todos os livros

    if not livros:
        tk.Label(frame, text="Nenhum livro cadastrado.").pack(pady=10)
    else:
        output = ""
        for livro in livros:
            output += f"ID{livro[0]} - Título: {livro[1]}\nAutor: {livro[2]}\nEditora: {livro[3]}\nAno de Publicação: {livro[4]}\nISBN: {livro[5]}\n\n"

        text_widget = tk.Text(frame, wrap=tk.WORD, height=15, width=50)
        text_widget.pack(pady=10)
        text_widget.insert(tk.END, output)
        text_widget.config(state=tk.DISABLED)

    tk.Button(frame, text="Voltar", command=lambda: show_frame(frames["main_menu"])).pack(pady=5)



# Inicializar todos os frames
criar_menu_principal(frames["main_menu"])
criar_frame_inserir_livro(frames["inserir_livro"])
criar_frame_inserir_usuario(frames["inserir_usuario"])
criar_frame_realizar_emprestimo(frames["realizar_emprestimo"])
criar_frame_atualizar_devolucao(frames["atualizar_devolucao"])
criar_frame_livros_emprestados(frames["livros_emprestados"])
criar_frame_listar_livros(frames["listar_livros"])

# Mostrar o menu principal
show_frame(frames["main_menu"])

janela.mainloop()


