# faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade, se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar ou se ja passou do tempo do alistamento
# seu programa tambem devera mostra o tempo que falta ou que passou do prazo.

# exercicio

from datetime import date
atual= date.today().year
nasc=int(input('ano de nascimento'))
idade= atual - nasc
print('quem nasceu me {} tem {} anos em {}'.format(nasc, idade, atual))
saldo=18- idade
saldo2=idade-18
if idade==18:
    print('voce tem que se alistar imediatamente')
elif idade <18:
    print(' voce nao tem 18 anos. ainda falta {} anos para o alistamento'.format(saldo))
else:
    print('voce ja deveria ter se alistado ha {} anos.'.format(saldo2))

