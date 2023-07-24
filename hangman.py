"""
File: hangman.py
Name: Doris
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
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
    The program allows users to make limited guesses on randomly chosen words.
    """
    wrong = 0  # The total number of wrong guesses
    guess = ''  # A string of guesses has inputted by the user
    answer = random_word()  # The correct answer in the game
    turns = N_TURNS  # The number of wrong guesses left in the game

    while True:
        # flag1 marks whether the inputted guess is wrong answer or not
        flag1 = 0
        # flag2 marks two different scenarios that break the game
        flag2 = 0

        hidden = dashed(answer, guess)
        print('The word looks like ' + hidden)
        print('You have ' + str(turns) + ' wrong guesses left.')
        input_ch = input('Your guess: ').upper()  # an case-insensitive alphabet inputted by user

        # If having wrong format, keep asking user to input guesses until getting correct one
        while not input_ch.isalpha() or len(input_ch) != 1:
            print('Illegal format.')
            input_ch = input('Your guess: ').upper()
        guess = guess + input_ch  # append the new guesses into the string of guess
        if input_ch not in answer:  # If the new guesses is wrong
            wrong += 1
            flag1 = 1

        # Wrong guesses left = total wrong guesses in game - total number of wrong guesses
        turns = N_TURNS - wrong

        if flag1 == 0:  # flag1 == 0 denotes it's the correct guess
            print('You are correct!')
        elif flag1 == 1:  # flag1 == 1 denotes it's the wrong guess
            print('There is no ' + input_ch +"'s "+ 'in the word.')

        # Two different scenarios that break the game:
        if hidden == answer:  # flag2 == 0 denotes it ultimately get correct answer
            flag2 = 0
            break
        if turns == 0:  # flag2 == 1 denotes it has used up the number of guess the player has
            flag2 = 1
            break
    if flag2 == 0:
        print('You win!!')
    elif flag2 == 1:
        print('You are completely hung :(')
    print('The word was '+ answer)


def dashed(answer, guess):
    """
    :param answer: str, the correct answer in the game
    :param guess: str, a string of guesses has inputted by the user
    :return result: str, a combination of the dashed ('-') and alphabets
    """
    result = ''
    for i in range(len(answer)):
        if answer[i] in guess:
            result += answer[i]
        else:
            result += '-'
    return result


def random_word():
    """
    return: str, randomly choose correct answer in the game
    """
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


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
