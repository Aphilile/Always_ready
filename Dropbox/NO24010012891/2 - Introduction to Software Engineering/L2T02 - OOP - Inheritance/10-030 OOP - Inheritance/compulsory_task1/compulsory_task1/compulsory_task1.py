         


# This method in the Course class that prints the head office location: Cape Town.
class Course:
    def __init__(self, name):
        self.name = name
        

    def contact_details(self):
        print(f"Course: {self.name}")
        print("Head Office Location: Cape Town")

# The constructor that initialises the following attributes OOP Fundamentals
# and Mr Anon A. Mouse the trainers name on the subclass.        
class OOPCourse(Course):
    def __init__(self, name="OOP Fundamentals", trainer="Mr Anon A. Mouse"):
        super().__init__(name)
        self.trainer = trainer

    def trainer_details(self):
        print(f"Course: {self.name} (Trainer: {self.trainer})")

# A method in the subclass named "show_course_id" that prints the ID number of the course:#12345
    def show_course_id(self):
        print("Course ID: #12345")

# Create an object of the OOPCourse subclass
course_1 = OOPCourse()

# Call the specified methods
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()            


