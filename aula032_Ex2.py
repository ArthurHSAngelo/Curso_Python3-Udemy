"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
try:
    horario = int(input('Que horas são (0-23 horas)? '))
    if 0 <= horario <= 11:
        print('Bom dia')
    elif 12 <= horario <= 17:
        print('Boa tarde')
    elif 18 <= horario <= 23:
        print('Boa noite')
    else:
        print('Esse horário não é válido')

except:
    print('Horário inválido. Digite apenas números inteiros.')
