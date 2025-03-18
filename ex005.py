'''
Exercício 005
Resolução Rafael Costa
============================================
Faça um programa que leia um número inteiro
e mostre na tela o seu sucessor e seu
antecessor.
============================================
'''

#Entrada de dados pelo usuário
num = int(input('Digite um número inteiro: '))

#Exibição do resultado
print('O sucessor de {} é {}.'.format(num, num+1))
print('O antecessor de {} é {}.'.format(num, num-1))