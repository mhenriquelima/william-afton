def is_input_integer(prompt):
    while True:
        try:
            int(input(prompt))
            return prompt
        except ValueError:
            print('insira um número válido.')
number = is_input_integer('Digite um número inteiro > ')
result = ''
for i in range(len(number)):
    result = result + number[-1]
print(result)