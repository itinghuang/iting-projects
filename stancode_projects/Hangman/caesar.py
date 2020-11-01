"""
File: caesar.py
Name: Tina
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program produces cipher code.
    """
    """
    :param string: the word to be ciphered
    :return: result: the ciphered string
    """
    SECRET = int(input('Secret number: '))
    result = ''
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result += ALPHABET[(len(ALPHABET)-SECRET):] + ALPHABET[:(len(ALPHABET)-SECRET)] #find the complete secret code.
    string = input("What's the ciphered string? ")
    string = string.upper()
    ans = ''
    for i in range(len(string)):
        if not string[i].isalpha(): #confirm the content of string code
            ans += string[i]  #if content is not alphabet, then use original content
        else:
            finder1 = result.find(string[i])  #find the cooradinate of secret alphabet
            ans += ALPHABET[finder1]  #add the alphabet in the corresponed ALPHABET
    print('The deciphered number is ' + str(ans))




#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
