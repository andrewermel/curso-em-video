# crie um programa que leia dois valores
# e mostre um menu com o ao lado na tela:
# Seu program deverá realizar a operação solicitada em cada caso.

# menu
# [1] somar
# [2]multiplicar
# [3]maior
# [4]novos numeros
# [5]sair do programa

n1 = int(input('primeiro numero '))
n2 = int(input('segundo numero'))
opção= 0
while opção !=5:
    print('''    [1] somar
    [2]multiplicar                  problemas para colocar dentro da operação( resolver)
    [3]maior
    [4]novos numeros
    [5]sair do programa''')
    opção = int(input('Qual a sua opção ?'))
    if opção == 1:
        soma = n1+n2
        print('a soma entre {} e {} é {}'.format(n1,n2,soma))
    elif opção ==2:
        produto = n1*n2
        print('o resultado de {} x {} é {}'.format(n1,n2,produto))
    elif opção ==3:
        if n1>n2:
            maior = n1
        else:
            maior = n2
        print('entre {} e {} o maior é {}'.format(n1,n2,maior))
    elif opção ==4:
        print('informe os numeros novamente')
        n1=int(input('primeiro numero'))
        n2=int(input('segundo numero'))

    elif opção ==5:
        print('finalizando')

    else:
        print('opção invalida. tente novamente')
print('fim do programa')





