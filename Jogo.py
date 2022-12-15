from random import randint
from time import sleep


def linhaAmarela():
    print('\033[1;33m─\033[m' * 40)


def linhaVermelha():
    print('\033[1;31m─\033[m' * 40)


vermelho = '\033[1;31m'
noColor = '\033[m'
lista = ['Pedra', 'Papel', 'Tesoura']
nome = []
cont_jog = cont_comp = 0

titulo1 = 'Pedra - Papel - Tesoura'
linhaAmarela()
print(titulo1.center(40))
linhaAmarela()
print()
print()

while True:
    nome = str(input('Digite seu nome/nick: ')).strip()
    if len(nome) == 0:
        print(f'{vermelho}Digite um nome válido{noColor}')
    else:
        print('Tudo certo para começar o jogo, {}'.format(nome))
        linhaAmarela()
        print()
        sleep(1.5)
        break

while True:
    while True:
        jogador = int(input(f'Digite o número da sua escolha | {lista[0]}-0 | {lista[1]}-1 | {lista[2]}-2 | → '))
        if jogador not in range(0, 4):
            print('\033[1;31mValor incorreto\033[m')
            linhaVermelha()
            print()
            sleep(0.7)
        else:
            break

    computador = randint(0, 2)
    if computador == 0:
        print(f'O computador escolheu pedra')
    elif computador == 1:
        print(f'O computador escolheu papel')
    else:
        print(f'O computador escolheu tesoura')

    sleep(1.5)

    if jogador == 0:
        print('O jogador(a) {} escolheu pedra'.format(nome))
        linhaAmarela()
        print()
    elif jogador == 1:
        print('O jogador(a) {} escolheu papel'.format(nome))
        linhaAmarela()
        print()
    else:
        print('O jogador(a) {} escolheu tesoura'.format(nome))
        linhaAmarela()
        print()
    sleep(1.5)

    print('\033[1;32m Jo \033[m')
    sleep(0.5)
    print('\033[1;32m Ken \033[m')
    sleep(0.5)
    print('\033[1;32m Pô \033[m')
    print()
    sleep(0.5)

    if computador == 0:
        if jogador == 0:
            linhaAmarela()
            print('houve um EMPATE!')

        elif jogador == 1:
            linhaAmarela()
            print('Jogador ganhou.')
            cont_jog += 1

        elif jogador == 2:
            linhaAmarela()
            print('Computador ganhou.')
            cont_comp += 1

        else:
            linhaVermelha()
            print('JOGADA INVÁLIDA!')

    elif computador == 1:
        if jogador == 0:
            linhaAmarela()
            print('Computador ganhou.')
            cont_comp += 1

        elif jogador == 1:
            linhaAmarela()
            print('Houve um EMPATE!')

        elif jogador == 2:
            linhaAmarela()
            print('Jogador ganhou.')
            cont_jog += 1
        else:
            linhaVermelha()
            print('JOGADA INVÁLIDA!')

    elif computador == 2:

        if jogador == 0:
            linhaAmarela()
            print('Jogador ganhou.')
            cont_jog += 1

        elif jogador == 1:
            linhaAmarela()
            print('Computador ganhou.')
            cont_comp += 1

        elif jogador == 2:
            linhaAmarela()
            print('Houve um EMPATE!')

        else:
            linhaVermelha()
            print('JOGADA INVÁLIDA!')

    print()
    titulo = 'PLACAR'
    print(titulo.center(30))
    linha = f' Jogador {cont_jog} x Computador {cont_comp}'
    print(linha.center(30))

    print()
    while True:
        fim = str(input('Deseja finalizar? S/N → ')).strip().upper()
        linhaAmarela()
        print()
        if fim[0] == 'S':
            exit()

        if fim[0] != 'N':
            print('Valor incorreto!')

        if fim[0] == 'N':
            break
