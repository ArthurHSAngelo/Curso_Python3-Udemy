"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'

nome = 'Arthur Henrique'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = (nome[indice])
    novo_nome += letra
    novo_nome += '*'
    indice += 1

print(novo_nome)
