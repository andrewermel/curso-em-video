# escreva um programa que leia dois numeros interio e compare-os,
# mostrando na tela uma mensagem:
# -o primeiro numero é maior
# -o segundo numero é maior
# - os dois numeros são iguais

# exercicio

n1= int(input('primeiro numero:'))
n2= int(input('segundo numero '))

if n1 > n2:
    print('o PRIMEIRO NUMERO É MAIOR')
elif n1< n2:
    print('o segundo numero é maior')
else:
    print('os dois numeros são iguais')