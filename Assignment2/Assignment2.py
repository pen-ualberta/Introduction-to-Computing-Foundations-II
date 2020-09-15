#----------------------------------------------------
# Assignment 2: Columns 1000
# Purpose of code: Create the game Columns 1000
# Author: Penelope Chen (Final)
# Collaborators/references:
#----------------------------------------------------

from columns1000 import Tile
from columns1000 import Columns1000
from columns1000 import Pile

def inputValidFile():
    '''
    Parameters: None
    Purpose: ask the user for a valid file input
    Return: fileName
    '''
    validInput = False
    print('Setting up new game...')
    
    #continue if the valid input is not inputted, try again for another file
    while not validInput:
        try:
            fName = input('Enter name of text file to initialize pile of tiles:')
            f= open(fName, 'r')
            f.close()
        #when a file can not be found    
        except IOError as myError:
            validInput = False
            print('Error with file: No such file or directory')
        
        else:
            validInput = True
    
    return fName


def readFile():
    '''
    Parameters: fileName
    Purpose: to read the contents of file and convert them into a list
    Return: a list of values
    '''
    fName = inputValidFile()
    #open the file
    file = open(fName, 'r')
    vList = file.read().splitlines()
    #split the first row and column
    vList[0] = vList[0].split(',')
    file.close()
    
    return vList

def initBoard(vList):
    '''
    Parameters: list of values
    Purpose: initialize board
    Return: board
    '''    
    nCol = int(vList[0][0])
    nRow = int(vList[0][1])
    #initialize board
    board = Columns1000(nCol, nRow)
        
    return board

    
def initPile(vList):
    '''
    Parameters: list of values
    Purpose; Initialize pile of tiles
    Return: queue of the tiles
    '''

    tileValues = vList[1:]
    
    #initialize pile
    pile = Pile(tileValues)
    
    return pile    


def gameInited(listofValues):
    '''
    Parameters: list of Values
    Purpose: to initialize game and handle exceptions
    Return: game initialized (bool)
    '''
    
    gameInit = False
    
    #while the game cannot be initialized, continue
    while not gameInit:
        try :
            #try to initialize board and pile
            board = initBoard(listofValues)
            pile = initPile(listofValues) 
        #handle exceptions
        except Exception as myError:
            print('Sorry, the values in this file are not valid....restarting new game')
            listofValues = readFile()
            gameInit = False
        else:
            gameInit= True

    return [gameInit, listofValues]   


def validColChosen(board, tile):
    '''
    Parameters: board, tile
    Purpose: to see if a valid column is chosen and handle exceptions
    Return: row, col
    '''
    
    colValid = False
    #while a valid column is not chosen
    while not colValid:
        try:   
            #try finding a valid column for the tile to be placed in
            col = input('Which column would you like to place, ' + tile.__str__() +' in?')
            row = board.placeTile(col, tile)
            board.drawColumns()    
        #handle any exceptions
        except Exception:
            print('Cannot place tile in that column')
        else:
            colValid = True
    #return the row and column number that the tile was placed in           
    return [int(col),row]
    
def validMerge(board, pile, col, row):
    '''
    Parameters: board, pile, col, row
    Purpose: to merge tiles and handle exceptions
    Return: the next tile
    '''
    
    try:
        # while board can continue merging tiles
        while board.mergeTiles(col, row):
            print('Merging Tiles......')
            print('')
            board.drawColumns()
            #try merging the row below
            row = row - 1
    except Exception as myError:
        #to pass the exception
        x = 'None'
    
    
def gameContinue(deci):
    '''
    Parameters: decision input
    Purpose: to return a bool and ask if the user wants to restart game
    Return: toContinue(bool)
    '''
    # valid options
    validOptions = ['Y', 'N']
    
    #continue asking till valid input
    while deci.upper() not in validOptions:
        print('invalid choice')
        deci = input('Do you want to play another game? (Y/N)')
        
    #if yes is chosen, continue    
    if deci.upper() == 'Y':
        toContinue = True
    #if no is chosen, stop game
    elif deci.upper() == 'N':
        print('Thanks for playing')
        toContinue = False
        

    return toContinue

def printScore(board):
    '''
    Parameters: board
    Purpose: print score
    Return; None
    '''
    print('----------')
    print('Points', board.getScore())
    print('----------')

def game():
    '''
    Parameters: None
    Purpose: to play game
    Return: decision to continue
    '''
    #retreive the list of values from file
    listofValues = readFile()
    gameValues = gameInited(listofValues)
    gameInitiated = gameValues[0]
    # if game was able to initiate with valid values
    if gameInitiated:
        listofValues = gameValues[1]
        board = initBoard(listofValues)
        pile = initPile(listofValues)
        board.drawColumns()
        tile = pile.nextTile()
        #while the game ending conditions are not met
        while not pile.isEmpty() and not board.isFull() and not board.isWon():
            #find the row and col of the tile place
            rcVal = validColChosen(board, tile)            
            col = rcVal[0] 
            row = rcVal[1]
            #merge tiles
            #retrieving the next tile
            validMerge(board, pile, col, row)
            tile = pile.nextTile()
            printScore(board)
            # if the board is full and is not won
        if board.isFull() and not board.isWon():
            print('Game over - cannot play tiles in any column. Final Score: ', board.getScore())
            decision = input('Do you want to play another game? (Y/N)')
        # if the board has met the isWon condition
        elif board.isWon():
            print('WINNER! Final Score:', board.getScore())
            decision = input('Do you want to play another game? (Y/N)')  
        #if there are no more tiles in the pile
        elif pile.isEmpty():
            print('Game over - no more tiles to play. Final Score:', board.getScore())
            decision = input('Do you want to play another game? (Y/N)')  
    
    return decision
def main():
    
    #initial decision to start playing
    decision = 'Y'
    
    #while the decision to play remains yes
    while gameContinue(decision):
        #play the game
        decision = game()

main()