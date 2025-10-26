""" Calculadora com while """
while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num1_float = 0
    num2_float = 0
                       
    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números não são válidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue 

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print('Realizando operação. O resultado é: ')

    if operador == '+':
        print(num1_float + num2_float)
    elif operador == '-':
        print(num1_float - num2_float)
    elif operador == '*':
        print(num1_float * num2_float)
    elif operador == '/':
        print(num1_float / num2_float)
    else:
        print('Isso nunca deve ser mostrado.')

    sair = input('Quer sair? [s]im: ').lower()

    if sair.startswith('s'):
        break
