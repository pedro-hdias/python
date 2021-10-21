from  lib.interface import *

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


def lerArquivo(arq):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabecalho('pessoas cadastradas: ')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n ', ' ')
            print(f'Pessoa {dado[0]:<15} idade {dado[1]:>2}.')
    finally:
        a.close()




def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome}; {idade};\n')
        except:
            print('Houve um erro ao escrever os dados.')
        else:
            print(f'Pessoa {nome} adicionada com sucesso')
            a.close()
