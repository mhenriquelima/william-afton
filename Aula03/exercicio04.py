def is_input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('insira um número válido.')

nota1 = is_input_float('nota 1 > ')
nota2 = is_input_float('nota 2 > ')
nota3 = is_input_float('nota 3 > ')

media = (nota1 + nota2 + nota3) / 3
print(f'A média é {media:.2f}')