#created the list of numbers
numbers = [11, 25, 32, 4, 67, 18, 50, 11, 4, 11] 
oddNumbers = []
print('The contents of object', id(oddNumbers), 'are', oddNumbers)
#creating a list of odd numbers
for number in numbers:
    if number % 2 == 1:
        oddNumbers.append(number)
print('The contents of object', id(oddNumbers), 'are', oddNumbers)

#the identities haven't changed but the list is muttable

#sorting the list by decreasing order
oddNumbers = sorted(oddNumbers, reverse = True)

#finding the largest and smallest numbers
lNum = oddNumbers.pop(0)
sNum = oddNumbers.pop(len(oddNumbers)-1)
print('The smallest odd number,', sNum, 'has been removed from the list of odd numbers. ')
print('The largest odd number,' , lNum, 'has been removed from the list of odd numbers. ')

#finding the amount of numbers in a list
print('There are', len(numbers), 'numbers in the original list.') 
#removing the smallest number
for number in numbers:
    if number == sNum:
        numbers.remove(number)
print('After removing the smallest odd number, there are', len(numbers), 'numbers in the list:')
print(numbers)


print('')

#creating a list of months
months = ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT')

print('The contents of object', id(months), months) 

#new months
nMonths = ('NOV', 'DEC')
#adding new months
months = months + nMonths 
print(months)

print('The contents of object', id(months), 'are', months)

#the identities of the tuple has changed and therefore it is immuatable

#list of precipitation amounts
precipitation2019 = [15.5, 12.1, 18.5, 15.6, 10.7, 62.2, 41.4, 58.3, 15.7, 15.3, 24.8] 

#adding july levels
precipitation2019.insert(6, 67.8)

print(precipitation2019)

#finding the amount for april
aprilIndex = months.index('APR')

print(str(precipitation2019[aprilIndex]) + 'mm fell in APR 2019')

#asking for the month
monthInput= input('Please enter a month? :')
#if wrong answer
if monthInput not in months:
    print('sorry, cannot find information for the month inputted')
    

#finding precipitaiton levels for said month   
if monthInput in months:
    monthIndex = months.index(str(monthInput))
    print(str(precipitation2019[monthIndex]) + 'mm fell in ' + monthInput+  ' 2019')

print('')

animals = {'dog', 'cat', 'fish', 'snake'} 
print('The contents of object', id(animals) ,'are', animals) 
#The animals are not printed in the expected order
#adding bird while removing snake
animals.remove('snake')
animals.add('bird')
print('The contents of object', id(animals) ,'are', animals) 
#the identities remained the same and therefore are muttable

#list of animals that Alice likes
Alist = ['dog', 'cat', 'rabbit', 'hamster']

#available pets sold at the store for Alice
Apets = animals.intersection(Alist)

print('Alice could buy', Apets , 'from Pets R Us.')

print('')
#flowers with their corresponding prices
fPrices = {'daffodil': 0.35, 'tulips' :0.33, 'crocus' : 0.25, 'hyacinth': 0.75, 'bluebell' :0.50 }
print(fPrices)
fAmount = {'daffodil': 50, 'tulips': 100}
#updates the new daffodil amount into price list
newPrice = 0.33*1.25
danPrices = {'tulips': '%.2f' % newPrice}
fPrices.update(danPrices)
print(fPrices)
#updates the hyacinth amount into amount list
hAmount = {'hyacinth': 30}
fAmount.update(hAmount)
print(fAmount)

#printing the chart
print('You have purchased the following bulbs:')
#sorting flowers by Capital letter
sortedFlowers= sorted(fAmount)

#creating a list of the total prices of each flower
listPrices = []
#creating the chart with the prices
for flower in sortedFlowers:
    disFlower = flower.upper()
    totalPrice = float(fAmount[flower])* float(fPrices[flower])
    listPrices.append(totalPrice)
    print('{:<5}'.format(disFlower[:3]) +'*' + '{:>4}'.format(fAmount[flower]), '=  $', '{:>6.2f}'.format(totalPrice))
    
#total amount of bulbs sold
amount = fAmount.values()
totalVal= sum(amount)
print('')
print('Thank you for purchasing', totalVal, 'bulbs from Bluebell Greenhouses.')

#total price of all flowers
totalPrices= sum(listPrices)
print('Your total comes to $', '{:.2f}'.format(totalPrices))
