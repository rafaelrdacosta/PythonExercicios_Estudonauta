
n1 = input('Digite um valor: ')
print(type(n1))

n2 = int(input('Digite um valor: '))
print(type(n2))

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
s =  num1 + num2
print('A soma vale:', s)
print(f'A soma entre {num1} e {num2} vale {s}.')
print('A soma entre {} e {} vale {}.'.format(num1, num2, s))

n = float(input('Digite um valor: '))
print(n)

a = input('Digite algo: ')
print(a.isnumeric())

b = input('Digite algo: ')
print(b.isalpha())

c = input('Digite algo: ')
print(c.isalnum())