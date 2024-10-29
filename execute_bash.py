import subprocess

def atualizar_linux():
    subprocess.run(f'''sudo apt update -y && sudo apt-get upgrade -y''', shell=True, check=True, executable='/bin/bash')
    
def instalar_pip():
    subprocess.run(f'''sudo apt install python3-pip''', shell=True, check=True, executable='/bin/bash')
    
def criar_venv():
    subprocess.run(f'''sudo apt install python3-venv''', shell=True, check=True, executable='/bin/bash')
    subprocess.run(f'''python3 -m venv .venv''', shell=True, check=True, executable='/bin/bash')
    subprocess.run(f'''source .venv/bin/activate''', shell=True, check=True, executable='/bin/bash')
    
def abrir_projeto_vscode(path_full_novo_projeto):
    subprocess.run(f'''code {path_full_novo_projeto}''', shell=True, check=True, executable='/bin/bash')
    
def instalar_tkinter():
    subprocess.run(f'''sudo apt-get install python3-tk -y''', shell=True, check=True, executable='/bin/bash')
    
def instala_node_20():
    subprocess.run(f'''curl -sL https://deb.nodesource.com/setup_20.x -o /tmp/nodesource_setup.sh''', shell=True, check=True, executable='/bin/bash')
    subprocess.run(f'''sudo bash /tmp/nodesource_setup.sh''', shell=True, check=True, executable='/bin/bash')
    subprocess.run(f'''sudo apt install nodejs -y''', shell=True, check=True, executable='/bin/bash')
    
def cria_projeto_react(dir_novo_projeto):
    # CRIA UM PROJETO EM REACT
    subprocess.run(f'''npx create-react-app {dir_novo_projeto} --template typescript''', shell=True, check=True, executable='/bin/bash')