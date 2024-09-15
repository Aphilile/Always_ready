

# User inputs that ask for the name, age, hair colour, and eye colour of a person.
name = input("Enter your name:")
age = int(input("Enter your age:"))
hair_colour = input("What is  the colour of your hair:")
eye_colour = input("What your eye colour:")

# Parent class using the attributes on the user input of the person.
class Adult:
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour
        
# Method to check if the person can drive.
    def can_drive(self):
        print(f"{self.name} is {self.age} years old and can drive.")

# Example usage:
person = Adult(name="Alice", age=30, eye_colour="brown", hair_colour="black")
# Output: "Alice is 30 years old and can drive."
person.can_drive()  

# Child class that inherits to the parent class.
class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is too young to drive.")

# Example usage:
child = Child(name="Bob", age=12, eye_colour="blue", hair_colour="blonde")
child.can_drive() 

# This logic will determines if the person is 18 or older 
def create_person(name, age, eye_colour, hair_colour):
    if age >= 18:
        return Adult(name, age, eye_colour, hair_colour)
    else:
        return Child(name, age, eye_colour, hair_colour)

# Example usage:
person1 = create_person(name="Eva", age=20, eye_colour="green", hair_colour="red")
# Output: "Eva is 20 years old and can drive."
person1.can_drive() 

person2 = create_person(name="Sam", age=15, eye_colour="brown", hair_colour="black")
# Output: "Sam is 15 years old and can drive."
person2.can_drive()