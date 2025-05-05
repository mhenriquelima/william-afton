def is_input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('insira um número válido.')

n1 = is_input_float('Digite um número > ')
n2 = is_input_float('Digite um número > ')

soma = n1 + n2
mult = n1 * n2
media = soma/2

print(f'''
A soma dos de {n1} e {n2} é {soma}
O produto de {n1} e {n2} é {mult}
A média de {n1} e {n2} é {media}''')