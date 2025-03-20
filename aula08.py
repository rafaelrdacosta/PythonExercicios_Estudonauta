import math

num = int(input('Digite um número: '))

raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
print('A raiz de {} é igual a {}'.format(num, math.trunc(raiz)))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

import random

n = random.random()
print(n)
a = random.randint(1, 10)
print(a)

#bibliotecas externas python.org
import emoji
print(emoji.emojize("Olá, Mundo!🌎"))