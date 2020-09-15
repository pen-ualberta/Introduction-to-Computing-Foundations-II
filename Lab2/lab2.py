def getInputFile():
    
    '''
    Parameter: None
    prompts the user to enter a file name
    Sends an error message when the file does not end in .txt
    Returns aFile
    '''

    fileName = input('Enter the input filename:')
    
    while fileName[-4:] != '.txt':
        fileName = input('Invalid filename extension. Please re-enter the input filename:')
    
    else:
        return fileName
    

def readFile(fileName):
    
    '''
    Parameter : fileName
    reads file and splits the lines in the file induvidually in a list
    Returns the txt document into a list
    
    '''
    
    f = open(fileName, 'r')
    aList = f.read().splitlines()
    for line in aList:
        line.strip()
    
    f.close()
    return aList



def decrypt(aList):
    
    ''' 
    Parameter : aList
    Decrypt the message by converting the by finding the number of each encrypted letter, 
    then adding the cipher key, then coverting it back to its original message.
    Returns : Decrypted message
    '''
    
    #if cipher keys are over 26
    key = int(aList[0]) % 26
    #converting the string into a list and in lower case
    emList = list(aList[1].lower())
    
    #maximum letters
    maxNumber = 26
    #new list
    dmList = []
    #for each letter in the list
    for letter in emList:
        #add space if the element is a space
        if letter == ' ':
            dmList.append(' ')
        #if not space, the order is letter minus the key
        else:
            order = (ord(letter) - key)
            #to reverse the order if smaller than the order of 'a'
            if order < ord('a'):
                order += maxNumber
                dmList.append(chr(order))
            else:
                dmList.append(chr(order))  
    
    #turning list back into string
    dMessage = ''.join(dmList)
    return dMessage



def main():
    '''
    Parameters: None
    Purpose: print out original message
    returns: None
    '''
    
    fileName = getInputFile()
    aList = readFile(fileName)
    dMessage = decrypt(aList)
    print(" ".join(dMessage.split()))

    
main()