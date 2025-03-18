'''
Exercício 015
Resolução Rafael Costa
============================================
Escreva um programa que pergunte a quantidade
de km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi
alugado. Calcule o preço a pagar, sabendo
que o carro cust R$60 por dia e R$0.15 por
km rodado.
============================================
'''

#Entrada de dados pelo usuário
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

#Cálculo do valor do aluguel
aluguel = (dias*60) + (0.15*km)

#Exibição do resultado
print('O total a pagar é R$ {:.2f}.'.format(aluguel))

