# faça um programa que mostre na tela uma
# contagem regressiva para o estouro de
# fogos de artificio, indo de 10 até 0,com
# uma pausa de 1 segundo entre eles.

# exercicio

from time import sleep
for c in range(10,-1,-1):
    print(c)
    sleep(1)
print('BUMM, BUMM, POW')
