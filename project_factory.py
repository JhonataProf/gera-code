from manager_dir import change_to_dir, change_to_user_dir, create_dir, create_file
from execute_bash import atualizar_linux, cria_projeto_react, instala_node_20, instalar_pip, criar_venv, abrir_projeto_vscode, instalar_tkinter

def make_project_python(diretorio_projetos, dir_novo_projeto):
    has_tkinter = input('Deseja instalar o Tkinter: \n Digite s ou sim para confirmar: ')
    path_full_novo_projeto = f'{diretorio_projetos}/{dir_novo_projeto}'
    create_dir(path_full_novo_projeto)
    change_to_dir(path_full_novo_projeto)
    create_file(path_full_novo_projeto, "main.py")
    print(f'{path_full_novo_projeto}/main.py')
    # atualizar_linux()
    instalar_pip()
    criar_venv()
    if has_tkinter == 's' or has_tkinter == 'sim':
        instalar_tkinter()
    else:
        print("Projeto sem a biblioteca do TKinter")
        
    return path_full_novo_projeto

def make_project_react(diretorio_projetos, dir_novo_projeto):
    # atualizar_linux()
    path_full_novo_projeto = f'{diretorio_projetos}/{dir_novo_projeto}'
    diretorio_home = change_to_user_dir()
    print(f'Você está na pasta: {diretorio_home}')
    # INSTALA O NODEJS V20
    instala_node_20()

    change_to_dir(diretorio_projetos)
    cria_projeto_react(dir_novo_projeto)
    return path_full_novo_projeto