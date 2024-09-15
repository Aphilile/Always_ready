# The program make the characters in Upper and lower case 
original_string =input("Enter the string: ")
lengthofstring=len(original_string)
words = original_string.split()
lengofeachword = len(words)
increase_string = 0
wcount = 0
while(lengthofstring>0):
    new_string = original_string[increase_string]
    if increase_string %2==0:
        print(new_string.upper(), end='')   
    elif increase_string %2 !=0:
        print(new_string, end='')
    lengthofstring -=1
    increase_string +=1 
print('')
while lengofeachword>0:
    if wcount%2 ==0:
        print(words[wcount].lower(), end= ' ')
    elif wcount%2 !=0:
        print(words[wcount].upper(), end= ' ')
    lengofeachword-=1
    wcount+=1
print(' ')
