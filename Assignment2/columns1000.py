#----------------------------------------------------
# Columns1000: Assignment 2
# Purpose of code: Creat ADTS to support 
# assignment 2 
# Author: Penelope Chen (Final)
# Collaborators/references:
#----------------------------------------------------

from queues import CircularQueue


class Tile:
    def __init__(self, initValue):
        '''
        Parameters: initial value
        Purpose:initializes the tile and assigns the value of the tile
        Reutrns: None
        '''
        validValues= [2,4,8,16,32,64,128,256,512]
        
        #if the values are not valid
        
        if initValue not in validValues:
            raise Exception('value not valid')
        
        self.value = initValue
        
    
    def getValue(self):
        '''
        Parameters: None
        Purpose: To retrieve the value of the tile
        Returns: None
        '''
        
        return self.value
    
    def doubleValue(self):
        '''
        Parameters: None
        Purpose: To double the value of the tile
        Returns: None
        '''
        self.value = self.value *2
        
    
    def __eq__(self, tile2):
        '''
        Parameters: tile 2
        Purpose: to find out if the value of the two tiles equal each other
        Returns: isEqual( boolean)
        '''
        isEqual = False
        if tile2 != None:
            if self.value == tile2.getValue():
                isEqual = True            
        
            
        return isEqual
            
    
    def __str__(self):
        '''
        Parameters: None
        Purpose: convert the tile value into string format
        Returns: the tile value in string format
        '''
        
        strValue = '<' + str(self.value) + '>'
        
        return strValue
        
    
    
