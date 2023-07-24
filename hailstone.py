"""
File: hailstone.py
Name: Doris
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    The random positive integer that the user entered
    will be multiplied by 3 plus 1 if the number is odd; be divided by 2 if the number is even.
    After multiple times of computation, the number will end up being 1
    and also show how many steps in order to reach the outcome.
    """
    print('This program computes Hailstone sequences')
    n = int(input('Enter a number:'))
    count = 0
    n1 = 0
    while True:
        if n == 1:
            break
        elif n % 2 == 0:
            n1 = n // 2
            print(str(n)+' is even, so I take half: '+str(n1))
        elif n % 2 == 1:
            n1 = 3 * n + 1
            print(str(n) + ' is odd, so I take 3n+1: '+str(n1))
        count += 1
        n = n1
    print('It took '+str(count)+' steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
