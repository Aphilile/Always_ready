

# Creating email class.
class Email:
    has_been_read = False
    
    # Constructor method with instance variables email address, subject line and email content.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        
# Creating email simulator.
class EmailSimulator:

    has_been_read = False
    def __init__(self):
        self.inbox = []
        
# Create three sample email objects and add them to the inbox.
    def populate_inbox(self):
        
        sample_emails = [
            Email("sender1@example.com", "Welcome to HyperionDev!", "Thank you for joining."),
            Email("sender2@example.com","Great work on the bootcamp!","Your progress is impressive."),
            Email("sender3@example.com","Your excellent marks!","Congratulations on your achievements."),]
            
        self.inbox.extend(sample_emails)
        
  
    # List emails function takes self as an argument, 
    # which suggests it's part of a class or object.  
    def list_emails(self):
        print("\nEmail Numbers/Indexes to read from:")
        for i, email in enumerate(self.inbox):
            print(f"{i} {email.subject_line}")
    
    # This method reads an email from the inbox based on the provided index  
    # Removing the has been read email.        
    def read_email(self, index):
        if 0 <= index < len(self.inbox):
            email = self.inbox[index]
            print(f"Email From: {email.email_address}")
            print(f"Subject: {email.subject_line}")
            print(f"Content: {email.email_content} \nhas been read\n")
            self.has_been_read = True
            self.inbox.pop(index)
        else:
            print("Invalid email index.")  
    
    # The email has been read true then print the email  subject line.        
    def has_been_read_true(self):
        print("\nEmail indexes/numbers to read from:")
        for i, email in enumerate(self.inbox):
            print(f"{i} {email.subject_line}") 

# Example usage: 
simulator = EmailSimulator()  
simulator.populate_inbox()

# The while True: loop ensures that the menu keeps 
# displaying until the user chooses to quit.
while True:
    print("\nMenu:")
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Quit application")
    choice = input("Enter your choice: ")
    
    # If the choice 1 on the menu enter the email index then simulator read emails.
    if choice == "1":
        if len(simulator.inbox)>0: 
            simulator.list_emails()
            index = int(input("Enter the email index: "))
            simulator.read_email(index)
        else:
            print("\nAll items have been read!!")
            
    # Choice 2 on the menu unread emails then simulator list emails.

    elif choice == "2":
        if len(simulator.inbox)>0:
            print("Unread emails:")
            simulator.has_been_read_true()
        else:
             print("\nAll items have been read!!")
             
    # Choice 3 on the menu quit the application then print goodbye 
    elif choice == "3":
         print("Goodbye!")
         break
    # Else print invalid choice please select 1,2, or 3.
    else: 
        print("Invalid choice. Please select 1, 2, or 3.")

    

   



     

    

        

        

            


        

 

    
        
            

            


            

            

           

            

        

          

 


        

                  

        

 







 



    

    

    

   

    

  

    
    


   


            

            

        

           

           


        
    
    

  

       

        

  


    

        
