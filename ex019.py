'''
Exercício 019
Resolução Rafael Costa
============================================
Um professor quer sortear um dos seus quatro
alunos para apagar o quadro. Faça um programa
que ajude ele, lendo o nome deles e escrevendo
o nome escolhido.
============================================
'''

import random

nome1 = str(input('Qual nome do 1º Aluno: '))
nome2 = str(input('Qual nome do 2º Aluno: '))
nome3 = str(input('Qual nome do 3º Aluno: '))
nome4 = str(input('Qual nome do 4º Aluno: '))

list = [nome1, nome2, nome3, nome4]

print('Aluno sorteado: {}'.format(random.choice(list)))
