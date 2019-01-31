# Refaça o DESAFIO 9, mostrando a
# tabuada de um numero que o
# usuario escolher, so que agora
# utilizando um laço for.

# exercicio

n = int(input('Digite um numero para ver sua Tabuada:'))
for c in range(1,11):
    print('{} x {:2} = {}'.format(n,c,n*c))