class Columns1000:
    def __init__(self, numColumns, colHeight):
        '''
        Creates an empty Columns 1000 game board, and initializes the game's
        score to 0.
        
        Inputs:
           numColumns (int) - number of columns on game board. 
                              Must be at least one column, and a max of 10.
           colHeight (int) - number of rows in each column on game board.
                             Must be at least one row, and a max of 20.
        
        Returns: None
        '''
        #################
        # TO DO: add asserts to check that inputs are valid
        #################
        
        # the conditions for number of rows and columns
        maxColumns  = 10
        maxHeight = 20
        minColumns = 1
        minHeight = 1
        
        # initiate chart if conditions are met
        if numColumns >= minColumns and numColumns <= maxColumns:
            self.__COLUMNS = numColumns
        
        if colHeight >= minHeight and colHeight <= maxHeight:
            self.__ROWS = colHeight
            
        self.__board = []
        self.__score = 0
        
        #initiate board
        for c in range(self.__COLUMNS):
            self.__board.append([])
            for r in range(self.__ROWS):
                self.__board[c].append(None) 
    
                
    def getScore(self):
        '''
        Parameters: None
        Purpose: to retreive the score
        Return: the score
        '''
        
        return int(self.__score)
    
    def drawColumns(self):
        '''
        Parameters: None
        Purpose: to draw each column as a graph
        Return: boardlist
        '''
        
        # to printout  '*' instead of None
        i = 0 
        board = self.__board.copy()
        printBoard = []
        for col in board:
            colList = []
            for i in range(len(col)):
                if col[i] == None:
                    colList.append('*')
                else:
                    value = col[i].__str__()
                    colList.append(value)
            printBoard.append(colList)
        
        
        # to create a new list to print the new columns and rows in the right format         
        j= 0
        k = 0
        boardList = []
        for k in range(self.__ROWS):
            rowList = [str(k)]
            for j in range(self.__COLUMNS):
                rowList.append('{:^7}'.format(printBoard[j][k]))
            boardList.append(rowList)
            
        #reverse the row numbers to the correct format
        boardList.reverse()
        #to print the number of columns at the bottom
        colList = [' ']
        for n in range(self.__COLUMNS):
            colList.append('{:^7}'.format(str(n)))            

        #print each list as a string
        for col in boardList:
            print(''.join(col))
        
        #print the bottom numbers as a string
        print(''.join(colList))
        
        
    
    def columnFull(self, col):
        '''
        Parameters: col(int)
        Purpose: to see if a column is full
        Return : a boolean to see if a column is full
        '''
        #initial value of isFull
        isFull = False
        #the column selected
        column = self.__board[col]
        
        #see the numbers of values in the column is filled
        i = 0
        nRowFilled = 0
        maxROW = self.__ROWS
        for i in range (self.__ROWS):
            if column[i] != None:
                nRowFilled+= 1
                
        #if the number of values is equal to the number of rows
        if nRowFilled == maxROW:
            isFull = True
            
        return isFull
    
    def placeTile(self, col, tile):
        '''
        Parameters: col(str), tile
        Purpose: to place a tile in the selcted column
        Return: Row(int) where the tile was dropped
        '''
        #retreiving a list of the number of columns
        listofCols = []
        for n in range(0, len(self.__board)):
            listofCols.append(n)
            
        #convert col string to int
        colIndex = int(col)
        #if the column number is valid
        if colIndex in listofCols:
            indexIn = True
        #assertion error raised if column not valid
        assert indexIn == True, 'Invalid column chosen'
    
        #condition if column is full
        columnFull = self.columnFull(colIndex)
        
        #find the list containing the column's values
        column = self.__board[colIndex]
        
        #if full, raise exception
        if columnFull:
            raise Exception('Cannot place tile in that column')
        
        row = 0
        tilePlaced = False
        
        #if if row exist, add tile to the smallest row
        while row < self.__ROWS and not tilePlaced:
            if column[row] == None:
                column[row] = tile
                tilePlaced = True
            elif column[row] != None:
                tilePlaced = False
                row+=1        
                
        return row       
    
    def mergeTiles(self, col, row):
        
        '''
        Parameters: col(int), row(int)
        Purpose: to merge the values at [col][row] and [col][row-1]
        Return: 
               True - if the values sucessfully merged 
               Otherwise - exception raised
        '''
        
        #finding the values in the column
        column = self.__board[col]
        
        noneAbove = False
        oneBelow = False
        
        #if there is an object in the row above except for the most upper row
        if row< self.__ROWS-1: 
            if column[row+1] == None:
                noneAbove = True
        elif row == self.__ROWS-1:
            noneAbove = True
        
        #if there is an object below except for the lowest row
        if row == 0:
            oneBelow = True
        elif row > 0 :
            if column[row-1] != None:
                oneBelow = True
            
        # conditions need to be met for merge to continue    
        assert column[row] != None and noneAbove == True and oneBelow == True
        
        # 2 tile merge
        tile1 = column[row]
        tile2 = column[row-1]
        #if the values are equal
        if tile1.__eq__(tile2):
            # the object at row becomes None
            column[row] = None
            #object in the row below doubles
            column[row-1].doubleValue()
            #the score increases by adding the doubled value
            self.__score = self.__score + (column[row-1].getValue())
            mergeSucceed = True
        else:
            raise Exception('Cannot merge tiles')
        
        return mergeSucceed
            
    
    def isWon(self):
        '''
        Parameters: None
        Purpose: to find out if the win condtition is met
        Return: isWon(bool)
        '''
        isWon = False
        if isWon == False:
            for col in self.__board:
                for tile in col:
                    if tile != None and tile.getValue()> 1000:
                        isWon = True
        return isWon
    
    def isFull(self):
        '''
        Parameters: None
        Purpose: to find out if the chart is full
        Return: isFull(bool)
        '''
        
        isFull = True
        for col in self.__board:
            for tile in col:
                if tile == None:
                    isFull = False
        
        return isFull
                
    
    
class Pile:
    def __init__(self, valuesStr):
        '''
        Parameters: list of str values
        Purpose: Creates an ordered pile of tiles based on the list of string values provided
        Return: None
        '''
        #ValuesStr
        #initialize the queue size
        n = len(valuesStr)
        cq = CircularQueue(n)
        
        
        #push each tile into the queue
        for value in valuesStr:
            tile = Tile(int(value))
            cq.enqueue(tile)
            
        #initialize attribute     
        self.pile = cq
        
    def nextTile(self):
        '''
        Parameters: None
        Purpose: to retrieve the next tile in the pile
        Return: nextTile
        '''
        
        nextTile = self.pile.dequeue()
        
        return nextTile
    
    def isEmpty(self):
        '''
        Parameters: None
        Purpose: to find out whether the pile is empty
        Return: isEmpty(bool)
        '''
        isEmpty = False
        if self.pile.isEmpty():
            isEmpty = True
        
        return isEmpty 
            
    
    def __str__(self):
        '''
        Parameters: None
        Purpose: to print all the tiles in the pile in str form
        Return: a string of all the tiles in the pile
        '''
        
        return self.pile.__str__()
    

