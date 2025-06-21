"""
Interpolação básica de strings
-> O que é?
basicamente é um format diferente

s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Arthur'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %08X' % (1500, 1500))