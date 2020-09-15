#------------------------------
# Assignment 3
# Purpose: main.py
# Author: Penelope Chen
# References/Collaborators:
#------------------------------
from WordGuess import WordGuess

def printHeader():
    '''
    Parameters: None
    Purpose: print header
    Return: None
    '''
    header = '**************'
    print(header)
    print('Guess the Word')
    print(header)
    
def toContinue():
    '''
    Parameters: None
    Purpose: to return whether the player wants to play another round
    Return: to Continue
    '''
    TC = True
    while TC:
        #ask the user if they want to play again
        answer = input('Would you like to play again? (y/n):') 
        #if the answer is y
        if answer.lower() == 'y':
            toContinue = True
            return toContinue
        #if the answer is n
        elif answer.lower() == 'n':
            toContinue = False
            return toContinue
        
        else:
            TC  = True
            print('answer is invalid.....please enter again')
        
    
    return toContinue()

def readFile(fileName):
    '''
    Parameters: None
    Purpose: to read file and return a list containing file info
    Return: File in list
    '''    
    try:
        #open the file
        f= open(fileName, 'r')
    except Exception as myError:
        #if file has error
        print('file not valid')
        print('Exiting Program......Goodbye')
        #exit game
        quit()
    
    #split the file by line
    file= f.read().split('  ')   
    for line in file:
        aList = line.split('\n')
        
    f.close()
    
    return aList
def createDict(aList):
    '''
    Parameters: alist
    Purpose: to convert a list to a dict
    Return: aDict
    '''
    #create a new dict
    aDict = {}
    #for line in each list
    for line in aList:
        #split the line to retreive values
        line = line.split(' ')
        #capitalize the key
        key = line[0]. upper()
        #add the key and its values in the dictionary
        aDict[key] = (''.join(line[1:]))
        
    return aDict   
    
def main():
    #to Continue game initialize
    tC = True
    #ask user to input file    
    fileName = input('Enter the input filename:') 
    
    while tC:
        #read the file
        alist = readFile(fileName)
        #create a dictionary with the values in the file
        dictValues = createDict(alist)  
        #initialize the game class
        wg = WordGuess(dictValues)
        #play the game
        wg.play()
        #if the player chooses to continue
        if toContinue():
            tC = True
        #if not
        else:
            tC = False
        print('')
        
    #exiting game...
    else:
        print('Exiting program...Goodbye. ')
    

main()