from random import randint
from time import sleep
computador = randint(0,5)
print('-=-'*20)
print('Vou pensar em um número de 0 a 5, tente adivinhar')
print('-=-' *20)
jogador = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('PARABÉNS! você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}'.format(computador, jogador))






