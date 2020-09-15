#------------------------------
# Assignment 3
# Purpose: LinkedLists.py
# Author: Penelope Chen
# References/Collaborators:
#------------------------------

from Node import Node

class LinkedList:

    def __init__(self):
        self.__head = None
        self.__size = 0

    def isEmpty(self):
        return self.__head == None

    def length(self):
        return self.__size

    def add(self, item):
        temp = Node(item, None)
        temp.setNext(self.__head)
        self.__head = temp
        self.__size += 1

    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
            index = -1
        return index

    def remove(self, item):
        current = self.__head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.__head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.__size -= 1
        return found

    def append(self, item):
        temp = Node(item, None)
        if self.__head == None:
            self.__head = temp
        else:
            current = self.__head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(temp)
        self.__size += 1
        
    def insert(self,pos,item):
        # inserts the item at pos
        # pos should be a positive number of type int
        assert isinstance(pos,int),'position must be of type int'
        assert pos >= 0,'position must be a valid number in the range'
        
        if pos == 0:  # insert at the start of list
            self.add(item)
        elif pos >= self.__size : #insert at end of list
            self.append(item)
        else: # insert in the middle of list
            temp = Node(item,None)
            current = self.__head
            previous = None
            index=0
            while (current != None):
                previous = current
                current = current.getNext()
                index=index+1
                if pos==index:
                    previous.setNext(temp)
                    temp.setNext(current)
            self.__size = self.__size + 1 
        
    def pop(self):
        current = self.__head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        if previous == None:
            self.__head = None
        else:
            previous.setNext(None)
        self.__size -= 1
        return current.getData()

    def getHead(self):
        return self.__head
    

class SecretWord:

    def __init__(self):
        '''
        Parameters: None
        Purpose: initialize secretword and its attributes
        Return: None
        '''
        
        self.__wordLinkedList = LinkedList()
        self.__numVisible = 0

    def setWord(self, word):
        '''
        Parameters: word(str)
        Purpose: to capitalize each letter in each node of the linked list
        Returns: None
        '''
        
        #splits the word into a list
        word = list(word)
      
        for letter in word:
            #capitalize each letter
            letter = letter.upper()
            #add the cap letter to node
            self.__wordLinkedList.append(letter)
            

    def isSolved(self):
       # TO DO: delete pass and complete the method
        '''
        Parameters: None
        Purpose: to find if the word has been found
        Returns: True if all letters were guessed, False otherwise
        '''
        
        solved  = False
        
        # if the number of visible 
        if self.__numVisible == self.__wordLinkedList.length():
            solved = True
            
        return solved

    def update(self, guess):
        '''
        Parameters: guess(str)
        Purpose: to update if a letter should be visible
        Return: True if at least one letter updates, False otherwise
        '''
        #letters of the linked list
        word = self.__wordLinkedList
        #to tranverse, retreive head
        current = word.getHead()
        found = False
        # while the current is not None
        while current != None:
            #if  the current's data is equal to guess
            while current!= None and current.getData() == guess:
                found = True
                #set the current to visible
                current.setIsVisible(True)
                # continue to transverse to find if any other letters match
                current = current.getNext()
                self.__numVisible+= 1
            else:
                if current!= None:
                    current = current.getNext()
                elif current == None:
                    return found
                    
        
        return found

    def printProgress(self):
        '''
        Parameters: None
        Purpose: to print the current status of secret word
        Return: None
        '''
        word = self.__wordLinkedList
        current = word.getHead()
        
        #create a new list
        printList = []
        while current!= None:
            #if the node is set to visible
            if current.getIsVisible():
                letter = current.getData()
                printList.append(letter)
                #transverse to next node
                current = current.getNext()
            else:
                printList.append('_')
                #transverse to next node                
                current = current.getNext()
                
        #print the list as a string
        print(' '.join(printList))
        

    def __str__(self):
        '''
        Parameters: None
        Purpose: to return list as string
        Return: None
        '''
        output = ""
        current = self.__wordLinkedList.getHead()
        while current != None:
            output += current.getData()
            current = current.getNext()
        return output
    
    
