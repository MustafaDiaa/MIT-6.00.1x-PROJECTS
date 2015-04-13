import random
import string
WORDLIST_FILENAME = "C:/Users/lenovo/words.txt"

########################################
def getGuessedWord(secretWord, lettersGuessed):
    ans = ''
    for x in range(0, len(secretWord)):
        if secretWord[x] in lettersGuessed:
            ans += secretWord[x]
            
        else:
            ans += '_ '
    return ans
########################################

def loadWords():
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print len(wordlist), "words loaded."
    return wordlist
########################################

def chooseWord(wordlist):
    return random.choice(wordlist)
########################################

def getAvailableLetters(lettersGuessed):
    letters = []
    ans = ''
    for n in range(97, 123):
        letters += chr(n)

    for n in range(0, len(letters)):
        if letters[n] not in lettersGuessed:
            ans += letters[n]
    return ans
########################################

wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
lettersGuessed = []
tries = 8
x = ''
oldGuess = []
########################################

print 'Welcome to the game, Hangman!'
print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'

while True:
    print '-------------'
    print 'You have ' + str(tries) + ' guesses left.'
    letters = ''
    for n in range(97, 123):
        letters += chr(n)
    print 'Available letters: ' + getAvailableLetters(lettersGuessed),
    oldGuess += x
    x = raw_input('Please guess a letter: ').lower()
    lettersGuessed += x
    ans = getGuessedWord(secretWord, lettersGuessed)
    if (x in oldGuess):
        print "Oops! You've already guessed that letter: " + ans
    elif (x in secretWord) and (x not in oldGuess):
        print 'Good guess: ' + ans
    elif x not in secretWord:
        tries -= 1
        print 'Oops! That letter is not in my word: ' + ans
        if tries < 1:
            print 'Sorry, you ran out of guesses. The word was ' + secretWord
            break
    if ans == secretWord:
        print 'Congratulations, you won!'
        break
########################################
