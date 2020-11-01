"""
File: similarity.py
Name: Tina
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    dna = input('Please give a DNA sequence to search:')
    dna = dna.upper() #string, to assign a spring for dna word
    match = input('What DNA sequence would you like to match:')
    match = match.upper() #string, to assign a string for match word
    maximum = 0 #int, to assign the highest possibility
    max_sequence = '' #string, to assign the sequence of highest possibility
    for i in range(len(dna)-len(match)+1):
        count = 0
        sequence = dna[i:(i+(len(match)))]
        for j in range(len(sequence)):
            if match[j] == sequence[j]:
                count += 1
        percentage = count/len(match)
        if maximum < percentage:
            maximum = percentage
            max_sequence = sequence
    print('The best match is: '+max_sequence)


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
