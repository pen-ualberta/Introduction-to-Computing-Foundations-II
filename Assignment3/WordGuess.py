#------------------------------
# Assignment 3
# Purpose: WordGuess.py
# Author: Penelope Chen
# References/Collaborators:
#------------------------------

import random
from LinkedLists import SecretWord, GuessedLetters

class WordGuess:

    def __init__(self, wordDic):
        '''
        Parameters: wordDic
        Purpose: Initialize attributes
        Return: None
        '''
        self.__wordDic = wordDic
        self.__guessedLetters = GuessedLetters()
        self.__maxWrong = 6
        self.__wrongGuesses = GuessedLetters()

    def chooseSecretWord(self):
        '''
        Parameters: None
        Purpose: return a random secret word
        Return: random word
        '''
        
        word = random.choice(list(self.__wordDic))
        
        return word.upper()


    def getGuess(self):
        '''
        Parameters: None
        Purpose: asks the player for a valid entry
        Return: Valid Letter
        '''
        gLetters = self.__guessedLetters
        valid = False
        
        while not valid:
            entry = input('Enter a character that has not been guessed or * for a hint:')
            #if the entry is a letter in alphabet
            if entry == '*':
                valid = True
            elif entry.isalpha():
                entry = entry[0].upper()
                if not gLetters.checkIfGuessed(entry):
                    gLetters.addGuess(entry)
                    valid = True
                else:
                    print('Invalid guess: you have already guessed this character')
                    valid = False
            else:
                print('Invalid entry. Must be a letter or *')                
                valid = False

        return entry
    
    def play(self):
        '''
        Parameters: None
        Purpose: to play the game
        Return: None
        '''
        #initialize secret word
        sWord= SecretWord()
        #choose a word
        word = self.chooseSecretWord()
        wrongGuesses = self.__wrongGuesses
        #set the secret word
        sWord.setWord(word)
        maxWrong = self.__maxWrong
        gLetters = self.__guessedLetters
        print('A secret word has been randomly chosen!')
        print('You have ', maxWrong, ' chances remaining.')
        print('Word Guess Progress: ', end = '')
        sWord.printProgress()
        print('Wrong guesses:', wrongGuesses)
        wrong = 0
        #if wrong is less than max wrong and word is not solved
        while wrong< maxWrong and not sWord.isSolved():
            print('')
            #get guess
            guess = self.getGuess()
            #if guess is hint
            if guess == '*':
                #retrieve hint
                hint= self.__wordDic[word]
                print('Hint: ', hint)
                print('You have ', maxWrong- wrong, ' chances remaining.')
                print('Word Guess Progress: ', end = '')
                sWord.printProgress()                
                print('Wrong guesses:', wrongGuesses)
            #if able to update 
            elif sWord.update(guess):
                #if solved
                if sWord.isSolved():
                    print('You solved the puzzle! ')
                    print('The secret word was: ', word)   
                #if not solved
                else:
                    print('You have ', maxWrong- wrong, ' chances remaining.')
                    print('Word Guess Progress: ', end = '')
                    sWord.printProgress()                
                    print('Wrong guesses:', wrongGuesses)   
            #if not able to update
            elif not sWord.update(guess):
                #add guess in guessed words
                wrongGuesses.addGuess(guess)
                wrong+=1
                #if max wrong is reached and not solved
                if wrong == maxWrong and not sWord.isSolved():
                    #sort the guesses by alphabet
                    wrongGuesses.sortGuesses()
                    print('Round over!')
                    print('The secret word was: ', word)
                    print('Wrong guesses in alphabetical order:', wrongGuesses) 
                #if max wrong not reached
                else:
                    print('You have ', maxWrong- wrong, ' chances remaining.')
                    print('Word Guess Progress: ', end = '')
                    sWord.printProgress()                
                    print('Wrong guesses:', wrongGuesses)                   
                  
    
    
    
if __name__ == '__main__':
    # test your WordGuess class here
    wd = WordGuess({'apple': 1, 'pear': 2, 'orange': 2,})
    #print(wd.chooseSecretWord())
    wd.play()
    #wd.getGuess()
    
