'''
Exercício 012
Resolução Rafael Costa
============================================
Faça um algoritmo que leia o preço de um
produto e mostre seu novo preço com 5% de
desconto.
============================================
'''

#Entrada de dados pelo usuário
preco = float(input('Qual o preço do produto? R$ '))

#Cálculo do desconto
preco_d = 0.95*preco

#Exibição do resultado
print('O valor do produto com 5% de desconto é R$ {:.2f}.'.format(preco_d))