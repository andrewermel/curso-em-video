
primeiro = int(input('preimeiro termo'))
razao = int(input('digite a razao'))
termo = primeiro
cont= 1
while cont <= 10:
    print('{} >'.format(termo),end='')
    termo+=razao
    cont +=1
print('fim')
