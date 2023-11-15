# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   KWard,11/11/2023,Created Script
#   KWard, 11/12/2023, finished
# ------------------------------------------------------------------------------------------ #
import json
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print('File does not exist \n')
    print("--Error Message-- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print('There was an unspecific error \n')
    print("--Error Message-- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try: 
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError('First name cannot contain numbers')
            if len(student_first_name) == 0:
                print('Must enter a name')
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError('Last name cannot contain numbers')
            if len(student_last_name) == 0:
                print('Must enter a name')
            course_name = input("Please enter the name of the course: ")
            if len(course_name) == 0:
                print('Must enter a course')
            student_data = {'firstName' : student_first_name ,'lastName' : student_last_name, 'courseName' : course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        
        except ValueError as e:
            print(e)
            print("--Error Message-- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print('There was an unspecific error \n')
            print("--Error Message-- ")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f'{student["firstName"]} {student["lastName"]} is enrolled in {student["courseName"]}')  
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
        except FileNotFoundError as e:
            print('The file does not exist \n')
            print("--Error Message-- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("There was a non-specific error!\n")
            print("--Error Message-- ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            file.close()
        print("The following data was saved to file!")
        for student in students:
            print(f'{student["firstName"]} {student["lastName"]} is enrolled in {student["courseName"]}')
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
