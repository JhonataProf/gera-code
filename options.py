
from project_factory import make_project_python, make_project_react


def select_project_type(opcao_projeto, diretorio_projetos, dir_novo_projeto):
    if opcao_projeto == 'P':
    ## CRIA UM PROJETO PYTHON
        return make_project_python(diretorio_projetos, dir_novo_projeto)
    elif opcao_projeto == 'N':
        ## CRIA PROJETO REACT
        return make_project_react(diretorio_projetos, dir_novo_projeto)
    else:
        print('Opção inválida!!!!')
        return None