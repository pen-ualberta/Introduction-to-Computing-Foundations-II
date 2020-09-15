#Excercise 1
def mylen(aList):
    '''
    Parameters: a list
    Purpsoe: to find the length of a list using recursion
    Returns: the length of a list
    '''
    
    if aList:
        
        num = 1 + mylen(aList[1:])
    else:
        num = 0
    
    return num

#Excercise 2
def intDivision(dividend, divisor):
    '''
    Parameters: dividend and divisor
    Purpose: to find the result of integar division
    Returns: a number 
    '''
    if dividend < 0 or divisor <= 0 :
        raise Exception('number is invalid')
    
    if dividend>= divisor:
        newDividend = dividend - divisor
        num = 1 + intDivision(newDividend, divisor)
    
    elif dividend< divisor:
        if dividend>= (divisor/2):
            num =1
        else:
            num = 0
    return num

def sumdigits(num):
    '''
    Parameters: a number
    Purpose: to find the sum of all digits in a number
    Return: the sum
    '''
    sumFound = False
    if not num:
        sum1 = 0
        sumFound = True
    
    if not sumFound:
        num = int(num)
        if num< 0:
            raise Exception('number needs to be positive')
        
        elif num>=0:
            nextNum = str(num)[1:]
            if len(nextNum) == 1:
                currentNum = str(num)[0]
                sum1= int(currentNum) + int(nextNum)
            else:
                strNum = str(num)[0]
                sum1 = int(strNum) + sumdigits(nextNum)                     
    
    return sum1



def reverseDisplay(num):
    '''
    Parameters: num
    Purpose: to reverse a number by it's digits
    Return: a reversed number
    '''
    
    nnum = int(num)
    if nnum < 0 :
        raise Exception('Entered an invalid number')
    
    if 0 < nnum < 10:
        newNum = nnum
        
    else:    
        length = len(str(nnum))
        strNum = str(nnum)
        intNum = strNum[:(length-1)]
        newNum = strNum[length-1] + str(reverseDisplay(intNum))
        newNum = int(newNum)
        

    return newNum

def binary_search1(key,alist,low,high): 
    '''
    Parameters: key,alist,low,high
    Purpose: to search the index of a  key in list
    Returns: if in list, returns index. if not, returns: item not found
    '''
    nlist = alist


    if low <= len(alist)-1 and high >= 0:
        if key!= nlist[low] and key!= nlist[high]:
            search = binary_search1(key, nlist, low + 1, high-1)
            return ( 'Item is not in the list' )
        else:
            if key == nlist[low]:
                search = low
                return search
            elif key == nlist[high]:
                search = high
                return search
        
    
    
        
    
def main():
    
    print('Excercise 1')
    
    alist=[43,76,97,86]
    print(mylen(alist))
    
    print('')
    print('Excercise 2')
    
    n = int(input('Enter an integer dividend: '))
    m = int(input('Enter an integer divisor: '))
    print('Integer division', n, '//', m, '=' ,intDivision(n,m))    
    
    print('')
    print('Excercise 3')
    
    number = int(input('Enter a number:'))
    print(sumdigits(number))  
    
    
    print('')
    print('Excercise 4')
    number = int(input('Enter a number:'))
    print(reverseDisplay(number))
    
    
    
    print('')
    print('Excercise 5')
    
    some_list = [-8,-2,1,3,5,7,9]
    print(binary_search1(9,some_list,0,len(some_list)-1))
    print(binary_search1(-8,some_list,0,len(some_list)-1))
    print(binary_search1(4,some_list,0,len(some_list)-1))     
    
    
main() 

    
