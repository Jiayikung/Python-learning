"""
File: find_max.py
Name: Doris
--------------------------
This program finds the maximum among
all the user inputs. Students can refer to
this file when they are doing Problem 4
in Assignment 2
"""

# This constant controls when to stop
EXIT = -1 # Sentinel value


def main():
    """
    This program finds the maximum among
    user inputs
    """
    print('This program finds the max!')
    data = int(input('Data: '))
    if data == EXIT:
        print('no numbers.')
    else:
        maximum = data
        # while loop
        while True:
            data = int(input('Data: '))
            if data == EXIT:
                break
            if data > maximum:
                maximum = data
        print(maximum)





# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
