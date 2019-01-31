# Desenvolva um programa que leia o
# primeiro termo ea razão de uma progressão aritimetrica (PA)
# No Final, mostre os 10 primeiros termos dessa pregressão.

# exercicio

pn= int(input('primeiro numero:'))
r = int(input('Razao:'))
decimo = pn + (10-1)* r    #formula pra fazer 10 numeros ou mais [10 = x]

for c in range(pn,decimo+r,r):
    print('{}'.format(c),end=' > ')
print('ACABOU')
