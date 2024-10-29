from manager_dir import change_to_dir, create_dir, change_to_user_dir
from execute_bash import abrir_projeto_vscode
from options import select_project_type
from project_factory import make_project_python, make_project_react

diretorio_home = change_to_user_dir()
diretorio_projetos = f'{diretorio_home}/Projetos'
create_dir(diretorio_projetos)
change_to_dir(diretorio_projetos)
dir_novo_projeto = input('Digite o nome do Projeto a ser criado: ')


path_full_novo_projeto = None

while path_full_novo_projeto == None:
    opcao_projeto = input('Qual projeto deseja criar, Python ou Node? \n Digite P para Python \n e N para Node: ')
    path_full_novo_projeto = select_project_type(opcao_projeto, diretorio_projetos, dir_novo_projeto)

## ABRE O PROJETO CRIADO NO VSCODE
abrir_projeto_vscode(path_full_novo_projeto)