"""
File: hangman.py
Name: Tina
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    ran_word = random_word() #spring, to assign a spring for the random word
    world = ''
    for i in range(len(ran_word)):
        world += '-'
    print('The world look like' + world)
    count = 0 #int, to count wrong guess numbers
    ans = ''
    while count < N_TURNS:
        count1 = N_TURNS - count #int, to count how many times left for guessing
        your_guess = input('Your guess: ')
        your_guess = your_guess.upper()
        if not your_guess.isalpha(): #to check if guess-word is an alphabet
            print('illegal format.')
        else:
            if ran_word.find(your_guess) != -1:
                print('You are correct!')
                ans = ''
                for i in range(len(ran_word)): #check each alphabet with each alphabet in random word
                    ch = ran_word[i]
                    if ch == your_guess:
                        ans += your_guess
                    else:
                        ans += world[i]
                if ans.find('-') == -1:
                    break
                else:
                    print('The word looks like ' + ans)
                    print('You have '+str(count1) + ' guesses left.')
                    world = ans
            else:
                print('There is no '+str(your_guess))
                count += 1
                print('You have ' + str(count1) + ' guesses left.')
    if count <= N_TURNS:
        print('You win!!')
        print('The word was: ' + ans)
    else:
        print('You are completely hung :(')
        print('The word was: ' + ran_word)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
