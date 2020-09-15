#******************
# Lab 9: Exercise 2
# Author:
# Collaborators/References:
#******************

class Student():
    def __init__(self, id, name, mark):
        '''Initialize the object properties'''
        self.id = id
        self.name = name
        self.mark = mark

    def __str__(self):
        '''Informal string representation of Student'''
        return ' - {}, {}, {}'.format(self.id, self.name, self.mark)

    def is_less_than(self, another_student):
        ''' 
        Checks if the mark of the student is less than the mark of another 
        Student object
        Input: another_student (Student)
        Returns: boolean
        '''
        lessThan = False
        
        if self.mark < another_student.mark:
            lessThan = True
        
        return lessThan
        



def recursive_merge_sort(data):  
    '''
    Uses MergeSort to sort the list of data in INCREASING order
    Returns: the sorted list of Students  
    '''
    # TODO - remove the pass and complete the function
    # Hint: modify your merge sort from exercise 1
    if len(data)<= 1:
        return data

    middle = len(data)//2

    right = recursive_merge_sort(data[:middle])
    left = recursive_merge_sort(data[middle:])

    result = []
    i = 0
    j = 0
    while i<len(left) and j<len(right):
        if left[i].is_less_than(right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result+=left[i:]
    result+=right[j:]

    return result    


if  __name__== "__main__":
    # Read the data
    students_file = open('student_list.txt', 'r')
    students_data = students_file.readlines()
    student_list = []
    

    # Create a Student object corresponding to each line in input file
    for student in students_data:
        fields = student.split(', ')
        id = fields[0]
        name = fields[1]
        mark = fields[2]
        student_list.append(Student(id, name, int(mark)))        

    # Print the original data
    print('Original data:')
    for student in student_list:
        print(student)

    # Sort the students
    sorted_students = recursive_merge_sort(student_list)

    # Print the sorted data
    print('Sorted data:')
    for student in sorted_students:
        print(student)
