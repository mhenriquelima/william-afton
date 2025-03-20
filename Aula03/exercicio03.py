ano_de_nascimento = input('em que ano vc nasceu > ')
fez_aniversário = input('ja fez aniversário (y/n)> ')

if fez_aniversário == 'y':
    fez_aniversário = True
elif fez_aniversário == 'n':
    fez_aniversário = False

if ano_de_nascimento.isdigit() and fez_aniversário == True:
    idade = 2025 - int(ano_de_nascimento)
    print(idade)
elif ano_de_nascimento.isdigit() and fez_aniversário == False:
    idade = 2025 - int(ano_de_nascimento) -1
    print(idade)
else:
    print(f'insira um valor válido')