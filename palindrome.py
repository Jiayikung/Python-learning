"""
File: palindrome.py
Name: Jerry Liao
----------------------------
This program finds if 5 words are palindrome by
using a recursive function called is_palindrome(s).
What is the self-similarity in this problem?
"""


def main():
	print(is_palindrome('madam'))             # True
	print(is_palindrome('step on no pets'))   # True
	print(is_palindrome('QQ'))                # True
	print(is_palindrome('pythonpy'))          # False
	print(is_palindrome('notion'))            # False


def is_palindrome(s):
	if len(s) == 1:
		return True
	elif len(s) == 0:
		return True
	else:
		if s[0] != s[-1]:
			return False
		return is_palindrome(s[1:len(s)-1])


if __name__ == '__main__':
	main()
