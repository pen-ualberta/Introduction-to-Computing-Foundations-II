#Exercise 1
#yes you can put stacks into a list as a list, it would function
#the same way as a list except the stack would have features such as pop or peep or push.
#for stack in self.board:
#   stack = Stack()

#----------------------------------------------------
# Lab 4, Exercise 2: Web browser simulator
# Purpose of code:Create a web brower simulator
#
# Author: Penelope Chen 
# Collaborators/references:
#----------------------------------------------------

from stack import Stack

def getAction():
    '''
    purpose :get action
    retruns action
    '''
    #delete pass and write your code here
    action = input('Enter = to enter a URL, < to go back, > to go forward, q to quit:')
    
    validActions = ['=', '<', '>', 'q']
    if action not in validActions:
        print('Invalid Action')
    return action

def goToNewSite(current, bck, fwd):
    '''
    go to new site
    returns new site
    '''
    #delete pass and write your code here
    newSite = input('URL:')
    
    bck.push(current)
    while not fwd.isEmpty():
        fwd.pop()
    return newSite
        
def goBack(current, bck, fwd):
    '''
    go back to previous site
    returns precious site
    '''
    #delete pass and write your code here
    if bck.isEmpty():
        print('Cannot go back')
        newSite = current
        
    if not bck.isEmpty():  
        newSite = bck.pop()
        fwd.push(current)
        
    
    return newSite    


def goForward(current, bck, fwd):
    '''
    go to next site
    returns site
    '''
    #delete pass and write your code here
    if fwd.isEmpty():
        print('Cannot go forward')
        newSite= current
    
    if not fwd.isEmpty():
        newSite = fwd.pop()
        bck.push(current)
        
    return newSite
   


def main():
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        action = getAction()
        
        if action == '=':
            current = goToNewSite(current, back, forward)
        elif action == '<':
            current = goBack(current, back, forward)
        elif action == '>':
            current = goForward(current, back, forward)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()




