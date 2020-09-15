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