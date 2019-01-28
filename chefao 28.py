from random import randint
pc= randint(0,5)
print('-=-'*20)
print('vou pensar em um numero entre 0, 5. tente adivinhar...')
print('-=-'*20)
jogador=int(input('em que numero eu pensei?'))
if jogador == pc:
    print('VOCE GANHO')
else:
    print('voce perdeu')


