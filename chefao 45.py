# criar um jogo de Joken po

from random import randint
itens=('pedra','papel','Tesoura')
computador = randint(0,2)
# print('O computador escolheu {}'.format(itens[computador]))
print('''Suas opções
 [0] Pedra
 [1] Papel
 [2] Tesoura''')
jogador =int(input('qual é a sua jogada?'))
print('-='*40)
print('O computador escolheu {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-='*40)

if computador==0: #computador jogou pedra
    if jogador==0:
        print('empate')

    elif jogador == 1:
        print('jogador vence')

    elif jogador == 2:
        print('jogador perde')

    else:
        print('jogada invalida')

# problemas no programas apartir de agora

elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('jogador perde')
        elif jogador == 1:
        print('empate')

        elif jogador == 2:
        print('jogador vence')

        else:
        print('jogada invalida')

elif computador == 2: #computador jogou Tesoura
    if jogador == 0:
        print('jogador vence')
        elif jogador == 1:
        print('jogador perde')

        elif jogador == 2:
        print('empate')

        else:
        print('jogada invalida')
#erro com a palavra jogador
