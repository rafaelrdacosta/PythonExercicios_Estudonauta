'''
Exercício 014
Resolução Rafael Costa
============================================
Faça um algoritmo que leia uma temperatura
em ºC e converta para ºF.
============================================
'''

#Entrada de dados pelo usuário
celsius = float(input('Informe a temperatura em ºC: '))

#Conversão para Fahrenheit
faren = ((celsius*9) / 5) + 32

#Exibição do Resultado
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF!'.format(celsius, faren))