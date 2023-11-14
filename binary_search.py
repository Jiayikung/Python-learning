def main():
	lst = [3, 6, 9, 10, 11, 23, 33, 45, 66, 99]
	print(binary_search(lst, 7))
	print(binary_search(lst, 23))


def binary_search(lst, target):
	"""
	:param lst: list[int], a Python list storing integers.
	:param target: int, the value to be searched.
	:returns : bool, if target is in the lst or not.
	"""
	left_i, right_i = 0, len(lst)-1
	while True:
		mid_i = (left_i+right_i)//2
		if target == lst[mid_i]:
			return True
		elif target > lst[mid_i]:
			left_i = mid_i + 1
		else:
			right_i = mid_i - 1
		if left_i > right_i:
			return False


if __name__ == '__main__':
	main()
