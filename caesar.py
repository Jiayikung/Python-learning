"""
File: caesar.py
Name: Doris
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program allows users to decrypt a given string using a secret number as input.

    The deciphering strategy involves two steps:
    (1) Alphabet Rearrangement:
        We moves the last certain number of alphabets to the beginning of the string,
        creating a new alphabet string.
    (2) Decryption Process:
        We finds the location of each ciphered alphabet in the new alphabet string
        and uses this information to identify the corresponding original alphabet
        in the old alphabet string.
    """
    num = int(input('Secret number: '))
    ciphered = input("What's the ciphered string?: ")
    new = new_alphabet(num)
    print('The deciphered string is: ' + decipher(new, ciphered))


def new_alphabet(num):
    """
    It's the first step in our strategy.
	:param num: The last number of alphabets need to move to the beginning of the string
	:return result: The new alphabet string
	"""
    if num == 0:
        return 'You must be a SPY!'
    else:
        result = ''
        result = ALPHABET[len(ALPHABET)-num:] + ALPHABET[:len(ALPHABET)-num]
        return result


def decipher(new, ciphered):
    """
    It's the second step in our strategy.
    :param new: str, the new string of alphabets
    :param ciphered: str, the ciphered string
    :return ans: str, the deciphered string
    """
    ans = ''
    for ch in ciphered:
        # make the ciphered string be case-insensitive
        ch = ch.upper()
        if ch == ' ':
            ans += ' '
        elif ch == '!':
            ans += '!'
        else:
            # reveal the location of each ciphered alphabet in the new alphabet string
            i = new.find(ch)
            ans += ALPHABET[i]
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
