from  lib.interface import *

while True:
    resposta = menu(['criar usuário', 'listar usuários', 'sair do sistema'])
    if resposta == 1:
        cabecalho("Cadastrar usuário:")
    elif resposta == 2:
        cabecalho("Ver usuários cadastrados")
    elif resposta == 3:
        cabecalho("Saindo do sistema, até logo!")
        break
    else:
        print("Você digitou um valor errado, por favor digite uma opção válida.")


