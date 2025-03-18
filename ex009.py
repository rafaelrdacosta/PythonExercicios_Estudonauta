'''
Exercício 009
Resolução Rafael Costa
============================================
Faça um programa que leia um número inteiro
qulquer e mostre na tela a sua tabuada.
============================================
'''

#Entrada de dados pelo usuário
num = int(input('Digite um número: '))

#Exibição da tabuada do número
print('='*20)
print('Tabuada de {}'.format(num))
print('{:<2} x {:>2} = {:>2}'.format(num, 1, num*1))
print('{:<2} x {:>2} = {:>2}'.format(num, 2, num*2))
print('{:<2} x {:>2} = {:>2}'.format(num, 3, num*3))
print('{:<2} x {:>2} = {:>2}'.format(num, 4, num*4))
print('{:<2} x {:>2} = {:>2}'.format(num, 5, num*5))
print('{:<2} x {:>2} = {:>2}'.format(num, 6, num*6))
print('{:<2} x {:>2} = {:>2}'.format(num, 7, num*7))
print('{:<2} x {:>2} = {:>2}'.format(num, 8, num*8))
print('{:<2} x {:>2} = {:>2}'.format(num, 9, num*9))
print('{:<2} x {:>2} = {:>2}'.format(num, 10, num*10))
print('='*20)