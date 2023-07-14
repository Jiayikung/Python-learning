"""
File: prime_checker.py
Name: Doris
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

# This number controls when to stop the game
EXIT = -100


def main():
	"""
	This program can tell the user whether the number entered is a prime number.
	Also, the user can stop the game whenever inputting certain number as 'EXIT'.
	"""
	print('Welcome to the prime checker!')
	while True:
		i = 2  # The smallest prime number is 2
		flag = 0  # Used to mark whether it's a prime number or not
		num = int(input('n: '))
		if num == EXIT:
			break
		# If 'num' is not a prime number, then 'num' must at least have a factor less than its own value
		while i < num:
			if (num % i) == 0:
				flag = 1
				break
			i += 1
		if flag == 1:
			print(str(num)+' is not a prime number.')
		else:
			print(str(num) + ' is a prime number.')
	print('Have a good one!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
