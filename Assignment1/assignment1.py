#----------------------------------------------------
# Assignment 1: Pay It Foward Detection App
# Purpose of code: Creat an app that tracks 
# overpayment
# Author: Penelope Chen (Final)
# Collaborators/references:
#----------------------------------------------------


def printMenu():
    '''
    Parameters: None
    Purpose: prints menu
    Returns: None
    '''
    
    dashLine = ('*'*43)
    print(dashLine)
    print('Welcome to the Pay It Forward Detection App')
    print(dashLine)
    
    
    print('What would you like to do?')
    print('1  Print PAY IT FORWARD CHAINS for current month')
    print('2. Print and save REGIONAL IMPACT GRAPH for current month')
    print('3. Quit')    
    
    

def createMenu():
    '''
    Parameters: None
    Purpose: continuously prints menu until user chooses an option between 1 , 2 and 3
    Returns: option 
    '''
    
    toContinue = True
    cOptions = ['1','2','3']
    while toContinue:
        printMenu()
        option = input('>')  
        print('')
        if option in cOptions:
            toContinue = False
        else:
            print('Sorry, invalid entry. Please enter a choice from 1 to 3.') 
            toContinue = True
    
    return option
    

def cOneHeader():
    ''' 
    Parameters: None
    Purpose: Prints out option 1 header
    Return None
    '''
    
    dash =('+' + '-'*16 + '+' + '-' *19 + '+'+ '-'*14 + '+' + '-'* 23 + '+')
    c1 = '{:^16}'.format('Name')
    c2 = '{:^19}'.format('Kindness Received')
    c3 = '{:^14}'.format('PIF Fund')
    c4 = '{:^23}'.format('Day & Time')
    
    print('Pay It Forward Chain:')
    print(dash)
    print('|' + c1 + '|' + c2 + '|' + c3 + '|' + c4 + '|')
    print(dash)
    
def cTwoHeader():
    '''
    Parameters: None
    Purpose: prints out option 2 header
    Return: None
    '''
    dash = '=' * 44
    print(dash)
    print('Regions impacted by Pay It Forward Actions: ')
    print(dash)
  
def readFile(fName):
    '''
    Parameters: fName
    Purpose: reads file and sorts into list
    returns: a list of info
    '''
    
    f = open(fName, 'r')
    aList = f.read().splitlines()
    f.close()
    
    return aList

    
def splitList1():
    '''
    Parameter: None
    Purpose: sort transaction list and sorting values to a list for option 1
    Returns: values in a list
    '''
    transactionsF = ('transactions.txt')
    transL = readFile(transactionsF)
    
    #split lines by ';'
    ntransL = []
    for line in transL:
        nline = line.split(';')
        ntransL.append(nline)
    
    #removing the C and the initials
    anon = 'anonXXXXXXXXXX'
    for line in ntransL:
        line[0] = line[0].split('C')
        if line[1] != anon:
            line[1]= ''.join(i for i in line[1] if i.isdigit())

    return ntransL



def splitList2():
    '''
    Parameter: None
    Purpose: sort loyalCustomers list and sorting values to a list for option 1
    Returns: values in a list
    '''    
    loyalcsF = ('loyalCustomers.txt')
    loyalL = readFile(loyalcsF)
    
    nloyalL = []
    
    #split lines by ','
    for line in loyalL:
        nline = line.split(',')
        nloyalL.append(nline)    
    
    return nloyalL


def seperateDates():
    '''
    Parameters: None
    Purpose:seperate transactions list by their date
    Return : a list seperated by date
    '''
    tL = splitList1()
    
    #creating a list of all dates without duplicate
    dates = []
    for alist in tL:
        date = alist[0][0]
        dates.append(date)
        
    dates = list(dict.fromkeys(dates))
    dates = sorted(dates)
    
    #max amount of lists
    maxSize = len(dates)
    
    
    #creating a new set of lists
    sL = []
    for date in dates:
        sL.append([])
    
    #sorting list by their dates of transaction
    for alist in tL:
        i= 0   
        for i in range(0, maxSize):
            #if the date is equivilant
            if alist[0][0] ==  dates[i]:
                sL[i].append(alist)
                i+=1
            else:
                i= i
    
    #sort each transaction of each date by the time of transaction
    for alist in sL:
        alist = alist.sort(key= lambda x : x[0][1])
         
    return sL
    

