'''
Exercício 006
Resolução Rafael Costa
============================================
Crie um algoritmo que leia um número e mostre
mostre o seu dobro, triplo e raiz quadrada.
============================================
'''

import math

#Entrda de dados pelo usuário
num = int(input('Digite um número: '))

#Raiz quadrada de num
raiz = math.sqrt(num)  # ou raiz = n ** (1/2), ou ainda, raiz = pow(n, (1/2))

#Exibição do resultado
print('O dobro de {} é igual a {}.'.format(num, num*2))
print('O triplo de {} é igual a {}.'.format(num, num*3))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(num, raiz))
