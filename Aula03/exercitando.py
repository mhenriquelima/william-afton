class calc():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        if self.b == 0:
            return 'Operação inválida.'
        else:
            return self.a / self.b

    def pot(self):
        return self.a ** self.b

    def raiz(self):
        return self.a ** (1/self.b)

def is_input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('insira um número válido.')

def is_input_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('insira um número válido.')

is_running = True
historico = []
n1 = 0
n2 = 0
while is_running:
    selected_operation = is_input_integer('''
    Bem vindo a calculadora POG
        Escolha uma opção:
        1 - Soma
        2 - Subtração   
        3 - Multiplicação
        4 - Divisão
        5 - Potenciação
        6 - Raiz
        7 - Histórico
        8 - Sair
        ''')

    if 1 <= selected_operation <= 6:
        n1 = is_input_float('Digite o primeiro número > ')
        n2 = is_input_float('Digite o segundo número > ')
        calc_instance = calc(n1, n2)
        operations = [calc_instance.soma, calc_instance.sub, calc_instance.mult, calc_instance.div, calc_instance.pot, calc_instance.raiz]
        resultado = operations[selected_operation - 1]()
        operations_dict = {1: '+', 2: '-', 3: '*', 4: '/', 5: '^', 6: 'raiz'}
        historico.append(f'{n1} {operations_dict[selected_operation]} {n2} = {resultado}')
        print(f'O resultado é {resultado}')
    elif selected_operation == 7:
        print(historico)
    elif selected_operation == 8:
        is_running = False
    else:
        print('Opção inválida.')