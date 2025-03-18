'''
Exercício 008
Resolução Rafael Costa
============================================
Escreva um programa que leia um valor em
metros e o exiba convertido em centímetros
e milímetros.
============================================
'''

#Entrada de dados pelo usuário
valor = float(input('Digite um valor (metros): '))

#Exibição do resultado
print('{} metros são {} centímetros.'.format(valor, valor*100))
print('{} metros são {} milímetros.'.format(valor, valor*1000))