def is_input_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Insira um número válido.')

number = is_input_integer("Digite um número: ")
numlist = list(str(number))
reverse = numlist[::-1]
print("".join(reverse))