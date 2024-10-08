import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
wanna_play = True

while wanna_play is True:
    player_move = input('Choose [r]ock, [p]aper or [s]cissors: ')

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        raise SystemExit('Invalid Input. Try again...')

    computer_random_num = random.randint(1, 3)
    computer_move = ''
    if computer_random_num == 1:
        computer_move = rock
    elif computer_random_num == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f'The computer chose {computer_move}.\n')

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print('You win!')
    elif player_move == computer_move:
        print('Draw!\n')
    else:
        print('You lose! \n')
    wanna_play = input('Do you wanna play again? \n [y]es \n [n]o \n')
    if wanna_play == 'y':
        wanna_play = True
    elif wanna_play == 'n':
        wanna_play = False
    else:
        print('wrong command')
