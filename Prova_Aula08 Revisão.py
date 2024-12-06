import os

def listdir():
    itens_diretorio = os.listdir()
    print(itens_diretorio)
    print("Arquivos e pastas no diretório atual:")
    for item in itens_diretorio:
        print(item)
listdir()
