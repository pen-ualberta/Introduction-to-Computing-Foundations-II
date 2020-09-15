#------------------------------
# Assignment 3
# Author: CMPUT 175 team
#------------------------------

class Node:
    def __init__(self, initData, initNext, initVisible = False):
        """ Constructs a new node and initializes it to contain
        the given object (initData) and link to the given next node. """
        self.__data = initData
        self.__next = initNext
        self.__isVisible = initVisible

    def getData(self):
        """ Returns the element """
        return self.__data

    def getNext(self):
        """ Returns the next node """
        return self.__next

    def getIsVisible(self):
        """ Returns whether or not self.__data should be displayed """
        return self.__isVisible

    def setData(self, newData):
        """ Sets newData as the element """
        self.__data = newData

    def setNext(self, newNext):
        """ Sets newNext as the next node """
        self.__next = newNext

    def setIsVisible(self, visible):
        """ Sets whether or not self.__data should be displayed in the WordGuess progress """
        self.__isVisible = visible