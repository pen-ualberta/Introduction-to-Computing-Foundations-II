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
    



