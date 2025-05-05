input_x = input('')
valores_x = input_x.split()

input_y = input('')
valores_y = input_y.split()

x_1 = float(valores_x[0])
x_2 = float(valores_x[1])

y_1 = float(valores_y[0])
y_2 = float(valores_y[1])

distancia = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** (1/2)

print(f'''
x= ({x_1}), ({x_2}) y= ({y_1}), ({y_2})      
{distancia:.4f}
''')