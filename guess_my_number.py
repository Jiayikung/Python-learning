"""
File: guess_my_number.py
Name: Doris
-----------------------------
This program plays a Console game
"Guess My Number" which asks user
to input a number until he/she gets it
"""

# This number controls when to stop the game
SECRET = 32


# Solution 1:
def main():
    print('Guess a number from 0-99')
    while True:
        guess = int(input('Your guess'))
        if guess > SECRET:
            print('Too high')
        elif guess < SECRET:
            print('Too low')
        else:
            break
    print('Congrats! The secret is' + str(SECRET))

# Solution 2:
# def main():
#     print('Guess a number from 0-99')
#     guess = int(input('Your guess'))
#     while guess != SECRET:
#         # Wrong guess
#         if guess > SECRET:
#             print('Too high')
#         else:
#             print('Too low')
#         guess = int(input('Your guess'))
#     # Correct!
#     print('Congrats! The secret is'+str(SECRET))


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
