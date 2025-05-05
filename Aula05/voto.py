def is_input_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('''
insira uma idade válida.
                  ''')

def pode_votar(idade):
    if idade > 0 and idade >= 16 and idade < 18 or idade >= 70 and idade < 120:
        print('''
Voto opcional
              ''')
    elif idade <= 0:
        print('''
Tu não nasceu ainda
              ''')
    elif idade >= 120:
        print('''
Tu Morreu, eu espero
              ''')
    elif idade >= 18:
        print('''
Voto obrigatório
              ''')
    else:
        print('''
Tu não pode votar
              ''')

def encerrar_app(rodando):
    print("Programa encerrado.")
    return False

is_rodando = True
while is_rodando:
    idade = is_input_integer('''
                             
                             
Digite a sua idade > ''')
    pode_votar(idade)
    continuar = input('''                     
Deseja continuar? 
[0] - Parar > '''


).lower()
    if continuar == "0":
        is_rodando = encerrar_app(is_rodando)