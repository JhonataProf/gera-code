from manager_dir import change_to_dir, create_dir, create_file, change_to_user_dir
from execute_bash import atualizar_linux, instalar_pip, criar_venv, abrir_projeto_vscode, instalar_tkinter

diretorio_home = change_to_user_dir()
diretorio_projetos = f'{diretorio_home}/Projetos'
create_dir(diretorio_projetos)
change_to_dir(diretorio_projetos)
dir_novo_projeto = input('Digite o nome do Projeto a ser criado: ')
has_tkinter = input('Deseja instalar o Tkinter: \n Digite s ou sim para confirmar: ')
path_full_novo_projeto = f'{diretorio_projetos}/{dir_novo_projeto}'
create_dir(path_full_novo_projeto)
change_to_dir(path_full_novo_projeto)
create_file(path_full_novo_projeto, "main.py")
print(f'{path_full_novo_projeto}/main.py')
atualizar_linux()
instalar_pip()
criar_venv()
if has_tkinter == 's' or has_tkinter == 'sim':
    instalar_tkinter()
else:
    print("Projeto sem a biblioteca do TKinter")
abrir_projeto_vscode(path_full_novo_projeto)