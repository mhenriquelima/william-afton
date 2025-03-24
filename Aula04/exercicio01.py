def is_input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('insira um número válido.')

n1 = is_input_float("Digite um número: ")
n2 = is_input_float("Digite um número: ")

soma = n1 + n2
mult = n1 * n2
media = soma/2
print(f'''
A soma dos números é {soma}
O produto dos números é {mult}
A média dos números é {media}''')