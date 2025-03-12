'''
Desafio 004
Resolução Rafael Costa
============================================
Programa que lê algo pelo teclado e mostra
na tela seu tipo primitivo e todas as
informações possíveis sobre ele.
============================================
'''

#Declaração de variável e entrada de dados
entrada = input('Digite algo: ')

#Tipo primitivo
print(type(entrada))

#Verificar se é um número
print('Numérico:', entrada.isnumeric())

#Verificar se é alphabético
print('Alfabético:', entrada.isalpha())

#Verificar se é alphanumérico
print('Alfanumérico:', entrada.isalnum())

#Verificar se é maiúsculo
print('Maiúsculo:', entrada.isupper())

#Verificar se é minúsculo
print('Minúsculo:', entrada.islower())

#Verificar se é digito
print('Digito:', entrada.isdigit())