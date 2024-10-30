from manager_dir import change_to_dir, create_dir, change_to_user_dir
from execute_bash import abrir_projeto_vscode
from options import select_project_type
from project_factory import make_project_python, make_project_react

def validate_input(name):
    return name.isalnum()

def save_data(dir_novo_projeto, opcao_projeto):
    diretorio_projetos = init_criar_projeto()
    return select_project_type(opcao_projeto, diretorio_projetos, dir_novo_projeto)

def init_criar_projeto():
    diretorio_home = change_to_user_dir()
    diretorio_projetos = f'{diretorio_home}/Projetos'
    create_dir(diretorio_projetos)
    change_to_dir(diretorio_projetos)
    return diretorio_projetos