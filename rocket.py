"""
File: rocket.py
Name: Doris
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.
"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    This program will print out a rocket pattern with certain size defined by 'SIZE'.
    To make it easier to understand,
    We divide the rocket into four different parts,
    which are head, belt, upper, and lower parts.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    The head part is a regular triangle
    filled up with incrementally increasing '/' and '\' symbols.
    """
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(' ', end='')
        for j in range(i+1):
            print('/', end='')
        for j in range(i+1):
            print('\\', end='')
        print('')  # Add the line break


def belt():
    """
    The belt part is a horizontal line starts and ends with a '+' symbol,
    while '=' symbols will repeat several times to create the main body of the line.
    """
    print('+', end='')
    for i in range(SIZE*2):
        print('=', end='')
    print('+', end='')
    print('')


def upper():
    """
    The upper part can be divided into three layers:
    (1) The outer layer, displayed by the '|' pattern
    (2) The middle layer, filled up by the '.' pattern
    (3) The inner layer, presented as a pyramid-like image
        and created by the '/' and '\' patterns
    """
    for i in range(SIZE):
        print('|', end='')  # Create the outer layer on the left side
        for j in range(SIZE-i-1):  # Create the middle layer on the left side
            print('.', end='')
        for j in range(i*2+2):  # Create the inner layer
            if j % 2 == 0:
                print('/', end='')
            else:
                print('\\', end='')
        for j in range(SIZE-i-1):  # Create the middle layer on the right side
            print('.', end='')
        print('|', end='')  # Create the outer layer on the right side
        print('')


def lower():
    """
    The lower part is the upside-down version of the upper part.
    """
    for i in range(SIZE):
        print('|', end='')
        for j in range(i):
            print('.', end='')
        for j in range(SIZE*2-i*2):
            if j % 2 == 0:
                print('\\', end='')
            else:
                print('/', end='')
        for j in range(i):
            print('.', end='')
        print('|', end='')
        print('')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
