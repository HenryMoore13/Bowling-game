from time import sleep
from random import randint


def greeting():
    print('Welcome to Henry\'s Alley!!')
    print()


def bowl():
    frame = 0
    total = 0
    for i in range(10):
        roll, roll2 = 0, 0
        print('______________________________________________')
        print('\nBall is Rolling')
        sleep(.1)
        frame = frame + 1
        roll = int(input('\nRoll_1: How many Pins fell? '))
        if roll == 10:
            print('\n(STRIKE)')
            continue

        roll2 = int(input('\nRoll_2: How many Pins fell? '))
        if roll + roll2 == 10:
            print('\n(SPARE)')
        print('Frame:{}'.format(frame))
        total += (roll + roll2)
    print('Player Score: {}'.format(total))


def main():
    greeting()
    bowl()


if __name__ == '__main__':
    main()
