"""
File: coin_flip_runs.py
Name: Doris
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	Solution 01 is the most optimal solution.
	"""
	"""
	Solution 01
	===========================
	The algorithm we adopted is as followed:
	Since there're at least two flips, we initially perform two sets of flips 
	and assign values to flip1 and flip2.
	Then we put in a switch to count one more runs only when the first consecutive result occurs.
	What's more, we'll keep flipping coins until the inputting number of runs equal to the ones in the game.
	"""
	print("Let's flip a coin!")
	run = int(input('Number of runs: '))
	count = 0  # Count how many runs so far
	is_in_a_row = False  # Used as a switch in the following codes

	ans = ''
	flip1 = r.choice('TH')  # The first flip. Randomly choose either 'T' or 'H'
	flip2 = r.choice('TH')  # The Second flip.
	ans = ans + flip1 + flip2
	if flip1 == flip2:
		count += 1

	while count != run:  # Keep looping until the inputting number of runs equal to ones in the game
		flip1 = flip2
		flip2 = r.choice('TH')
		ans += flip2
		if flip1 == flip2:
			if not is_in_a_row:  # Only run through the codes below when the first consecutive result occurs
				count += 1
				is_in_a_row = True  # Turn off the switch to prevent counting subsequent consecutive results
		else:
			is_in_a_row = False
	print(ans)



	"""
	Solution 02
	===========================
	The algorithm we adopted is as followed:
	First, we check if there's any consecutive result in the first two flips.
	Then we check if there's any 'THH' or 'HTT' in the rest of the flips.
	"""
	# print("Let's flip a coin!")
	# run = int(input('Number of runs: '))
	# ans1 = ''  # The string tracking each flip
	# ans2 = ''  # The string that used to identify whether any 'run' occurred
	# count = 0  # Count how many runs so far
	# # Check if there's any consecutive result in the first two flips
	# for i in range(2):
	# 	flip = r.choice('TH')
	# 	ans1 = ans1 + flip
	# if 'HH' in ans1:
	# 	count += 1
	# 	ans2 = 'H'
	# elif 'TT' in ans1:
	# 	count += 1
	# 	ans2 = 'T'
	# else:
	# 	ans2 = ans1
	#
	# # Check if there's any 'THH' or 'HTT' in the rest of the flips
	# while True:
	# 	if count == run:
	# 		break
	# 	flip = r.choice('TH')  # Randomly choose either 'T' or 'H'
	# 	ans1 = ans1 + flip
	# 	ans2 = ans2 + flip
	# 	if 'THH' in ans2:
	# 		count += 1
	# 		ans2 = 'H'
	# 	elif 'HTT' in ans2:
	# 		count += 1
	# 		ans2 = 'T'
	# print(ans1)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
