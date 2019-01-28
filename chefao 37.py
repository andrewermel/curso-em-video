#escreva um programa que leia um numero interio qualquer e peça para o usuario escolher qual sera a base de conversão:
# 1 para  binario
# 2 para octal
# 3 para hexadecimal

# exercicio

num=int(input('digite um numero inteiro:'))
print('''Escolha uma das bases para conversão:
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
op= int(input('Sua opção:'))
if op== 1:
    print('{} convertido para BINARIO é igual {}'.format(num, bin(num)[2:]))
elif op==2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif op== 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))

