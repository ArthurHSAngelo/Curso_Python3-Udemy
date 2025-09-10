"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'luiz Otávio'
# outra_variavel = f'{string[:3]}ABC{string[4:]}' # forma de mudar uma string, sem mexer na original. 
# print(string)
# print(outra_variavel)
print(string.zfill(20)) # esse método "zfill" preenche a string com zeros a esquerda, a quantidade é a todal de caracteres não de zeros.
