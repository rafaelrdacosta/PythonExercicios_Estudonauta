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
valor = float(input('Digite uma distância (metros): '))

#Exibição do resultado
print('A medida de {}m corresponde a:'.format(valor))
print('{} km.'.format(valor/1000))
print('{} hm.'.format(valor/100))
print('{} dam.'.format(valor/10))
print('{} dm.'.format(valor*10))
print('{} cm.'.format(valor*100))
print('{} mm.'.format(valor*1000))