def createDict1():
    '''
    Parameters: None
    Purpose: to create and sort the lists into a dictionary
    Return: a dictionary
    '''
    tL = seperateDates()
    
    dL = []         
    for alist in tL:
        nL = []
        for anList in alist:
            tvalues = anList[0][0], anList[0][1], anList[2], anList[3]
            lvalues = list(tvalues)
            d = {}
            d[anList[1]] = lvalues
            nL.append(d)
        #removes all the non involved kindness days
        if len(nL) >=2 :
            dL.append(nL)
          
    return dL

def createDict2():
    '''
    Parameters: loyal customer list
    Purpose: to create and sort the lists into a dictionary
    Return: a dictionary
    '''    
    lL = splitList2()
    
    dL = {}      
    for anList in lL:
        tvalues = anList[1], anList[2], anList[3]
        lvalues = list(tvalues)
        d = {}
        d[anList[0]] = lvalues
        dL.update(d)
    return dL

def option2Dict():
    '''
    Parameters: None
    Purpose: find how many time a region was affected by PIF
    Returns: a dictionary containing the info
    '''
    tD = createDict1()
    lD = createDict2()
    
    op2D  = tD.copy()
    
    anon = 'anonXXXXXXXXXX'
    
    for date in op2D:
        for d in date:
            [[key, value]] = d.items()
            # change the value to the corresponding address
            #if the customer was not a loyal cs
            if key == anon:
                address = 'UNKNOWN'
                d[key] = address
            else:
                address = lD[key][2]
                d[key] = address.upper()
    return op2D
                         
    
def option1Dict():
    '''
    Parameters: None
    Purpose: transfer the names of the customers , match and add them to option 1 dict
    Return: a dict with all the info for option 1
    '''
    tD = createDict1()
    lD = createDict2()
    
    op1D = tD.copy()
    
    #if name is Anonymous
    anon = 'anonXXXXXXXXXX'
    for alist in op1D:
        for d in alist:
            [[key, value]] = d.items()
            #convert and add names      
            if key == anon:
                name = 'Anonymous'
                d[key].append(name)
            else:
                d[key].append(lD[key][1])
    
    return op1D

def listofValues1():
    '''
    Parameters: None
    Purpose: to covert all infos in a proper list with the right wording for the time
    Return: a list with all values needed for option 1
    '''
    op1D = option1Dict()
    
    #final list created
    finalList= []
    for date in op1D:
        dateList= []
        for adict in date:
            for key in adict:
                info = adict[key]
                name = info[4]
                minutes =int( info[1])
                #converting the time in proper format
                hours = '{:02}:{:02}'.format(*divmod(minutes, 60))
                #list of months
                months = ['Jan ', 'Feb ', 'Mar ', 'Apr ', 'May ', 'Jun ', 'Jul ', 'Aug ', 'Sep ', 'Oct ', 'Nov ', 'Dec ']
                #finding the relative month integer to match the correlating month in the right word format
                #if the month is under 10
                if str(info[0][2]) == '0':
                    monthsInt = (int(info[0][3] )- 1)
                    month = months[monthsInt]
                    time = (month + (str(info[0][0:2]) + ', ') +info[0][4:8] + ' ' +'at ' + hours)
                    values = [name, info[2], info[3],  time]
                    #adding the list of info to a list dependant on its date
                    dateList.append(values)

                #if the integer is over 10
                else:
                    monthsInt = (int(info[0][2:4]) - 1)
                    month = months[monthsInt]
                    time = (month + (str(info[0][0:2]) + ','), info[0][4:8] + ' '+ 'at ' + hours)
                    values = [name , info[2], info[3], time]
                    dateList.append(values)
        finalList.append(dateList)
        
    return finalList

def listofValues2():
    '''
    Parameters: None
    Purpose: to sort the dictionary into a reversed list of dicts with region counted
    Return: a list containing the values needed for option 2
    '''
    op2D = option2Dict()
    
    #convert the dictionary into a list of locations
    listofLocations = []
    for date in op2D:
        for d in date:
            [[key,value]] = d.items()
            listofLocations.append(value)
   
    #removing the duplicates of the locations
    nlistofLocations= list(dict.fromkeys(listofLocations))
    flistofLocations = []
    #making 'unknown' to be the first element
    i = 0
    for i in range(0, len(nlistofLocations)-1):
        if nlistofLocations[i] == 'UNKNOWN':
            flistofLocations.append(nlistofLocations[i])
            del nlistofLocations[i]
    
    #reverse the rest of the list
    nlistofLocations = sorted(nlistofLocations, reverse = True)
    flistofLocations.extend(nlistofLocations)
    
    
    finalList = []
    
    #count the amount of times each locations was affected
    for place in flistofLocations:
        i = 0
        timesAffected = 0
        newDict = {}
        for i in range(0, len(listofLocations)):
            if place == listofLocations[i]:
                timesAffected+=1
            i+=1
        newDict[place] = timesAffected
        finalList.append(newDict)
            
            
    return finalList

