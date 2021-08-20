from random import randint
from time import sleep
computador = randint(0, 5)# o computador pensa
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número entre 0 e 5 eu pensei? '))#jogador advinha
print('PROCESSANDO...')
sleep(1)
print('BIP, BOP!')
if jogador == computador:
    print('Parabens! Você conseguiu me vender!')
else:
    print('Ganhei! Eu pensei no numero {} e não no {}!'.format(computador, jogador))