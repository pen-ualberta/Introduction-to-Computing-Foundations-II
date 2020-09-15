#******************
# Lab 9: Exercise 1
# Author:
# Collaborators/References:
#******************

import random
import time


def recursive_selection_sort(data, data_len, index = 0): 
    '''
    Use Selection Sort to arrange the integers in a list (data) in descending order
    Inputs:
       data (list) - list of integers to be sorted
       data_len (int) - number of elements in the data
       index (int) - index of starting element
    Returns: None
    '''
  
    # TODO-Remove pass and fill out the rest. 
    #You may use additional user-defined functions if required.
    minIndex = index
    if data_len >= 1:
        for i in reversed(range(index, data_len)):
            if data[i]> data[minIndex]: 
                minIndex = i
        temp = data[minIndex]
        data[minIndex] = data[i]
        data[i] = temp             
     
    if index+ 1< data_len:
        recursive_selection_sort(data, data_len, index = index+1)
        
    # Recursively calling selection sort function 


  
def recursive_merge_sort(data): 
    '''
    Use MergeSort to arrange the integers in a list (data) in descending order
    Inputs:  data (list) - list of integers to be sorted
    Returns: sorted data list
    '''
    
    # TODO-Remove pass and fill out the rest. 
    #You may use additional user_defined functions if required.
    
    # Set the base case 
    if len(data)<= 1:
        return data
    
    middle = len(data)//2
    
    right = recursive_merge_sort(data[:middle])
    left = recursive_merge_sort(data[middle:])
    
    result = []
    i = 0
    j = 0
    while i<len(left) and j<len(right):
        if left[i]>= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    result+=left[i:]
    result+=right[j:]
    
    return result
    #Find the middle of the data list
    
    #Recursively calling merge sort function for both half of the data list
    
    # merge the two halves of the data list and return the data list

if  __name__== "__main__":
     # Define the list of random numbers
    random_list = [random.randint(1,1000) for i in range(500)]
    list_len = len(random_list) 
    ascending_list = sorted(random_list)
    descending_list = sorted(random_list, reverse=True)
      
    # Calculate the execution time to sort a list of random numbers #
    start_sel = time.time()
    recursive_selection_sort(random_list, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    x = recursive_merge_sort(random_list)   
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of random numbers
    print('The execution time: to sort a random list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
    
    
    # Calculate the execution time to sort a list of intergers already sorted in ascending order #
    start_sel = time.time()  
    recursive_selection_sort(ascending_list, list_len)  
    end_sel = time.time()
    
    start_merge = time.time()
    #recursive_merge_sort(ascending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in ascending order 
    print('The execution time: to sort a ascending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))      
    
    
    # Calculate the execution time to sort a list of intergers already sorted in descending order #
    start_sel = time.time()
    recursive_selection_sort(descending_list, list_len)      
    end_sel = time.time()
    
    start_merge = time.time()
    #recursive_merge_sort(descending_list)
    end_merge = time.time()
    
    # Print the results execution time to sort a list of intergers already sorted in descending order 
    print('The execution time: to sort a descending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))    
