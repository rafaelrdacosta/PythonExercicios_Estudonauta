'''
Exercício 020
Resolução Rafael Costa
============================================
Um professor quer sortear a ordem de apresen-
tação de trabalhos dos alunos. Faça um
programa que leia o nome dos quatro alunos
e mostre a ordem sorteada
============================================
'''

nome1 = str(input('Qual nome do 1º Aluno: '))
nome2 = str(input('Qual nome do 2º Aluno: '))
nome3 = str(input('Qual nome do 3º Aluno: '))
nome4 = str(input('Qual nome do 4º Aluno: '))

list = [nome1, nome2, nome3, nome4]
list.sort()
print('Sequência de apresentação: {}'.format(list))
