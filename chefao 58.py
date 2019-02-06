# melhore o jogo do desafio 28 onde o computador vai
# 'pensar' em um numero entre 0 e 10 . so que agora
# o jogador vai tentar adivinhar até acertar. mostrando no final
# quanto palpites foram necessarios para vencer.

# exercicio

from random import randint

computador = randint(1,10)
print('sou seu computador ... acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar ?')
acertou = False
palpite =0
while not acertou:
    jogador = int(input(' Qual é o seu palpite?'))
    palpite +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais ... tente mais uma vez.')
        elif jogador > computador:
            print('Menos ... tente outra vez.')
print('Acertou com {} tentativas'.format(palpite))

