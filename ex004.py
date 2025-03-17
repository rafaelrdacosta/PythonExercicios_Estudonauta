'''
Exercício 004
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
print('O tipo primitivo desse valor é ', type(entrada))

#Verificar se foi digitado somente espaços
print('Só tem espaços? ', entrada.isspace())

#Verificar se é um número
print('É um número:', entrada.isnumeric())

#Verificar se é alphabético
print('É alfabético:', entrada.isalpha())

#Verificar se é alphanumérico
print('É alfanumérico:', entrada.isalnum())

#Verificar se é maiúsculo
print('Está em letras maiúsculas:', entrada.isupper())

#Verificar se é minúsculo
print('Está em letras minúsculas:', entrada.islower())

#Verifciar se está capitalizado
print('Esta capitalizada:', entrada.istitle())
#Verificar se é digito
print('É um dígito:', entrada.isdigit())