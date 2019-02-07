# faça um programa que leia um numero
# qualquer e mostre oseu fatorial
#
# ex 5= 5x4x3x2x1 = 120

# jeito de fazer com modolo

# from math import factorial
#
# n = int(input('diga um numero '))
# f = factorial(n)
# print('o faltorial de {} é {}'.format(n,f))

n = int(input('diga um numero '))
c = n
f = 1
while c > 0:
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))


