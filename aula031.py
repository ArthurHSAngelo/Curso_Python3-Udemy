"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e not is = é ou não é (tipo, valor, identidade)
"""

"""
id = Identidade

v1 = 'a' # Se uma váriavel tiver valor igual a uma outra, elas ocuparam o mesmo id na memória
v2 = 'a'
print(id(v1))
print(id(v2))
"""
condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True # Essa é a flag, que marca uma variável para ver uma condição, por exemlo se passou por algo ou não. 
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')
