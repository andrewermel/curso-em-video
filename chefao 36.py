casaInputada=input('valor da casa')
casaFormatada=casaInputada.replace(',', '.')
casa=float(casaFormatada)
salario=float(input('salario do comprador'))
anos=int(input('quantos anos de financiamento'))
prestacao = casa / (anos*12)
print('para pagar uma casa de {} em {} anos'.format(casa , anos))
print(' a prestação sera de {}'.format(prestacao))

limite =(salario/100)*30

if limite >= prestacao:
            print('aprovado')
else:
    print('negado')
