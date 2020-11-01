"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

words = [] # this is the words in the dictionary

def main():
    read_dictionary()
    while True:
        s = str(input("Find anagrams for : "))
        if s != EXIT:
            find_anagrams(s)
        else:
            break


def read_dictionary():
    global words
    with open(FILE, 'r') as f:
        for line in f:
            words += line.split()


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    ans = find_anagrams_helper(s, '', [], [])
    print(f'{len(ans)} anagrams: {ans}')


def find_anagrams_helper(s,current_s, ans, visited):
    global words
    if len(current_s) == len(s):
        if current_s in words:
            if current_s not in ans:
                print(f"Found:{current_s}")
                print(f"Searching...")
                ans.append(current_s)
    else:
        for i in range(len(s)):
            if i not in visited:
                visited.append(i)
                current_s += s[i]
                #if has_prefix(words,current_s):
                #print(f"current_s:{current_s}")
                find_anagrams_helper(s, current_s, ans, visited)
                current_s = current_s[:-1]
                visited.pop()
    return ans


def has_prefix(words, sub_s):
    """
    :param sub_s:
    :return:
    """
    for word in words:
        if word.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
