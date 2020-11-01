"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""

largest_digit = 0

def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	global largest_digit
	find_digit = 0
	if n >= 0:
		if n % 10 > largest_digit:
			largest_digit = n % 10
		if n // 10 == 0:
			find_digit = largest_digit
			largest_digit = 0
			return find_digit
		else:
			return find_largest_digit(n//10)
	else:
		n = -n
		if n % 10 > largest_digit:
			largest_digit = n % 10
		if n // 10 == 0:
			find_digit = largest_digit
			largest_digit = 0
			return find_digit
		else:
			return find_largest_digit(n//10)







if __name__ == '__main__':
	main()
