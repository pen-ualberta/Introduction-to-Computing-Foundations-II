class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self,initData,initNext,initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious
        
        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self
            
    def getData(self):
        return self.data
    
    def setData(self,newData):
        self.data = newData
        
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous
    
    def setNext(self,newNext):
        self.next = newNext
        
    def setPrevious(self,newPrevious):
        self.previous = newPrevious

class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0        
           
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index        
         
        
    def insert(self, pos, item):
        # TODO: mandatory
        # add and append referenced from the lectures
        #assertion statements
        '''
        Parameters: pos, item
        Purpose: to insert an item in a position in the list
        Return : None
        '''
        assert type(pos) == int
        strPos = str(pos)
        assert strPos[0] != '-'
        
        
        temp1= DLinkedListNode(item, self.head, None)
        temp2 = DLinkedListNode(item, None, None)  
        
        #add the item at the end of list
        if pos == self.size:
            if self.head == None:
                self.head = temp2
            else:
                self.tail.setNext(temp2)
                temp2.setPrevious(self.tail)
            self.tail = temp2
            self.size = self.size + 1
            
        #add item at the beginning of list         
        elif pos == 0:
            if self.head!= None:
                self.head.setPrevious(temp1)
            else:
                self.tail = temp1
            self.head = temp1
            self.size = self.size +1
        #add item at a certain postion    
        else:
            current = self.head
            for n in range(pos-1):
                current = current.getNext()
            nextNode = current.getNext()
            newNode = DLinkedListNode(item, nextNode, current)
            current.setNext(newNode)
            self.size = self.size+1
            
        

    def searchLarger(self, item):
        # TODO: mandatory
        #see if item is largest item in list, if not, return position of largest element
        '''
        Parameters: item
        Purpose:see if item is largest item in list, if not, return position of largest element
        Return: index of largest number, or if item:-1
        '''
        largest = item
        index = -1
        current = self.head
        found = False
        
            
        while not found and current!= None:
            if current.getData() > largest:
                found = True       
                largest = current.getData()
            elif self.tail == current and current.getData() <= largest:
                found = True
            current = current.getNext()
            index = index +1      
            
        if largest == item:
            index = -1   
        return index

    def getSize(self):
        # TODO: mandatory  
        '''
        Parameters: None
        Purpose: getting the number of linked elements in a list
        Return: size
        '''
        
        return self.size
    
    def getItem(self, pos):
        '''
        Parameters: pos
        Purpose: to return a item at a position in the list
        Return: the item 
        '''
        
        # TODO: mandatory  
        current = self.head
        
        if str(pos)[0] == '-':
            pos = self.size + int(pos)
        
        if pos not in range(self.size):
            raise Exception('Position out of range!')
        
        for n in range(pos):
            current= current.getNext()
            
        return current.getData()    
        
        
    def __str__(self):
        '''
        Parameters: None
        Purpose: to return the list as a string
        Return : list(str)
        '''
        # TODO: mandatory  
        current = self.head
        string = ''
        while current != None:
            string = string + str(current.getData()) + ' '
            current = current.getNext()
            
        return string.strip()        



    def add(self, item):
        # optional exercise
        pass
        
    def remove(self, item):
        # optional exercise
        pass
        
    def append(self, item):
        # optional exercise
        pass
        
    def pop1(self):
        # optional exercise
        pass
    
    def pop(self, pos=None):
        # optional exercise
        # Hint - incorporate pop1 when no pos argument is given
        pass
        
    

def test():
                  
    linked_list = DLinkedList()
                    
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.insert(0, "Hello")
    linked_list.insert(1, "World")  
    print(str(linked_list))
    
    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"
    
    
    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.getItem(0) == "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
    '''
    '''
    '''
    OPTIONAL TESTS FOR OPTIONAL EXERCISE - do not need to demo
    '''
    '''
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test" 
    
    int_list2 = DLinkedList()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
                
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"    
    '''
                    
    int_list = DLinkedList()
                    
    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"                   
                    
    for i in range(9, -1, -1):
        int_list.insert(0,i)      
            
    is_pass = (int_list.getSize() == 10)
    assert is_pass == True, "fail the test"            
            
    is_pass = (int_list.searchLarger(8) == 9)
    assert is_pass == True, "fail the test"
            
    int_list.insert(7,801)   
    print(int_list)
        
    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"
                  
    is_pass = (int_list.getItem(-1) == 9)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.getItem(-4) == 801)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")
             
if __name__ == '__main__':
    test()
