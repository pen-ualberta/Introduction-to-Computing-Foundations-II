#----------------------------------------------------
# Lab 3: Connect Four class
# Purpose of class: Create a connect4 Game
# 
# Author: Penelope Chen
# Collaborators/references:
#----------------------------------------------------

import copy
class Connect4:
    def __init__(self):
        '''
        Initializes an empty Connect Four board.
        Inputs: none
        Returns: None
        '''       
        self.board = []  # list of lists, where each internal list represents a column
        self.COLS = 7    # number of columns on board
        self.ROWS = 6    # maximum number of chips that can fit in each column
        
        # initialize board with 7 empty columns
        for i in range(self.COLS):
            self.board.append([])
     
                
    def locationIsEmpty(self, col, row):
        '''
        Checks if a given location is empty, or if it contains a chip.
        Inputs:
           col (int) - column index of location to check
           row (int) - row index of location to check
        Returns: True if location is empty; False otherwise
        '''
        
        Col = self.board[col]
        
        return len(Col) <= row
    
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown along the top and the left side.
        Inputs: none
        Returns: None
        '''        
        print(' ' ,' 0  1  2  3  4  5  6' )
        alist = copy.deepcopy(self.board)
        for col in alist:
            if len(col)<= self.ROWS:
                blank= ' * '.split()
                col.extend( blank *int(self.ROWS - len(col)))         
        newList = []
        col = 0
        for row in range(self.ROWS):
            Row = self.ROWS - row -1
            rowList = []
            for col in range(self.COLS):
                rowList.append(alist[col][Row])
                col = col +1
            print(Row, '' , '  '. join(rowList))
      



    def update(self, col, chip):
        '''
        Drops the chip into the indicated column, col, as long as there is still
        room in the column.
        Inputs:
           col (int)  - column index to place chip in
           chip (str) - colour of chip
        Returns: True if attempted update was successful; False otherwise
        '''       
        #TO DO: delete pass and complete the function
        
        yChip = 'Y'
        rChip = 'R'
        Col = self.board[col]
        if len(Col) < self.ROWS:
            colEmpty = False
            if chip == yChip:
                Col.append(yChip)
                attempt = True
            elif chip == rChip:
                Col.append(rChip)
                attempt = True
            
        else:
            attempt= False
        
        return attempt
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining empty locations.
        Inputs: none
        Returns: True if the board has no empty locations (full); False otherwise
        '''
        #TO DO: delete pass and complete the function
        
        full = False
        
        for eCol in self.board:
            if len(eCol)> (self.ROWS):
                full = True
                
        return full
        
           
    def isWinner(self, chip):
        '''
        Checks whether the given player (indicated by the chip) has just won. In
        order to win, the player must have just completed a line of 4 identically
        coloured chips (i.e. that player's chip colour). That line can be horizontal,
        vertical, or diagonal.
        Inputs: 
           chip (str) - colour of chip
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        #TO DO: delete pass and complete the function
        
        win = False
        hwin = False
        vwin = False
        rdwin = False
        ldwin = False
        unit = self.board  
                
        #horizontal win
        for y in range(0, self.ROWS):
            for x in range(0, self.COLS):
                try:
                    if unit[x][y] == unit[x+1][y] == unit[x+3][y] == unit [x+2][y] == str(chip):
                        hwin = True
                except IndexError as error:
                    xwin = False
        
        #Vertical Win
        for x in range(self.COLS):
            for y in range(self.ROWS):
                try:
                    if unit[x][y] == unit[x][y+1]== unit[x][y+2] == unit[x][y+3] == chip  :
                        vwin = True
                        
                except IndexError as error:
                    xwin = False
        
        
        # Right Diagonal Win
        for x in range(self.COLS):
            for y in range(self.ROWS):
                try :
                    if unit[x][y] == unit[x+1][y+1] == unit[x+2][y+2] == unit[x+3][y+3]==str(chip):
                        rdwin = True
                except IndexError as error:
                    xwin = False     
                    
        #Left Diagonal Win
        for x in range(self.COLS):
            for y in range(self.ROWS):
                try:
                    if unit[x][y] == unit[x-1][y+1] == unit[x-2][y+2] == unit[x-3][y+3] == str(chip):
                        ldwin = True  
                except IndexError as error:
                    xwin = False     
                  
        #if any conditions apply, return win
        if ldwin== True or hwin== True or vwin ==True or ldwin == True:
            win = True
            
        return win
     

if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # a few initial tests are provided to get you started, but more tests are required
    print('**********************')
    print('TESTING Connect4 CLASS')
    print('**********************')
    BOARD_COLUMNS = 7
    BOARD_ROWS = 6
    
    
    # Test 1: 
    # start by creating empty board and checking the contents of the board attribute
    myGame = Connect4()
    print('The initial state of the game board is:')
    print(myGame.board)
    
    # Test 2:
    # are all of the locations on the board empty?
    for column in range(BOARD_COLUMNS):
        for row in range(BOARD_ROWS):
            if not(myGame.locationIsEmpty(column, row)):
                print('\nSomething is wrong with the locationIsEmpty method')
                print('Column', column, 'and row', row, 'should be empty.')
    
    
    # Test 3:
    # does the empty board display properly?
    myGame.drawBoard()  
    
    # is there a winner when no one has played?
    print('There is a winner when no one has played', myGame.isWinner('Y'))
    print('\nThere is a winner : Yellow', myGame.isWinner('Y'))
    print('\nThere is a winner : Red', myGame.isWinner('R'))
    # TO DO: write your own tests to verify that all of the methods work correctly
    
    #Test update
    print('is game full:',myGame.boardFull())
    
    if not myGame.boardFull():
        myGame.update(4,'Y')
       
        myGame.drawBoard()        
        
     
        
     
    
    print('\nThere is a winner : Yellow', myGame.isWinner('Y'))
    print('\nThere is a winner : Red', myGame.isWinner('R'))    
    
    myGame.update(3,'R')
    myGame.update(2,'R')
    myGame.update(1,'R')
    myGame.update(0,'R')     
    myGame.drawBoard()
    
    myGame.update(3,'Y')
    myGame.update(2,'R')
    myGame.update(2, 'Y')
    myGame.update(1, 'R')
    myGame.update(1, 'R')
    myGame.update(1, 'Y')
    myGame.drawBoard()
    
    print('\nThere is a winner : Yellow', myGame.isWinner('Y'))
    print('\nThere is a winner : Red', myGame.isWinner('R'))    
    