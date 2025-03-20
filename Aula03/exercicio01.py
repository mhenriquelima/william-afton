nome = input('nome > ')
idade = input('idade > ')
if idade.isdigit() and int(idade) < 100: 
    print(f'olá, {nome}! Você tem {idade} anos.')
else:
    print(f'insira uma idade valida, {nome}')