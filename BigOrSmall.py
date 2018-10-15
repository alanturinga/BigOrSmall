import random
import os

def roll_dice(numbers = 3, points = None):
    print('<<<<< ROLL THE DICE! >>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers - 1
    return points

def roll_result(total):
    isBig = 11 <= total
    isSmall = 3 <= total <= 10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'

def start_game():
    print('<<<<< GAME START! >>>>>')
    choices = ['Big', 'Small','Exit']
    your_choice = input("Choose Big or Small, or input 'Exit' to leave the game: ")
    if your_choice in choices:
        if your_choice == 'Exit':
            return 0
        else:
            points = roll_dice()
            total = sum(points)
            you_win = your_choice == roll_result(total)
            if you_win:
                print('The points are ', points, '. You win!')
                return 1
            else:
                print('The points are ', points, '. You lose!')
                return -1
    else:
        print('Invalid words!')
        start_game()

Amount = 1000
flag = 0
while Amount > 0:
    flag = start_game()
    #print(flag)
    if flag == 1:
        #print(flag+1)
        Amount = Amount + flag * 1000
        print('You gained 1000, you have {} now.'.format(Amount))
    elif flag == -1:
        #print(flag-1)
        Amount = Amount + flag * 500
        print('You lose 500, you have {} now.'.format(Amount))
    if Amount == 0:
        print('<<<<< GAME OVER >>>>>')
        break
    if flag == 0:
        print('Exit the Game.')
        break
os.system("pause")