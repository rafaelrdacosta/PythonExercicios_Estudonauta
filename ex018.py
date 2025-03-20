'''
Exercício 018
Resolução Rafael Costa
============================================
Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno,
e tangentes desse ângulo.
============================================
'''

import math

#Entrada de dados pelo usuário
angulo = int(input('Qual é o ângulo: '))

#Exibição dos resultados
print('Seno do ângulo {}º é igual a {:.2f}'.format(angulo, math.sin(angulo)))
print('Cosseno do ângulo {}º é igual a {:.2f}'.format(angulo, math.cos(angulo)))
print('Tangente do ângulo {}º é igual a {:.2f}'.format(angulo, math.tan(angulo)))