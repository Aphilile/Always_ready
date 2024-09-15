# Ask the user to enter a number
number_entered = 0
average = 0
i = 0
# The program should stop when the user enter -1
while number_entered != -1:
 number_entered = int(input("Enter Number: "))
 # The program is calcuting the average
 if number_entered > 0:
  average += number_entered
  i+=1
  #The program will execute until the user enter -1
 elif number_entered == -1:
  calAverage=average/i
  print("Calculated average is " +str(calAverage))
