"""
File: my_smaller.py
Name: Doris
-------------------------
This program implements a my_smaller function
which takes 2 arguments and outputs the
smaller one
"""


def main():
    """
    Call my_smaller function
    """
    n1 = int(input('First Number: '))
    n2 = int(input('Second Number: '))
    smaller = my_smaller(n1, n2)
    print(smaller)


def my_smaller(n1, n2):
    """
    :param n1: int, the first number to be compared.
    :param n2: int, the second number to be compared.
    :return:
    """
    if n1 < n2:
        return n1
    return n2


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
