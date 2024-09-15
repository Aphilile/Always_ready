# The function takes in the number list to check the largest number.
def largest_number (numbers_list):
   
# Base case: if is only one largest number return that largest number.
   
   if len(numbers_list) == 1:
       return numbers_list[0]  
 
# Rercusive case:Check the largest number on the number list and return max.   
   else:
      return max(numbers_list[0], largest_number(numbers_list[1:])) 
  
# Printing the largest number. 
print(largest_number([1,4,5,3,]))
print(largest_number([3,1,6,8,2,4,5]))



      
      