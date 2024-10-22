from pathlib import Path
import os

def change_to_user_dir():
    diretorio_home = Path.home()
    # ENTRAR NA PASTA DE USUÁRIO
    os.chdir(diretorio_home)
    return diretorio_home
    
def create_dir(dirname:str):
    if os.path.exists(dirname) == False:
        os.mkdir(dirname)
        
def change_to_dir(dir_path:str):
    os.chdir(dir_path)
    
def create_file(path_file, file_name):
    if os.path.isfile(f'{path_file}/{file_name}') == False:
        os.mknod(file_name)