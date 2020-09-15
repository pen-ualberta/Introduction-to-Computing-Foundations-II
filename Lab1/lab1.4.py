#flowers with their corresponding prices
fPrices = {'daffodil': 0.35, 'tulips': 0.33, 'crocus': 0.25, 'hyacinth': 0.75, 'bluebell':0.50 }
print(fPrices)
fAmount = {'daffodil': 50, 'tulips': 100}
#updates the new daffodil amount into price list
newPrice = (fPrices['tulips'])* 1.25
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