if __name__ == '__main__':
    # Delete pass (below) and test your classes here.
    # Be sure to leave these tests here so that you can receive marks for them.
    
    '''
    #Pile Class Test
    #initialize the pile
    pile = Pile([2,4])
    
    #seeing all the tiles in the pile
    print(pile)
    
    #testing the next tile method
    print('nextTile:', pile.nextTile())
    #testing the isEmpty method
    print('is pile empty', pile.isEmpty())
    print('nextnextTile:', pile.nextTile())
    print('is pile empty', pile.isEmpty())
    '''
    
    
    '''
    
    #COLUMN1000 Class Test
    
    board = Columns1000(7,4)
    board.drawColumns()
    print('isColumnFull?', board.columnFull(2))
    tile = Tile(256)
    print(tile)
    tile2 = Tile(512)
    print('which row? did tile go?', board.placeTile(6,tile))
    #print('which row? did tile go?', board.placeTile(3,tile))
    board.drawColumns() 
    print('which row? did tile go?', board.placeTile(6,tile))
    board.drawColumns() 
    print('')
    
    print(board.mergeTiles(6, 1))
    board.drawColumns() 
    print('isWon?', board.isWon())
    
    
    print(board.placeTile(6,tile2))
    print(board.mergeTiles(6, 1))
    
    
    board.drawColumns() 
    print('isWon', board.isWon())
    
    print('is board full?', board.isFull())

    print('which row? did tile go?', board.placeTile(6,tile))
    print('which row? did tile go?', board.placeTile(6,tile))
    print('which row? did tile go?', board.placeTile(6,tile))
    print('which row? did tile go?', board.placeTile(5,tile))
    print('which row? did tile go?', board.placeTile(5,tile))
    print('which row? did tile go?', board.placeTile(5,tile))
    print('which row? did tile go?', board.placeTile(5,tile))
    print('which row? did tile go?', board.placeTile(4,tile))
    print('which row? did tile go?', board.placeTile(4,tile))
    print('which row? did tile go?', board.placeTile(4,tile))
    print('which row? did tile go?', board.placeTile(4,tile))
    print('which row? did tile go?', board.placeTile(3,tile))
    print('which row? did tile go?', board.placeTile(3,tile))
    print('which row? did tile go?', board.placeTile(3,tile))
    print('which row? did tile go?', board.placeTile(3,tile))
    print('which row? did tile go?', board.placeTile(2,tile))
    print('which row? did tile go?', board.placeTile(2,tile))
    print('which row? did tile go?', board.placeTile(2,tile))
    print('which row? did tile go?', board.placeTile(2,tile))
    print('which row? did tile go?', board.placeTile(1,tile))
    print('which row? did tile go?', board.placeTile(1,tile))
    print('which row? did tile go?', board.placeTile(1,tile))
    print('which row? did tile go?', board.placeTile(1,tile))
    print('which row? did tile go?', board.placeTile(0,tile))
    print('which row? did tile go?', board.placeTile(0,tile))
    print('which row? did tile go?', board.placeTile(0,tile))
    #print('which row? did tile go?', board.placeTile(0,tile))
    
    board.drawColumns() 
    print('is board full?', board.isFull())
    
    '''
    
    '''
    #Tile Class Test
    #initialize tile test
    tile1= Tile(2)
    tile2 = Tile(2)
    tile3 = Tile(2)
    
    #retreiving value of tile
    print(tile1.getValue())
    
    #double the value of tile
    tile1.doubleValue()
    print(tile1 .getValue())
    
    #equating two tiles by their values
    print(tile1.__eq__(tile2))
    print(tile2.__eq__(tile3))
    
    #turning the tile to a string
    print(tile1.__str__())
    '''
    
    
