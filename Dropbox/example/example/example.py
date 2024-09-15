with open('example.txt', 'r') as f:
    lines = file.readlines()
names = ('example.txt','r')
birthdates = ('example.txt', 'r')
for line in lines:
    names.append(parts[0])  
    birthdates.append(' '.join(parts[1:])) 
print("Names:")
for name in names:
    print(name)
print("\nBirthdates:")
for birthdate in birthdates:
    print(birthdate)