class GuessedLetters:
    
    def __init__(self):
        '''
        Parameters: None
        Purpose: initialize the class
        Reuturn: None
        '''
        self.__guessedLinkedList = LinkedList()
        
    def checkIfGuessed(self, guess):
        '''
        Parameters: guess(str)
        Purpose: checks if guess was already registered as incorrect
        Return: True if guess in guessedList, False otherwise
        '''
        guessed = False
        gList = self.__guessedLinkedList
        # current set to head
        current= gList.getHead()        
        # if the list is not empty or the head equals to None
        while not gList.isEmpty() and current!= None:
            # if guess is in list, set guessed to True
            if current.getData() == guess:
                guessed  = True
                # get next element in list
                current = current.getNext()
            else:
                # get next element in list                
                current = current.getNext()
                
        return guessed
        
        
    def addGuess(self, guess):      
        '''
        Parameters: guess
        Purpose: to add guess to the beginning of guessed List
        Return: True if guess is added, False otherwise
        '''
        added = False
        gList = self.__guessedLinkedList
        
        #if the letter has not been already guessed
        if not self.checkIfGuessed(guess):
            gList.add(guess)
            added = True
        
        return added
        
    
    def sortGuesses(self): 
        '''
        Parameters: None
        Purpose: to sort guesses in (A-Z) order (insertion sort)
        Return: None
        '''
        gList = self.__guessedLinkedList
        current = gList.getHead()              
        
        #if the current node is not empty
        while current!= None :
            #set temporary letter
            temp = current.getData()
            #if the letter is bigger than the element in the next node
            while current!= None and current.getNext()!= None and temp > current.getNext().getData():
                #set the current node with the next node's data
                current.setData(current.getNext().getData())
                #go to the next node
                current = current.getNext()
            else: 
                # if the current data equals the temp data
                if current.getData() == temp:
                    #go to the next node
                    current = current.getNext()
                #if the current data is less than the temp data
                elif current.getData() < temp:
                    #the current node is set the temp data
                    current.setData(temp)
                    #restart from the head
                    current = gList.getHead()                           
        
    
    def length(self):
        '''
        Parameters: None
        Purpose: to return the length of the guessed list
        Return: the length
        '''
        
        return self.__guessedLinkedList.length()
        
    def __str__(self):
        '''
        Parameters: None
        Purpose: to return the list as a string
        Return: list as string 
        '''
        output = ''
        current = self.__guessedLinkedList.getHead()
        while (current != None):
            output += str(current.getData()) + ' '
            current = current.getNext()
        return output

if __name__ == '__main__':
    # test SecretWord and GuessedLetters here
    
    #testing SecretWord
    s= SecretWord()
    s.setWord('YELLOW')
    print('is it solved', s.isSolved())
    print(s)
    s.printProgress()    
    print('is it updated', s.update('L'))
    s.printProgress()        
    print('is it updated', s.update('S'))
    print('is it updated', s.update('Y'))
    print('is it updated', s.update('E'))
    print('is it solved', s.isSolved())  
    s.printProgress()
    print('is it updated', s.update('O'))
    print('is it updated', s.update('W'))
    print('is it solved', s.isSolved())
    s.printProgress()
    print('')
    
    
    #testing GuessedLetters
    g = GuessedLetters()
    print('is Y guessed',g.checkIfGuessed('Y'))
    print('is Y added', g.addGuess('Y'))
    print('is Y guessed', g.checkIfGuessed('Y'))
    print(g.length())    
    print(g)
    print('is Z added', g.addGuess('E'))
    print('is A added', g.addGuess('B'))
    print('is B added', g.addGuess('C'))
    print('is C added', g.addGuess('F'))
    print('is D added', g.addGuess('K')) 
    print(g)    
    g.sortGuesses()   
    print(g)
    print(g.length())
    
    


    