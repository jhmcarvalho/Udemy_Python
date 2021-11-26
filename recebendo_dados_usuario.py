"""
Recebendo dados do usuário
**Todo dado do tipo input() é uma String. Em Python, string é tudo que tiver entre aspas simples, duplas, triplas ou duplas triplas.
Exemplos:
-Aspas simples -> 'Jeferson Martins'
-Aspas dupals -> "Jeferson Martins"
-Aspas simples triplas -> '''Jeferson Martins'''
Aspas duplas triplas -> """#Jeferson Martins"""
"""
"""
print("Qual seu nome? ")
nome = input()
# Pra usar só uma linha: nome = input('Qual seu nome? ')

print(f'Seja bem-vindo(a) {nome.title()}')

print("Qual sua idade? ")
idade = input()
if idade.isnumeric():
    print(f'{nome.title()} tem {idade} anos e nasceu em {2021 - int(idade)}')
else:
    print('Desculpe, o valor digitado não é válido')



