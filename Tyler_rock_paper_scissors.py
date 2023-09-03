#!/usr/bin/env python3
#creator: Tyler Kirkwood


print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_A = str(input("Player A: "))
    player_B = str(input("Player B: "))
    a = game_dict.get(player_A)
    b = game_dict.get(player_B)
    dif = a - b

    if dif in [-1, 2]:
        print('player A wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player B wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')
        print('')