

def linha(tam=42):
    return "-" * tam


def cabecalho(txt):
    print(linha(42))
    print(txt.center(42))
    print(linha(42))


def menu(lista):
    cabecalho('Menu principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção')
    return opc

