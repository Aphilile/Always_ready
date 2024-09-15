#Difining the strings to be used on the sentence
number_of_times = 3
adding_words_count = 5
count = 0
#The string  will display the input of the  sentence
str_manip = input("Enter the Sentence: ")
#The string will change to lower cases
change_to_lower = str_manip.lower()
# the program will calculate the lenght of the string from the first letter to the last letter
string_length = len(str_manip)
first_letter = str_manip[0]
second_letter = str_manip[1]
third_letter = str_manip[2]
second_last_letter = str_manip[string_length-2]
last_letter = str_manip[string_length-1]
first_letter = str_manip[0]
#Printing out the the lenght of the string
print("Length of the string is: "+str(string_length))

#Replace the letter from the last three letters backwards
letter_to_replace = change_to_lower[string_length-1]
#printing the last three string from backwards
print("Letter to replace is: " +letter_to_replace)
#Replace the last three letters of the string with @
replaced_string = change_to_lower.replace(letter_to_replace,"@")
#printing the last three letters of the string with @
print(replaced_string)

# The number of time is greater than 0 and the last three on the string will reverse
while number_of_times>0:
    last_three = str_manip[string_length-1]
    
#printing three last letters of the world in reverse
    print(last_three,end='')
    string_length -=1
    number_of_times -=1 
print('') 

#printing the first three number and last two numbers(added together)
print(first_letter+second_letter + third_letter + second_last_letter+last_letter)








