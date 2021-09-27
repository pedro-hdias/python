def leiaFloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except(ValueError, TypeError):
            print("ERRO: Por favor, digite um número flutuante válido.")
            continue
        except(KeyboardInterrupt):
            print("Usuário decidiu não digitar este número: ")
            break
        else:
            return n2