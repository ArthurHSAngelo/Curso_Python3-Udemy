# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar': # Primeira condição
    print('Você entrou no sistema')

    print(12341234)
elif entrada == 'sair': # Depende do if
    print('Você saiu do sistema')

else: # Se nada for correspondido caí no else
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')