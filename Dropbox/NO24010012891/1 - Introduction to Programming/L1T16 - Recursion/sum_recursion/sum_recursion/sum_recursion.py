#This function takes on number list and index.
def adding_up(numbers_list, index):

# Base case:if there is only 1 index return that index.
    if index == 0:
        return numbers_list[0]
    
#Recursive case: add the number at the current index to the sum of the numbers -1  
    return numbers_list[index] + adding_up(numbers_list,index -1)

adding_up([4,3,1,5],1)
adding_up([1,4,5,3,12,16],4)

# Printing the added numbers at the current index.
print(adding_up([1,4,5,3,12,16],4))
print(adding_up([4,3,1,5],1))

    
    
