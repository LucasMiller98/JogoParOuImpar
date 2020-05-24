# Para lançar números aleatórios
from random import randint
# Para dar um suspence
from time import sleep
print('{:=^50}'.format(''))
print('{:^50}'.format(' Jogo do Par ou Ímpar '))
print('{:=^50}'.format(''))
vitorias = 0
welcome = str(input('Qual é seu nome? ')).strip().upper()
question = ' '
while question not in 'PI':
    question = str(input(f'Bem-vindo, {welcome}. Você quer jogar em inglês ou em português? ')).strip().upper()[0]
# Sé o usuário escolher português...
if question == 'P':
    while True:
        # Pegando o import e colocando em uma variável
        computer = randint(0, 10)
        gamer = int(input(f'Digite um número inteiro, {welcome}: '))
        tot = computer + gamer
        tipo = ' '
        while tipo not in 'PI':
            tipo = str(input('Par ou ímpar? ')).strip().upper()[0]
        # Se for par
        if tipo == 'P':
            if tot % 2 == 0:
                vitorias += 1
                print(f'Você venceu, {welcome}!!')
                print('Vamos jogar novamente...')
            else:
                # Senão...
                sleep(0.5)
                print(f'Você pergeu, {welcome}! GAME OVER! FOI TRISTE KKKKKKKKKKKKKK')
                if vitorias == 0 or vitorias == 1:
                    print(f'Você venceu {vitorias} vez.')
                else:
                    print(f'Você venceu {vitorias} vezes.')
                break
        # Se o total for ímpar
        else:
            if tot % 2 != 0:
                vitorias += 1
                print(f'Você venceu, {welcome}!!')
                print('Vamos jogar novamente...')
            else:
                # Senão...
                sleep(0.5)
                print(f'Você pergeu, {welcome}! GAME OVER! FOI TRISTE KKKKKKKKKKKKKK')
                if vitorias == 0 or vitorias == 1:
                    print(f'Você venceu {vitorias} vez.')
                else:
                    print(f'Você venceu {vitorias} vezes.')
                break
# Se o usuário escolher inglês...
else:
    while True:
        # Pegando o import e colocando em uma variável
        computer = randint(0, 10)
        gamer = int(input(f'Type a interger number, {welcome}: '))
        tot = computer + gamer
        tipo = ' '
        while tipo not in 'EO':
            tipo = str(input('Even or odd? ')).strip().upper()[0]
        # Se for par
        if tipo == 'E':
            if tot % 2 == 0:
                vitorias += 1
                print(f'You won, {welcome}!!')
                print("Let's play again...")
            else:
                # Senão...
                sleep(0.5)
                print(f'You lose, {welcome}! GAME OVER! It was sad. LOL')
                if vitorias == 0 or vitorias == 1:
                    print(f'You won {vitorias} time.')
                else:
                    print(f'You won {vitorias} times.')
                break
        # Se o total for ímpar
        else:
            if tot % 2 != 0:
                vitorias += 1
                print(f'You won, {welcome}!!')
                print("Let's play again...")
            else:
                # Senão...
                sleep(0.5)
                print(f"You lose, {welcome}! GAME OVER! It was sad. LOL")
                if vitorias == 0 or vitorias == 1:
                    print(f'You won {vitorias} time.')
                else:
                    print(f'You won {vitorias} times.')
                break
print('{:=^50}'.format(''))