"""
PEP8 - Python Enchancement Proposal

[1] - Utilize Camel Case para nomes de classes; -- Exemplo: class Calculadora ou class CalculadoraCienifica;

[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis; -- Exemplo: soma ou soma_dois;

[3] - Utilize 4 espaços para identação - Não usar tab* Muito importante - - Exemplo:
if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco - Pra criar uma classe ou separar funções, deixar 2 linhas em branco acima; Métodos dentro de uma classe devem ser separados
com uma única linha em branco;


[5] - Imports - Imports devem ser sempre feitos em linhas separadas; Imports devem ser colocados logo no topo do arquivo, logo depois de quaisquer
comentários ou docstrings antes de constantes ou variáveis globais;

#Import Errado:
import sys, os

#Import Certo
import sys
import os


[6] - Espaço em expressões e instruções

#Errado:
1- funcao( algo[ 1 ], { outro: 2 } )
2- algo (1)
3- dict ['chave'] = list [indice]

#Certo
1- funcao(algo[1], {outro: 2})
2- algo(1)
3- dict['chave'] = lista[indice]

[7] - Termine sempre uma instrução com uma nova linha - Sempre deixar uma linha em branco no final de tudo.
"""
