'''
Exercício 010
Resolução Rafael Costa
============================================
Crie um programa que leia quanto dinheiro
uma pessoa tem na carteira e mostre quantos
dólares ela pode comprar.
Considere
US$ 1.00 = R$ 3.27
============================================
'''

#Entrada de dados pelo usuário
real = float(input('Quanto em R$ você tem: '))

#Cálculo do câmbio
dolar = real/3.27

#Exibição do resultado
print('R$ {:.2f} equivalem a US$ {:.2f} dólares.'.format(real, dolar))