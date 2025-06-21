"""
# Operadores lógicos

and (e) -  or (ou) - not (não)
and - Todas as condições precisam ser verdadeiras.

-> Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.
-> São considerados falsy (que você já viu, tem outros):
0 0.0 '' False

Também existe o tipo "None" que é usado pra representar um não valor.
"""
entrada = input('[E]entrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
# if True:
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
# avalia até certo ponto e ignora o restante.
print(True and False and True)
print(True and 0 and True)
if 1 and 1:
    print(True and 1 and False)