"""
Utilitários Python para auxiliar na programação.

**Todo dado do tipo input() é uma String. Em Python, string é tudo que tiver entre aspas simples, duplas, triplas ou duplas triplas.
Exemplos:
-Aspas simples -> 'Jeferson Martins'
-Aspas dupals -> "Jeferson Martins"
-Aspas simples triplas -> '''Jeferson Martins'''
-Aspas duplas triplas -> """#Jeferson Martins"""

"""
dir -> Apresenta todos os atributos/propriedades e funções/métodos disponíveis para determinado tipo de dado ou variável.
-->Como usar: dir(tipo de dado/variável) - Exemplo: dir("Jeferson")

help -> Apresenta a documentação/como utilizar os atributos/propriedade e funções/métodos disponíveis para determinado
tipo de dado ou variável.
-->Como usar: help(tipo de dado/variavel.propriedade) - Exemplo: help("Jeferson".upper)
"""


#PRINTS
nome = 'Jeferson Martins'

"""
print(nome.split()) #Transforma em uma lista de strings;
print(nome.split()[0]) #Acessa a primeira parte da lista dividida (Jeferson Martins apareceria Jeferson);
print(nome.split())[1] #Acessa a segunda parte da lista dividida (Jeferson Martins apareceria Martins);
print(nome.upper()) #Transforma em maiúsculo;
print(nome.lower()) #Transforma em minúsculo;
print(nome[0:8]) #Exibe somente parte da string. Nesse caso, da posição 0 até a 8 -- Slice de string;
print(nome[::-1]) #Inverte tudo. :vai do primeiro elemento, :vai até o ultimo elemento, -1 inverte;
print(nome.replace('J', 'G')) #Onde possui a letra J vai mudar para G;

"""

#VARIAVEIS
"""
1- Variaveis globais - São reconhecidas em todo o programa, ou seja, seu escopo compreende tudo;
2- Variaveis locais - São reconhecidas apenas no bloco onde foram declaradas, ou seja, seu espoco está limitado ao bloco onde foi declarada;

*Para declarar variaveis em Python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem do tipo dinâmica, ou seja, ao declarar uma variavel, não colocamos o tipo dela. Esse tipo é inferido ao atribuírmos valor á ela.
Exemplo em C: 
int numero = 42;

Exemplo em Java:
int numero = 42;

Exemplo em Python:
numero = 42; - Variavel global;

numero = 42
if numero > 10:
    novo = numero + 10 --Essa variável "novo" não será criada caso o numero seja menor do que 10 nesse caso, então essa variável é local;
    print(novo)

"""

#IF/ELSE/ELIF
"""
Estrutura condicionais
if, else, elif - Elif é a mesma coisa de 'else if'; --Pra mudar o bloco, a próxima linha precisa ter 4 espaços, ou seja, um tab;
"""
'''
idade = 6
if idade < 18:
    print('Menor de idade')
else:
    print('Maior de idade')
'''

'''
idade = 18
if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')
'''

#AND, OR, NOT, IS
"""
Estruturas lógicas: and(e), or(ou), not(não), is(é);
*AND - Ambos precisam ser true;
*OR - Ou um ou outro precisam ser true;
*NOT - O valor do booleano é invertido. Ou seja, se for true vira false, se for false vira true;
*IS - Como se fosse um igual

-Operadores unários:
    -not;
-Operadores binários:
    -and, or, is;
"""

"""
ativo = False
logado = True

if ativo is False:
    logado = False

if ativo and logado:
    print('Bem vindo usuário!')
elif ativo and not logado:
    print('Usuário ainda não conectou')
elif not ativo and not logado:
    print('Sua conta ainda não foi ativada, não é possível logar')
"""
