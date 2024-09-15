

# The user is prompted to choose between calculating new results or printing previous ones.
try:
    options = input("Do you want to calculate or print previous results: ")
    options_stripped = options.strip()
    options_tolower = options_stripped.lower()
 
# If they choose to calculate, they input two numbers and an operation (+, -, *, or /).
    if options_tolower == "calculate":
        try:
            first_number = int(input("Enter first number for calculation: "))
            second_number = int(input("Enter second number for calculation: "))
            operation = input("Enter operation between these ('+,-,* or /'): ")
            
# The program performs the calculation and displays the result.
            if operation == "+" or operation == "-" or operation == "*" or operation == "/":
                if operation == "+":
                    answer = first_number + second_number
                    print(f'{first_number} + {second_number} = {answer}')
                    f = open("equation.txt", "a")
                    f.write( str(first_number) + " + "+ str(second_number) + " = " + str(answer) + '\n')
                    f.close()
                elif operation == "-":
                    answer = first_number - second_number
                    print(f'{first_number} - {second_number} = {answer}')
                    f = open("equation.txt", "a")
                    f.write( str(first_number) + " - "+ str(second_number) + " = " + str(answer) + '\n')
                    f.close()
                elif operation == "*":
                    answer = first_number * second_number 
                    print(f'{first_number} * {second_number} = {answer}')
                    f = open("equation.txt", "a")
                    f.write( str(first_number) + " * "+ str(second_number) + " = " + str(answer) + '\n')
                    f.close()
                elif operation == "/":
                    try:
                        answer = first_number / second_number
                        print(f'{first_number} / {second_number} = {answer}')
                        f = open("equation.txt", "a")
                        f.write( str(first_number) + " / "+ str(second_number) + " = " + str(answer) + '\n')
                        f.close()
                    except ZeroDivisionError:
                        print("Dividing by 0 is not allowed")
            else:
                print(f'Operation ,{operation} , is not an operation, choose(+,-,* or /)')
        except ValueError:
            print("Please enter an integer in the first and / second number fields")
    elif options_tolower == "print previous results" :
        f = open('equation.txt', 'r')
        file_contents = f.read()
        print(file_contents)
    else:
        print(f'Input ,{options_tolower}, is not correct',
              'please enter either(calculate/print previous results)')
        
# If the file doesn't exist, it prints an error message.
except FileNotFoundError:
    print("file does not exist")

