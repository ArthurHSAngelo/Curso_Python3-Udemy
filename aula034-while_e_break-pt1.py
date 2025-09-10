"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem um ponto de parada 
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
    
    if nome == 'sair':
        break

print('Acabou') # é imprimido no terminal apenas quando o usuário digita "sair"
