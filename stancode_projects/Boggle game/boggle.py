"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

words = [] #words in dictionary
answer = 0 #count number of the answers
ans = [] # all answer words


def main():
	"""
	TODO:
	"""
	boggle_array = []
	i = 1
	while True:
		if i <= 4:
			boggle_line = str(input(f"{i} row of letters : "))
			if len(boggle_line) != 7:
				print(f"boggle != 7 illegal unit")
				break
			else:
				boggle = []
				for j in range(len(boggle_line)):
					if j == 0 or j == 2 or j == 4 or j == 6:
						bol = boggle_line[j].lower()
						boggle += [bol]
						#print(boggle)
				i += 1
				boggle_array.append(boggle)
		else:
			break
	read_dictionary()
	has_prefix(boggle_array)
	print(f'There are {answer} words in total')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global words
	with open(FILE, 'r') as f:
		for line in f:
			words += line.split()


def has_prefix(array):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	side_s = []
	for i in range(len(array)):
		for j in range(len(array[0])):
			ch = str(array[i][j])
			side = side_digit(i,j,side_s)
			has_prefix_helper(array, ch, ans , [], side)


def side_digit(i,j,side_s):
	if i == 0:
		if j == 0:
			side_s.append((i, (j + 1)))
			side_s.append(((i + 1), j))
			side_s.append(((i + 1), (j + 1)))
		elif j == 1 or j == 2:
			side_s.append((i, (j - 1)))
			side_s.append((i, (j + 1)))
			side_s.append(((i + 1), (j - 1)))
			side_s.append(((i + 1), (j + 1)))
			side_s.append(((i + 1), j))
		elif j == 3:
			side_s.append((i, (j - 1)))
			side_s.append(((i + 1), (j - 1)))
			side_s.append(((i + 1), j))
	elif i == 1:
		if j == 0:
			side_s.append(((i - 1), j))
			side_s.append(((i - 1), (j + 1)))
			side_s.append((i, (j + 1)))
			side_s.append(((i + 1), j))
			side_s.append(((i + 1), (j + 1)))
		elif j == 1 or j == 2:
			side_s.append(((i - 1), (j - 1)))
			side_s.append(((i - 1), j))
			side_s.append(((i - 1), (j + 1)))
			side_s.append((i, (j - 1)))
			side_s.append((i, (j + 1)))
			side_s.append(((i + 1), (j - 1)))
			side_s.append(((i + 1), j))
			side_s.append(((i + 1), (j + 1)))
		elif j == 3:
			side_s.append(((i - 1), j))
			side_s.append(((i - 1), (j - 1)))
			side_s.append((i, (j - 1)))
			side_s.append(((i + 1), j))
			side_s.append(((i + 1), (j - 1)))
	elif i == 2:
		if j == 0:
			side_s.append(((i - 1), j))
			side_s.append(((i - 1), (j + 1)))
			side_s.append((i, (j + 1)))
			side_s.append(((i + 1), j))
			side_s.append(((i + 1), (j + 1)))
		elif j == 1 or j == 2:
			side_s.append(((i - 1), (j - 1)))
			side_s.append(((i - 1), j))
			side_s.append(((i - 1), (j + 1)))
			side_s.append((i, (j - 1)))
			side_s.append((i, (j + 1)))
			side_s.append(((i + 1), (j - 1)))
			side_s.append(((i + 1), j))
			side_s.append(((i + 1), (j + 1)))
		elif j == 3:
			side_s.append(((i - 1), j))
			side_s.append(((i - 1), (j - 1)))
			side_s.append((i, (j - 1)))
			side_s.append(((i + 1), j))
			side_s.append(((i + 1), (j - 1)))
	elif i == 3:
		if j == 0:
			side_s.append((i, (j + 1)))
			side_s.append(((i - 1), j))
			side_s.append(((i - 1), (j + 1)))
		elif j == 1 or j == 2:
			side_s.append((i, (j - 1)))
			side_s.append((i, (j - 1)))
			side_s.append(((i - 1), (j - 1)))
			side_s.append(((i - 1), (j + 1)))
			side_s.append(((i - 1), j))
		elif j == 3:
			side_s.append((i, (j - 1)))
			side_s.append(((i - 1), (j - 1)))
			side_s.append(((i - 1), j))
	return side_s


def has_prefix_helper(array, current_s, ans, visited, side_s):
	global words, answer
	#print(f'array = {array}, current_s = {current_s}, ans = {ans}, visited = {visited}, side_s = {side_s}')
	if len(current_s) < 4:
		for digit in side_s:
			if digit not in visited:
				visited.append(digit)
				i = digit[0]
				j = digit[1]
				current_s += array[i][j]
				side_s = side_digit(i , j, [])
				has_prefix_helper(array, current_s, ans, visited,side_s)
				current_s = current_s[:-1]
				visited.pop()
	else:
		if current_s in words:
			if current_s not in ans:
				print(f"Found : {current_s}")
				ans.append(current_s)
				answer += 1



if __name__ == '__main__':
	main()
