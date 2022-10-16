"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    There are pictures more than 'hangman'.
    """
    answer = random_word()
    question = ''
    for i in range(len(answer)):
        question += '-'
    hp = 7
    new_question = ''
    while True:
        print('The word looks like ' + question)
        print('You have ' + str(hp) + ' wrong guesses left.')
        hangman(hp)
        guess = input('Your guess: ')
        while True:
            if len(guess) == 1:
                if guess.isalpha():
                    break
            print('Illegal format.')
            guess = input('Your guess: ')
        if guess.islower():
            guess = guess.upper()
        for i in range(len(answer)):
            ch = answer[i]
            if guess == ch:
                new_question += guess
            else:
                new_question += question[i]
        if guess in answer:
            print('You are correct!')
        else:
            hp -= 1
            print('There is no ' + guess + '\'s in the word.')
        question = new_question
        new_question = ''
        if hp == 0:
            dead()
            print('You are completely hung : (')
            print('The word was: ' + answer)
            break
        if not str('-') in question:
            alive()
            print('You win!!')
            print('The word was: ' + answer)
            break


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def hangman(hp):
    if hp == 7:
        print('-------------')
        print(' |      v')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print('-------------')
    elif hp == 6:
        print('-------------')
        print(' |      |')
        print(' |     vVv')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print('-------------')
    elif hp == 5:
        print('-------------')
        print(' |      |')
        print(' |     vVv')
        print(' |    (\' \')')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print('-------------')
    elif hp == 4:
        print('-------------')
        print(' |      |')
        print(' |     vVv')
        print(' |    (\' \')')
        print(' |    /| |\\')
        print(' |')
        print(' |')
        print(' |')
        print(' |')
        print('-------------')
    elif hp == 3:
        print('-------------')
        print(' |      |')
        print(' |     vVv')
        print(' |    (\' \')')
        print(' |    /| |\\')
        print(' |   | | | |')
        print(' |')
        print(' |')
        print(' |')
        print('-------------')
    elif hp == 2:
        print('-------------')
        print(' |      |')
        print(' |     vVv')
        print(' |    (\' \')')
        print(' |    /| |\\')
        print(' |   | | | |')
        print(' |     / \\')
        print(' |')
        print(' |')
        print('-------------')
    else:
        print('-------------')
        print(' |      |')
        print(' |     vVv')
        print(' |    (\' \')')
        print(' |    /| |\\')
        print(' |   | | | |')
        print(' |     / \\')
        print(' |    |   |')
        print(' |')
        print('-------------')


def alive():
    print('')
    print('            vVv')
    print('           (^ ^)')
    print('           /| |\\/')
    print('           \\| |_')
    print('      E=   _/  /')
    print('')



def dead():
    print('-------------')
    print(' |      |')
    print(' |     vVv')
    print(' |    (x x)')
    print(' |    /| |\\')
    print(' |   | | | |')
    print(' |     / \\')
    print(' |    |   |')
    print(' |')
    print('-------------')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