def calculatingKindPIF():
    '''
    Parameters: None
    Purpose: to the value list with calculated values
    Returns: a list of values seperated by their dates
    '''
    
    valueList = listofValues1()
    
    
    i = 0
    for date in valueList:
        for i in range(0, len(date)):
            #first transaction of the day
            if i == 0:
                #PIF
                date[i][2] = int(date[i][2]) - int(date[i][1])
                #KIND
                date[i][1] = '--'
            #if the fund is larger than purchase
            elif int(date[i-1][2]) >= int(date[i][1]):
                #PIF
                date[i][2] = int(date[i-1][2])  +int(date[i][2])- int(date[i][1])
                #KIND
                date[i][1] = int(date[i][1])
            #if fund is smaller than purchase
            elif int(date[i-1][2]) < int(date[i][1]):
                #PIF
                date[i][2] = int(date[i][2])- (int(date[i][1]) - int(date[i-1][2]))
                #KIND
                date[i][1] = int(date[i-1][2])
            
            
    return valueList                           

def printChart1():
    '''
    Parameters: None
    Purpose: to format the values of the calculated list and print chart
    Returns: None
    '''
    
    valueList = calculatingKindPIF()
    dash =('+' + '-'*16 + '+' + '-' *19 + '+'+ '-'*14 + '+' + '-'* 23 + '+')

    for date in valueList:
        #print header
        cOneHeader()
        totalOverPay = 0
        totalKindPpl = 0
        for trans in date:
            #if the length of name is over 14 characters
            if len(trans[0]) >= 14:
                name = (trans[0][0:13]+'*')
            else:
                name = trans[0]
            nameFormat = '{:<16}'.format(name)
            dollarSign = '{:^3}'.format('$')
            if trans[1] == '--':
                kindR = '--'
                kindRF = '{:^19}'.format(kindR)
            else:
                kindR = float(trans[1]/100)
                kindRF = dollarSign + '{:>16.2f}'.format(kindR)
            PIF = '{:>11.2f}'.format(float(trans[2])/100)
            dT = '{:^23}'.format(trans[3])
            
            print('|' + nameFormat + '|' +  kindRF  + '|' + dollarSign + PIF + '|' + dT + '|')
            
            # finding the total overpayments for each set of dates
            if float(PIF) > totalOverPay:
                totalOverPay = float(PIF)
            #finding the total people whom recieved kindness   
            if kindR != '--' and float(kindR) > 0:
                totalKindPpl +=1  
        #format the bottom part of the chart
        totalOverPayf = '{:>11.2f}'.format(totalOverPay)
        oPayf = '{:<37}'.format('Total overpayments:')
        totalKindPplf = '{:>14}'.format(str(totalKindPpl))
        tKPf = '{:<37}'.format('Total people who received kindness:')
        #print bottom parts of the chart
        print(dash)
        print('|' + oPayf + dollarSign + totalOverPayf + '|')
        print('|' + tKPf + totalKindPplf + '|')
        print('+' + '-'*16 + '+' + '-' *19 + '+'+ '-'*14 + '+')
        print('')
            
def printChart2():
    '''
    Parameters: None
    Purpose: Print chart in the correct format
    Return: None
    '''
    
    valueList = listofValues2()

    cTwoHeader()
    
    for v in valueList:
        [[key, value]] = v.items()
        hashValue = (int(value)*'#')
        print(key, hashValue)
    
    dash = '=' * 44
    print(dash)
    print('')

       
        
def saveChart2():
    '''
    Parameters: None
    Purpose: save chart to a file named regionSummary.txt
    Return: None
    '''
    valueList = listofValues2()
    
    f = open('regionSummary.txt', 'w')
    dash = '=' * 44
    
    f.write(dash + '\n')
    f.write('Regions impacted by Pay It Forward Actions: ' + '\n')
    f.write(dash+ '\n')
    
    for v in valueList:
        [[key, value]] = v.items()
        hashValue = ' ' + (int(value)*'#')
        f.write(key + hashValue + '\n' )
    
    
    f.write(dash + '\n')
       
    
def main():
    toContinue = True
    while toContinue:
        option = createMenu()
        if option == '1':
            printChart1()
        elif option == '2':
            printChart2()
            saveChart2()
        elif option == '3':
            print('Thank you for using the Pay It Forward Detection App! Goodbye.')
            toContinue = False

    
    
main()