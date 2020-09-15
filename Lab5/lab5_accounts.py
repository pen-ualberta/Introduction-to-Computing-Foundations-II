

        
def processAccounts(accounts):
    toContinue = True
    while toContinue:
        cName = input("Enter account name, or 'Stop' to exit:")
        if cName =='Stop':
            print('Exiting program...goodbye.')
            quit()
        else:
            try:
                bvalue = float(accounts[cName])
                transaction = float(input('Enter transaction amount for:'))
                avalue = transaction + bvalue
                print('New balance for account', cName, ':', avalue)
            except KeyError as myError:
                print('KeyError. Account for', cName, 'does not exist. Transaction cancelled.')
            except ValueError as myError:
                print('ValueError. Incorrect amount. Transaction cancelled. ')
            
    

def readAccounts(infile):
    accounts = {}
    for line in infile:
        try:
            (key,val)= line.strip().split('>')   
            if not val[1:].replace('.', '', 1).isdigit():
                raise ValueError(key)            
            elif val[1:].replace('.', '', 1).isdigit():
                accounts[key] = val
        
        except ValueError as myError:
            print('ValueError. Account for', key, ' not added: illegal value for balance ') 
       
    return accounts
    
        
    
        

        
def main():
    try:
        fileName =input('Enter filename >')
        f = open(fileName, 'r')
        accounts = readAccounts(f)
        processAccounts(accounts)
    except IOError as myError:
        print('IOError.', fileName, 'does not exist')
        print('Exiting program...goodbye.' )

main()

