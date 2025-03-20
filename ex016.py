'''
Exercício 016
Resolução Rafael Costa
============================================
Crie um programa que leia um número Real
qualquer pelo teclado e mostre na tela a sua
posição inteira.
============================================
'''

from math import trunc

#Entrada de dados pelo usuário
num = float(input('Digite um número: '))

#Exibição da porção inteira de num
print('O número {} tem a parte inteira {}.'.format(num, trunc(num)))