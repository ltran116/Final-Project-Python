#Lisa Tran
from random import randint
from idlecolors import *
from wordbank import *
done = False
response = input('Welcome to Wordle! Is this your first time playing? [Y or N]')
if response.lower() == 'y':
    printc(black('Allow me to explain how it works!'))
    printc(black('The system will prompt you to input a 5 letter word'))
    printc(black('The word will be compared to a random word in the word bank'))
    printc(black('Your goal is to match the word in the word bank'))
    printc(black('The system will show you which letters in the word you entered are correct'))
    printc(green('This color shows that the letter is correct and in the right place'))
    printc(orange('This color shows that the letter is somewhere in the word but is in the wrong place'))
    printc(black('This color shows that the letter does not belong in the word'))
    printc(black('You only get 6 guesses so make them count!'))
    printc(black('Have fun and happy guessing!'))
    printc(black("------------===+()+===------------"))
else:
    printc(black('Oh goodie a returnee!'))
    printc(black('Have fun!'))
while not done:
    letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    r1 = randint(0, 26)
    r2 = randint(0, len(alpha[r1]))
    word = alpha[r1][r2]
    guess = 'nothing'
    numGuess = 0
    #print(word)
    while guess != word and numGuess < 6:
        guess = input('\t  5 letter word: ')
        numGuess += 1
        while len(guess) != 5:
            printc(red('invalid guess'))
            guess = input('\t  5 letter word: ')
        for i in range(len(word)):
            if guess[i].lower() == word[i]:
                printc(green(guess[i]),end=' ')
            elif guess[i].lower() in word:
                printc(orange(guess[i]),end=' ')
            else:
                printc(black(guess[i]),end=' ')
        for j in range(len(guess)):
            if guess[j] in letter:
                letter.remove(guess[j])
        print('\n\t  Unused letters: ', end=' ')
        for letters in range(len(letter)):
            print(letter[letters], end = ' ')
        print()
        print('----==+',numGuess,'of 6 guesses used +==----')
        if guess.lower() == word:
            print('This word took you', numGuess,'tries!')
            print('The word was', word)
            again = input('Would you like to play again?')
            if again[0].lower == 'y':
                done = False
    if guess.lower() != word:
        print('Better luck next time!')
        print('The word was', word)
        again = input('Would you like to play again? [Y or N]')
        if again[0].lower() == 'y':
            done = False
            printc(black("------------===+()+===------------"))
        elif again[0].lower() == 'n':
            done = True
            printc(black("------------===+()+===------------"))
print("Hope you had fun playing!")
