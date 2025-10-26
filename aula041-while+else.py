""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('O else foi executado.') # não é executado quando aparece um "else" dentro do while
print('Fora do while.')
