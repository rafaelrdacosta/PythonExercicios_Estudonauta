'''
Exercício 011
Resolução Rafael Costa
============================================
Faça um programa que leia a largura e a
altura de uma parede em metros. Calcule a
quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma
área de 2m².
============================================
'''

#Entrada de dados pelo usuário
largura = float(input('Qual a largura da parede (m): '))
altura = float(input('Qual a altura da parede(m): '))

#Cálculo da área
area = largura * altura

#Cálculo da quantidade de tinta necessária para pintura
tinta = area/2

#Exibição do resultado
print('Sua parede tem a dimensão de {} x {} e sua área é de {:.2f}m².'.format(largura, altura, area))
print("Para pintar essa parede, você precisará de {:.2f}l de tinta.".format(tinta))