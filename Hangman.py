import pdb
#import random
#from itertools import count

def ContinueI():
    pass

def lettercheck(guess):
    if(len(guess)>1):
        return 1
    else:
        return 0

Wordlist = 'Lemon Asphyxiation Harish Girish Rikuo Ranma Kiyara'
secret = 'Asphyxiation'
for i in secret:
    print('_', end = ' ',)
print('It is a form of torture and death')

#List of var for guessing the secret word
chances = len(secret) + 2
letterg = ''
flag = 0
correct = 0

while chances!=0 and flag == 0:
    chances -= 1
    guess = str(input('Enter the letter: '))
    if(lettercheck(guess) == 0):
        print()
    else:
        continue

    if not (guess.isalpha()):
        print('Enter only alphabet')
        continue
    elif len(guess) > 1:
        print('Enter a single letter')
        continue
    elif guess in letterg:
        print ('You have already guessed that letter')
        continue

    if guess in secret:
        k=secret.count(guess)
        for j in range(k):
            letterg += guess
    else:
        print('Try again, Saviour')

    for char in secret:
        if char in letterg and (len(letterg)!=len(secret)):
            print(char, end = ' ')
            correct += 1
        elif len(letterg) == len(secret):
                flag = 1
                print ("The word is {}" .format(secret), "\nYou Won")
                exit()
    if chances <= 0 and (len(letterg) != len(secret)):
        print("The poor soul mourns in agony")
        print ('The secret word is {}' .format(secret))
        exit()