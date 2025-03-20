'''
Exercício 017
Resolução Rafael Costa
============================================
Faça um programa que leia o comprimento do
cateto oposto e do cateto adjacente de um
triângulo retângulo, calcule e mostre o
comprimento da hipotenusa.
============================================
'''

from math import hypot

#Entrada de dados pelo usuário
oposto = float(input('Qual o comprimento do cateto oposto(cm): '))
adjacente = float(input('Qual o comprimento do cateto adjacente(cm): '))

#Exibição da hipotenusa
print("A hipotenusa do triângulo retângulo com {}cm de cateto oposto e\n{}cm de cateto adjancente é igual a {:.2f}".format(oposto, adjacente, hypot(oposto, adjacente)))