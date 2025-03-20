n1 = input('n1 > ')
n2 = input('n2 > ')

if n1.isdigit() and n2.isdigit():
    soma = int(n1) + int(n2)
    print(f'a soma entre {n1} e {n2} é {soma}')
else:
    print(f'{n1} e/ou {n2} são valores inválidos')