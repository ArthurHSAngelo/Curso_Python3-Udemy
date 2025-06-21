# Operadores in e not in
# Strings são iteráveis 
# (item por item) (caractere por caractere)
#  0 1 2 3 4 5 
#  O t á v i o
# -6-5-4-3-2-1
nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
print('á' in nome) # True
print('zero' in nome) # False
print(10 * '-')
print('á' not in nome) # False
print('zero' not in nome) # True

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
