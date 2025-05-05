def is_input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('insira um número válido.')

temp = is_input_float('Digite a temperatura em Celsius > ')
f = (temp * 9/5) + 32
print(f'A temperatura {temp}°C em Fahrenheit é {f}°F')