#opening the file for reading purposes

file_with_names_dob = open("DOB.txt", "r")

names_and_dob_list = file_with_names_dob.readlines() #Creates a list of the contents of the file DOB.txt

 

print("Name"+"\n")

 

#Looping thought the list contents

for line in names_and_dob_list:

    words = line.split() #Splitting all the words of the file seperated by a space

    print(words[0] + " " + words[1]) #Printing words in first column and second column

  

print("\n" + "Birth Date" + "\n")  

 

#Looping thought the list contents

for line in names_and_dob_list:

    words = line.split() #Splitting all the words of the file seperated by a space

    print(words[2] + " " + words[3] + " " + words[4]) #Printing the rest of the columns

file_with_names_dob.close() #closing the file when done