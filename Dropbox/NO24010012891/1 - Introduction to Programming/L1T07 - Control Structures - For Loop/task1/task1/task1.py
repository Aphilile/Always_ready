# Initialize a variable called "stars" with a single asterisk (*)
stars = "*"

 # Loop from 1 to 8 (inclusive)
for i in range(1, 9):
    
# If the current value of "i" is less than or equal to 4
    if i <= 4:

# Print the current value of "stars"
        print(stars)
        
# Add one more asterisk to the "stars" variable
        stars = stars + "*"
        
# Otherwise (when "i" is greater than 4)
    else:
        
 # Print the current value of "stars"
        print(stars)
        
# Remove the last character (an asterisk) from the "stars" variable
        stars = stars[:-1]
        
# Print a single asterisk (*) after each line
print("*")  
   
