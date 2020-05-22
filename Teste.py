from random import randint
from time import sleep
print('{:=^50}'.format(''))
print('{:^50}'.format(' Jogo do Par ou Ímpar '))
print('{:=^50}'.format(''))
vitorias = 0
while True:
    # Pegando o import e colocando em uma variável
    computer = randint(0, 10)
    gamer = int(input('Digite um número inteiro: '))
    tot = computer + gamer
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? ')).strip().upper()[0]
    # Se for par
    if tipo == 'P':
        if tot % 2 == 0:
            vitorias += 1
            print('Você venceu!!')
            print('Vamos jogar novamente...')
        else:
            # Senão...
            sleep(0.5)
            print('Você pergeu! GAME OVER! FOI TRISTE KKKKKKKKKKKKKK')
            print(f'Você venceu {vitorias} vezes.')
            break
    # Se o total for ímpar
    else:
        if tot % 2 != 0:
            vitorias += 1
            print('Você venceu!!')
            print('Vamos jogar novamente...')
        else:
            # Senão...
            sleep(0.5)
            print('Você pergeu! GAME OVER! FOI TRISTE KKKKKKKKKKKKKK')
            print(f'Você venceu {vitorias} vezes.')
            break
print('{:=^50}'.format(''))