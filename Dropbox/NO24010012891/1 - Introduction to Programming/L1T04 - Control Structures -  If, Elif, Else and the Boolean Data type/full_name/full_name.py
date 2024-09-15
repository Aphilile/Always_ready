# User input for full name
full_name = input("Enter full name: ")

# Remove any leading/trailing spaces
full_name_without_spaces = full_name.strip()

# Calculate the length of the full name without spaces
full_name_without_spaces_length = len(full_name_without_spaces)

# Count the number of words in the full name
full_name_words = len(full_name_without_spaces.split())

# Check various conditions based on user input
if full_name_without_spaces_length <= 0:
    print("You haven't entered anything. Please enter your full name.")
elif full_name_without_spaces_length < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
elif full_name_without_spaces_length > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
elif full_name_words > 2 or full_name_words < 2:
    print("Please enter two words for the correct full name.")
elif full_name_words == 2 and full_name_without_spaces_length > 4:
    print("Thank you for entering your valid name.")
