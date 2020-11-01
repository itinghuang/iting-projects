"""
File: complement.py
Name: Tina
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    TODO:
    """
    dna = input("Please give me a DNA strand and I'll find the complement:")
    dna1 = dna
    dna = dna.upper()
    ans = build_complement(dna)
    print('the complement of '+dna1 + ' is '+ans)


def build_complement(dna):
    ans = ''
    for nucleotide in dna:
        if nucleotide == 'A':
            ans += 'T'
        elif nucleotide == 'T':
            ans += 'A'
        elif nucleotide == 'C':
            ans += 'G'
        else:
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
