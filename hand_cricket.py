import math
import random


toss_choice = (input('Choose Odd or Even :')).capitalize()

computer_input = random.randint(1,11)
while True:
    try:
        player_input = int(input('Enter a number for toss :'))
        assert 0 <= player_input < 11
    except ValueError:
        print("Not an integer! Please enter an integer.")
    except AssertionError:
        print("Please enter an integer from 1 to 10")
    else:
        break

print(f'Comp : {computer_input}')
print(f'player : {player_input}')

b_b = ['Batting','Bowling']
State = ""
if toss_choice == 'Even':
    if ((int(computer_input) + int(player_input))%2 == 0):
        print('You WON the TOSS !!')
        State = input('Do you want to Batt or Bowl (Batting or Bowling):')
    else:
        comp = random.choice(b_b)
        if comp == 'Batting':
            print(f'The Computer WON the TOSS and chose {comp}')
            State = 'Bowling'
        elif comp == 'Bowling':
            print(f'The Computer WON the TOSS and chose {comp}')
            State = 'Batting'

        
if toss_choice == 'Odd':
    if ((int(computer_input) + int(player_input))%2 == 1):
        print('You WON the TOSS !!')
        State = (input('Do you want to Batt or Bowl (Batting or Bowling):'))
        State.capitalize()
    else:
        comp = random.choice(b_b)
        if comp == 'Batting':
            print(f'The Computer WON the TOSS and chose {comp}')
            State = 'Bowling'
        elif comp == 'Bowling':
            print(f'The Computer WON the TOSS and chose {comp}')
            State = 'Batting'

print(f'player : {State}')

score = 0
target = 1
innings = 1

while True:
    while True:
        try:
            player_num = int(input(f'You are {State} and its innings {innings}. Enter the number :'))
            assert 0 <= player_num < 11
        except ValueError:
            print("Not an integer! Please enter an integer.")
        except AssertionError:
            print("Please enter an integer from 1 to 10")
        else:
            break
    computer_num = random.randint(1,11)

    if (player_num == computer_num):
        if (State == 'Batting' and innings == 1):
            State = 'Bowling'
            innings = 2
            print('Achooooo! You are out. Go defend your target')
            print(f'Your score is {score}')
        elif (State == 'Bowling' and innings == 1):
            State = 'Batting'
            innings = 2
            print(f'Hurray!! The computer is out. Chase your Target..')
            print(f'You should hit {target}')
        elif (State == 'Batting' and innings == 2):
            print('Computer Won the match')
            break
        elif  (State == 'Bowling' and innings == 2):
            print('You Won the match')
            break
        else:
            break

    else:
        if (State == 'Batting' and innings == 1):
            score += player_num
            print(f'Your score for now {score}')
        elif (State == 'Bowling' and innings == 1):
            target += computer_num
            print(f"The computer's score for now {target - 1}")
        elif (State == 'Batting' and innings == 2):
            if(target - player_num > 0):
                target -= player_num
                print(f'You should hit more {target} runs')
                pass
            else:
                print('you won the match')
                break
        elif (State == 'Bowling' and innings == 2):
            if(score - player_num > 0):
                score -= computer_num
                print(f'You have {score} more runs to defend.')
                pass
            else:
                print('Computer won the match')
                break
        else:
            break