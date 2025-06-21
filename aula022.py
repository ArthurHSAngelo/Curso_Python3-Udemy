"""
# Operadores lógicos

and (e) -  or (ou) - not (não)
or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.

-> Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.
-> São considerados falsy (que você já viu, tem outros):
0 0.0 '' False

Também existe o tipo "None" que é usado pra representar um não valor.
"""
entrada = input('[E]entrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
# if True:
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha' 
print(senha)
