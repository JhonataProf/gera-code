import tkinter as tk
from tkinter import ttk
from execute_bash import abrir_projeto_vscode
from subprocess import Popen, PIPE
from handlers import validate_input, save_data

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("App Gera Code")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Digite o nome do projeto sem espaços e acentuação:")
        self.label.pack(pady=5)
        
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        self.label_language = tk.Label(self.root, text="Selecione uma linguagem:")
        self.label_language.pack(pady=5)

        self.combo = ttk.Combobox(self.root, values=["Python", "NodeJS"])
        self.combo.pack(pady=5)

        self.submit_button = tk.Button(self.root, text="Enviar", command=self.submit)
        self.submit_button.pack(pady=5)

        self.save_button = tk.Button(self.root, text="Salvar", command=self.save)
        self.save_button.pack(pady=20)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=5)
        
        self.bash_output = tk.Text(self.root, height=10, width=80)
        self.bash_output.pack(pady=5)

    def submit(self):
        name = self.entry.get()
        language = self.combo.get()

        if validate_input(name):
            self.result_label.config(text=f"Nome: {name}, Linguagem: {language}")
        else:
            self.result_label.config(text="Erro: Nome inválido")

    def save(self):
        name = self.entry.get()
        language = self.combo.get()
        if validate_input(name):
            self.run_bash("sudo apt-get update -y && sudo apt-get upgrade -y")
            path_full_novo_projeto = save_data(name, language)
            message = f'Projeto Criado na pasta {path_full_novo_projeto}'
            self.result_label.config(text=message)
            abrir_projeto_vscode(path_full_novo_projeto)
        else:
            self.result_label.config(text="Erro: Nome inválido")
            
    def run_bash(self, command):
        process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE) 
        stdout, stderr = process.communicate() 
        self.bash_output.delete(1.0, tk.END) 
        self.bash_output.insert(tk.END, stdout.decode()) 
        if stderr: 
            self.bash_output.insert(tk.END, stderr.decode())

    def run(self):
        self.root.mainloop()
