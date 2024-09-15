

from datetime import date

def format_data(data):
    """
    Format task data into a readable format.
    
    Args:
        data (str): A string containing task details separated by commas.
    
    Returns:
        str: A formatted string representing the task details.
    """
    parts = data.strip().split(',')
    
    # Check if parts list has the expected number of elements
    if len(parts) != 6:
        return "Error: Invalid task data format"
    
    assign_to = parts[0]
    task = parts[1]
    task_description = parts[2]
    start_date = parts[3]
    end_date = parts[4]
    completed = parts[5]

    # Format the dates
    start_date = start_date.strip()
    end_date = end_date.strip()

    # Convert 'No' or 'Yes' to more readable 'Not Completed' or 'Completed'
    completed_status = (
        'Completed' if completed.lower() == 'yes' else 'Not Completed'
    )

    # Construct the formatted string
    formatted_string = (
        f"Task: {task}\n"
        f"Assigned to: {assign_to}\n"
        f"Task Description: {task_description}\n"
        f"Start Date: {start_date}\n"
        f"End Date: {end_date}\n"
        f"Completed: {completed_status}\n"
    )

    return formatted_string

def check_credentials(username, password):
    """
    Check user credentials.
    
    Args:
        username (str): The username to check.
        password (str): The password to check.
    
    Returns:
        bool: True if credentials are valid, False otherwise.
    """
    with open("user.txt", "r") as username_password_file:
        for credentials in username_password_file:
            filed_credentials = credentials.strip().split(',')
            if len(filed_credentials) >= 2:
                filed_username = filed_credentials[0]
                filed_password = filed_credentials[1].strip()
                if username == filed_username and password == filed_password:
                    return True
        return False

def is_valid_username(username):
    """
    Check if the username exists in the user file.
    
    Args:
        username (str): The username to check.
    
    Returns:
        bool: True if username exists, False otherwise.
    """
    with open("user.txt", "r") as user_file:
        existing_users = [
            line.split(',')[0].strip() for line in user_file
        ]
        return username in existing_users

def filter_tasks_by_user(username):
    """
    Filter tasks by user.
    
    Args:
        username (str): The username to filter tasks by.
    
    Returns:
        list: A list of formatted task strings for the given user.
    """
    try:
        with open("tasks.txt", "r") as tasks_file:
            user_tasks = []
            for line in tasks_file:
                parts = line.strip().split(',')
                if parts[0] == username:
                    user_tasks.append(format_data(line))
            return user_tasks
    except FileNotFoundError:
        print(
            "The file you are trying to access is not available. "
            "Please add the file in the directory and try again."
        )
        return []

def register_user():
    """
    Register a new user.
    """
    new_username = input("Enter new username: ")
    
    # Check if username already exists
    if is_valid_username(new_username):
        print("Username already exists. Please choose a different username.")
        return
    
    new_password = input("Enter new password: ")
    confirm_password = input("Confirm password: ")

    if new_password == confirm_password:
        with open("user.txt", "a") as user_file:
            user_file.write(f"\n{new_username},{new_password}")
        print(f"User {new_username} registered successfully.")
    else:
        print("Passwords do not match.")

def add_task():
    """
    Add a new task.
    """
    username_of_assigned = input(
        "Enter the username of the person to whom the task is assigned: "
    )
    
    # Check if the username exists
    if not is_valid_username(username_of_assigned):
        print(
            f"Username {username_of_assigned} does not exist. "
            "Please enter a valid username."
        )
        return
    
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter a description of the task: ")
    task_due_date = input("Enter the due date for the task (YYYY-MM-DD): ")
    current_date = date.today().isoformat()
    completed_status = 'No'  # New tasks are initially marked as not completed

    with open("tasks.txt", "a") as tasks_file:
        tasks_file.write(
            f"\n{username_of_assigned},{task_title},{task_description},"
            f"{current_date},{task_due_date},{completed_status}"
        )

    print("Task added successfully.")

def view_all_tasks():
    """
    View all tasks.
    """
    try:
        with open("tasks.txt", "r") as tasks_file:
            for line in tasks_file:
                formatted_task = format_data(line)
                if formatted_task.startswith("Error"):
                    continue  # Skip invalid task entries
                print(formatted_task)
    except FileNotFoundError:
        print("No tasks found or the file does not exist.")

def view_my_tasks(username):
    """
    View tasks assigned to the current user.
    
    Args:
        username (str): The username of the current user.
    """
    user_tasks = filter_tasks_by_user(username)
    if user_tasks:
        for task in user_tasks:
            print(task)
    else:
        print("No tasks found for the current user.")

def display_statistics():
    """
    Display statistics for admin.
    """
    try:
        with open("user.txt", "r") as user_file:
            num_users = sum(1 for line in user_file if line.strip())
        
        with open("tasks.txt", "r") as tasks_file:
            num_tasks = sum(1 for line in tasks_file if line.strip())
        
        print(f"Number of users: {num_users}")
        print(f"Number of tasks: {num_tasks}")
    except FileNotFoundError:
        print(
            "Required files are missing. Please ensure both user.txt and "
            "tasks.txt are present."
        )

def option(username, password):
    """
    Display options based on user role and handle user choice.
    
    Args:
        username (str): The username of the current user.
        password (str): The password of the current user.
    """
    if username == "admin":
        print("""
        r - Register a user
        a - Add task
        va - View all tasks
        vm - View my tasks
        ds - Display statistics
        e - Exit
        """)
    else:
        print("""
        a - Add task
        va - View all tasks
        vm - View my tasks
        e - Exit
        """)

    choice = input("Choose an option: ").strip().lower()

    if choice == "r" and username == "admin":
        register_user()

    elif choice == "a":
        add_task()

    elif choice == "va":
        view_all_tasks()

    elif choice == "vm":
        view_my_tasks(username)
    
    elif choice == "ds" and username == "admin":
        display_statistics()

    elif choice == "e":
        print("Exiting...")
        return

    else:
        print("Invalid option.")
    
    # Recursively call option() to continue menu loop
    option(username, password)

def login():
    """
    Handle user login.
    """
    username = input("Enter username: ")
    password = input("Enter password: ")

    if check_credentials(username, password):
        print("Login successful.")
        option(username, password)
    else:
        print("Invalid username or password.")
        login()

# Entry point of the program
if __name__ == "__main__":
    # Ensure "admin" user exists for testing
    with open("user.txt", "r") as user_file:
        existing_users = [line.split(',')[0].strip() for line in user_file]
        if "admin" not in existing_users:
            with open("user.txt", "a") as user_file:
                user_file.write("\nadmin,admin")
    
    login()
    
    
 

    

 



 

        

            



                

                

                

                     

           

                

       


    

        

            

            

               

                

                    

            

    

        

 



            

            

           

               

               

                

                



                

         

           

            

            

            


            

  















 
  

               
    
   

               



           


                    
      

            

                 

    

          

               

     
            

           



    

 

    



       
       

         

       




 




   

    
    

     
    