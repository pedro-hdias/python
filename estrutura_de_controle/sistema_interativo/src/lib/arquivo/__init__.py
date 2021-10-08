from src.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except(FileNotFoundError):
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt')
        a.close()
    except():
        print('Houve um erro ao criar o arquivo!')
    else:
        print(f'arquivo {nome} criado com sucesso.')


