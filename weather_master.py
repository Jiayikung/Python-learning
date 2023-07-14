"""
File: weather_master.py
Name: Doris
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

# This number controls when to stop the game
EXIT = -100


def main():
	"""
	After repeatedly inputting new temperatures,
	this program allow users to find the highest, the lowest, average temperatures,
	and the number of cold days, which are days have the temperature lower than 16 Celsius.
	Also, the user can stop the game whenever inputting certain number as 'EXIT'
	"""
	print('stanCode \"Weather Master 4.0\"!')
	data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)?'))
	if data == EXIT:
		print('No temperatures were entered.')
	else:
		cold = 0
		if data < 16:
			cold += 1
		maximum = data
		minimum = data
		average = data
		total_sum = data
		count = 1
		while True:
			data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)?'))
			if data == EXIT:
				break
			if data != EXIT:
				total_sum = total_sum + data
			if data < 16:
				cold += 1
			if data > maximum:
				maximum = data
			if data < minimum:
				minimum = data
			count += 1
			average = total_sum / count
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(average))
		print(str(cold) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
