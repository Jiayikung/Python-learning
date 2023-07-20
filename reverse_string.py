"""
File: reverse_string.py
Name: Doris
----------------------------
The goal of this file is to 
reverse "stressed". You will 
see something cool ; )
"""


def main():
	"""
	This program reverses 'stressed'
	"""
	old_str = 'stressed'
	new_str = reverse(old_str)
	print('The reversed string of ' + old_str + ' is: ' + new_str)


def reverse(string):
	"""
	:param string: The word to be reversed
	:return result: The reversed string
	"""
	result = ''
	for i in range(len(string)):
		result = string[i] + result
	return result
	

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
