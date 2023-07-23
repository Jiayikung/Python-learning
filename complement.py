"""
File: complement.py
Name: Doris
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    The program helps find and print out the complementary strand for different types of DNA sequence.

    The rules of determining the complement strand are as follows:
    (1) A (Adenine) pairs with T (Thymine) together
    (2) C (Cytosine) pairs with G (Guanine) together
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    :param dna: The DNA sequence inputted by users
    :return ans: The complementary DNA sequence
    """
    if dna == '':
        return 'DNA strand is missing.'
    else:
       ans = ''  # Create an empty string
       for i in range(len(dna)):
           if dna[i] == 'A':
               ans += 'T'
           elif dna[i] == 'T':
               ans += 'A'
           elif dna[i] == 'C':
               ans += 'G'
           elif dna[i] == 'G':
               ans += 'C'
       return(ans)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
