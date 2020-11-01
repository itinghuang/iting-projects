"""
File: rocket.py
Name: Tina
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

SIZE = 3


def main():
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	n = 0
	for i in range(SIZE):
		for h in range(SIZE-n):
			print(' ', end='')
		for j in range(n+1):
			print('/', end='')
		for k in range(n+1):
			print('\\', end='')
		n += 1
		print('')


def belt():
	print('+', end='')
	for i in range(SIZE*2):
		print('=', end='')
	print('+', end='')
	print('')


def upper():
	n = 1
	for i in range(SIZE):
		print('|', end='')
		for h in range(SIZE-n):
			print('.', end='')
		for j in range(n):
			print('/\\', end='')
		for k in range(SIZE-n):
			print('.', end='')
		print('|', end='')
		print('')
		n += 1


def lower():
	n = SIZE
	for i in range(SIZE):
		print('|', end='')
		for h in range(SIZE-n):
			print('.', end='')
		for j in range(n):
			print('\\/', end='')
		for i in range(SIZE-n):
			print('.', end='')
		print('|', end='')
		print('')
		n -= 1


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()