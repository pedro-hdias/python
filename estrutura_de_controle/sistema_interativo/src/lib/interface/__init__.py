
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(TypeError, ValueError):
            print("ERRO: Por favor digite um número inteiro válido!")
            continue
        except(KeyboardInterrupt):
            print("O usuário preferiu não digitar este valor.")
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha(42))
    print(txt.center(42))
    print(linha(42))


def menu(lista):
    cabecalho('Menu principal')
    c = 1
    for iten in lista:
        print(f"{c} - {iten}")
        c += 1
    print(linha(42))
    opc = leiaInt("Digite sua opção: ")
    return opc

