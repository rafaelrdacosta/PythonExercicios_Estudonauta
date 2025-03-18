'''
Exercício 007
Resolução Rafael Costa
============================================
Desenvolva um programa que leia as duas notas
de um aluno, calcule e mostre a sua média.
============================================
'''

#Entrada de dados pelo usuário
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

#Cálculo da média
media = (nota1 + nota2)/2

#Exibição da média
print('A média entre as notas {:.1f} e {:.1f} é igual a {:.1f}.'.format(nota1, nota2, media))