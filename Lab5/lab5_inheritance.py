#----------------------------------------------------
# Lab 5, Exercise 1: Exceptions and inheritance
# Purpose of code:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------



# Write your TransitionError class definition here.
# It is derived from the Exception base class, but has 3 unique properties that 
# need to be initialized in a custom __init__ method:
#   self.previousState - state at beginning of transition
#   self.nextState - attempted state at end of transition
#   self.msg - message explaining why specific transition is not allowed
# It also has one unique behaviour (i.e. method): printMsg()

#function2 priortizes the general exception over the custom exception


class TransitionError(Exception):
    
    def __init__ (self, beginning, final):
        '''
        initialize exception
        set two attributes to the exception using the 2 parameters
        '''
        self.previousState = beginning
        self.nextState = final
        self.msg = ('Transition error: Not normal to transition from adult to baby')
        
    def printMsg(self):
        '''
        prints attributed message
        '''
        
        message = self.msg
        print(message)


def function1(start, end):
    print('Running function1...')
    try:
        print('Benjamin Button started life as a(n)', start, 'and ended as a(n)', end)
        raise TransitionError(start, end)
    except TransitionError as myError:
        print('Transition error:', end = ' ')
        myError.printMsg()
    except Exception:
        print('General error')
    
    print('Exception was handled successfully: function1 finished.\n')    


def function2(start, end):
    print('Running function2...')
    try:
        print('Benjamin Button started life as a(n)', start, 'and ended as a(n)', end)
        raise TransitionError(start, end)
    except Exception:
        print('General error')
    except TransitionError as myError:
        print('Transition error:', end = ' ')
        myError.printMsg()       
    
    print('Exception was handled successfully: function2 finished.')  


def main():
    start = 'adult'
    end = 'baby'
    
    function1(start, end)
    function2(start, end)
    
main()
