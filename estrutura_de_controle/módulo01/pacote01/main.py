def leiaInt(msg):
	while True:
		try:
			n = int(input(msg))
		except	(ValueError, TypeError):
			print("ERRO: Por favor, digite um número inteiro válido.")
			continue
		except(KeyboardInterrupt):
			print("Usuário decidiu não digitar este número: ")
			break
		else:
			return n

num = leiaInt("Digite um número inteiro: ")
print(f"O valor digitado foi: {num}.")
