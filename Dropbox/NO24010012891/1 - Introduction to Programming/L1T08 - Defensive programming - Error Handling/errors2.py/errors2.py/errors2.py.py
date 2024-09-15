#syntax error it wasn't defined and it was without special characters 
animal = input("Enter the name of animal")
#It was not defined the animal type 
animal_type = input("Enter the type of animal")
#Runningtime error; (number_teeth) needs to be cast with str()
number_of_teeth = str(input("How many teeth does the animal have:"))
#the indentation and concatenate is correct
full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"
#Syntax error the was missing parentheses and it needed () in order to print
print(full_spec)


