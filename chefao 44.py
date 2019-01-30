# Elabore um programa que calcule o valor a ser pago por um produto
# considerando o seu preço normal e condição de pagamento:
# - a vista dinheiro/cheque: 10% de desconto
# - a vista no cartao :5% de desconto
# - em até 2x no cartao : preço normal
# -3x ou mais no cartao : 20% de juros

# exercicio

print('{:=^40}'.format('LOJAS DO ANDREW'))

preço= float(input('preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[1] a vista dinheiro/cheque
[2] a vista no cartao 
[3] 2x no cartao
[4] 3x ou mais no cartao ''')

opção = int(input('qual é a opção?'))

if opção==1:
    total=preço-(preço*10/100)

elif opção == 2:
    total=preço -(preço*5/100)

elif opção==3:
    total = preço
    parcela= total/2
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))

else:
    total= preço+(preço*20/100)
    totparc=int(input('quantas parcelas?'))
    parcela=total/totparc
    print('Sua comra será parcelanda em {:.2f}x'.format(parcela))

print('Sua compra de R${:.2f} vai custar R$ {:.2f} no final '.format(preço,total))
