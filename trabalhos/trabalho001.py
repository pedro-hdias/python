print ("Seja muito bem-vindo!")
nome = str(input("Digite seu nome:"))
idade = int(input("Digite sua idade:"))

if idade >= 18:
    print(f"Legal, {nome}, você é maior de idade. Você tem {idade} anos de idade.")
else: 
    print(f"Ah, {nome}. Você não é maior de idade, você tem apenas {idade} anos.")
