'''
Exercício 013
Resolução Rafael Costa
============================================
Faça um algoritmo que leia o salário de um
funcionário e mostre seu novo salário, com
15% de aumento.
============================================
'''

#Entrada de dados pelu usuário
salario = float(input('Qual é o seu salário: R$ '))

#Cálculo do salário com aumento de 15%
salario_n = 1.15*salario

#Exibição do novo salário
print('Seu novo salário com aumento de 15% é R$ {:.2f}.'.format(salario_n))