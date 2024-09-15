#Defining variables to be used for competition categories
cycling_time = 0
running_time = 0
swimming_time =0

#Input from the user for the different triathlon categories
cycling_time = int(input("Enter cycling time: "))
running_time = int(input("Enter running time: "))
swimmingtime = int(input("Enter swimming time: "))

#Calculating total time for triathlon
total_time = cycling_time + running_time + swimming_time

#Checking for total time that is less than 100 and display the message stating the award within that category 
if total_time <= 100:
    print("Total time for triathlon is " + str(total_time))
    print("You got an award of Provicial Colours!!!")

# Checking for total time that is greater than 100 and less than 105 and display the message stating the award within that category 
elif total_time > 100 and total_time <= 105:
    print("Total time for triathlon is " + str(total_time))
    print("You got an award of Provicial Half Colours!!!")
    
#Checking for total time that is greater than 105 and less than 110 and display the message stating the award within that category 
elif total_time > 105 and total_time <= 110:
    print("Total time for triathlon is " + str(total_time))
    print("You got an award of Provicial Scroll!!!")
    
#The is no award for the competition 
else:
    print("Total time for triathlon is " + str(total_time))
    print("Sorry you got No Award!!!!")

