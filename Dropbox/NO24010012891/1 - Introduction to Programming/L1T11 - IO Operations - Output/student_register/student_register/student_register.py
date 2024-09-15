students_registering = int(input("How many students are registering?"))

for i in range(1,students_registering+1):

    student_id_number = input("Enter student ID number: ")

    with open('reg_form.txt','a') as student_file:

        student_file.write(student_id_number +"................."+ "\n")