# -----------------------------------------------------------------------------------------------------------#
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   <Rucha Nimbalkar>,<11/16/2024>,<Update Script with my name and other details>
#   <Rucha Nimbalkar>,<11/19/2024>,<Add function definitions and function calls in the main body>
#   <Rucha Nimbalkar>,<11/19/2024>,<Reorganize the code to apply "Separation of Concerns Pattern">
#   <Rucha Nimbalkar>,<11/19/2024>,<Add doc strings to the functions>
# ---------------------------------------------------------------------------------------------------------- #
import json

#Data-------------------------------------------------------------------------------------------------------#
#Global Data--------------------------------------------------------------------------------------------#
# Define the Data Constants and Variables
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"
students : list = [] # a table of student data
menu_choice: str  # Hold the choice made by the user.

    # The following variables are not used in this assignment.
    # FILE_NAME: str = "Enrollments.csv" #Note: Commented as won't be used in this assignment.
    #student_first_name: str = ''  # Holds the first name of a student entered by the user. #Note: Commented as won't be used in this assignment.
    #student_last_name: str = ''  # Holds the last name of a student entered by the user.#Note: Commented as won't be used in this assignment.
    #course_name: str = ''  # Holds the name of a course entered by the user.#Note: Commented as won't be used in this assignment.
    #student_data: dict = {} # one row of student data#Note: Commented as won't be used in this assignment.
    #csv_data: str = ''  # Holds combined string data separated by a comma.#Note: Commented as won't be used in this assignment.
    #json_data: str = ''  # Holds combined string data in a json format.#Note: Commented as won't be used in this assignment.
    #file = None  # Holds a reference to an opened file.#Note: Commented as won't be used in this assignment.

# End of Variable Declaration---------------------------------------------------------------------------#

# Processing --------------------------------------- #
class FileProcessor:
    """
        A collection of processing layer functions that work with Json files
        ChangeLog: (Who, When, What)
        Rucha Nimbalkar,11.19.2024,Created Class
        Rucha Nimbalkar,11.19.2024, Added  a function to read data from the file
        Rucha Nimbalkar,11.19.2024, Added a function to write(save) data to the file
    """
    # When the program starts, read the file data into table
    # Extract the data from the file
    # Read from the Json file

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data (student data) from the file (given file name)

            ChangeLog: (Who, When, What)
            Rucha Nimbalkar,11.19.2024,Created function

            :param file_name: str containing the file name as the first parameter
            :param student_data : List containing student data in JSON format as the second parameter
            return: student_data with the data read from the file
        """
        try:
            file = open(file_name, "r")  # Open the file in read mode
            student_data = json.load(file)  # Load the file contents
            #print(student_data)#Used this code statement while testing, this is not required for this assignment.
            file.close()  # close the file
            # CSV Answer #Not applicable in this assignment
            # for row in file.readlines():
            #     # Transform the data from the file
            #     student_data = row.split(',')
            #     student_data = {"FirstName": student_data[0],
            #                     "LastName": student_data[1],
            #                     "CourseName": student_data[2].strip()}
            #     # Load it into our collection (list of lists)
            #     students.append(student_data)
        except Exception as e:
            error_message = "Error: There was a problem with reading the file."
            IO.output_error_messages(message=error_message,error=e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes (saves) data (student data) to the file (given file name)

            ChangeLog: (Who, When, What)
            Rucha Nimbalkar,11.19.2024,Created function

            :param file_name: str containing the file name as the first parameter
            :param student_data : List containing student data in JSON format as the second parameter
            return: None
        """
        try:
            file = open(file_name, "w")
            # CSV answer  #Not applicable in this assignment,
            # for student in students:
            #     csv_data = f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}\n'
            #     file.write(csv_data)
            # # JSON answer
            json.dump(student_data, file)  # Write the contents in the file
            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except TypeError as e:
            error_message = "Error: There was a problem with writing to the file."
            IO.output_error_messages(message=error_message, error=e)
        except Exception as e:
            error_message = "Built-In Python error info: "
            IO.output_error_messages(message=error_message,error= e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
        A collection of presentation layer functions that manage user input and output
        ChangeLog: (Who, When, What)
        Rucha Nimbalkar,11.19.2024,Created Class
        Rucha Nimbalkar,11.19.2024, Added  a function to display menu
        Rucha Nimbalkar,11.19.2024, Added a function to accept user choice from the menu options
        Rucha Nimbalkar,11.19.2024, Added  a function to display student data
        Rucha Nimbalkar,11.19.2024, Added a function to accept student data (as input)
    """
    @staticmethod
    def output_menu(menu:str):
        """ This function displays the menu of choices to the user

          ChangeLog: (Who, When, What)
          Rucha Nimbalkar,11.19.2024,Created function
          :param menu: str data used as the menu of choices
          :return: None
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """ This function accepts user choice

            ChangeLog: (Who, When, What)
            Rucha Nimbalkar,11.19.2024,Created function

            :return: str data with user choice from the menu options
        """
        user_choice = input("What would you like to do: ")
        return user_choice

    @staticmethod
    def output_student_courses(student_data:list):
        """ This function prints the current student data (first name, last name and course name) on the console

            ChangeLog: (Who, When, What)
            Rucha Nimbalkar,11.19.2024,Created function

            :param student_data : list of JSON data (in key value format)
            :return: None
        """
        # Process the data to create and display a custom message
        print("-" * 40)
        for student in student_data:
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 40)

    @staticmethod
    def input_student_data(student_data:list):
        """ This function accepts input of student data (first name, last name and course name) from the user

            ChangeLog: (Who, When, What)
            Rucha Nimbalkar,11.19.2024,Created function

            :param student_data : list of JSON data (in key value format)
            :return: list data as student_data with user entered student information
        """
        student: dict = {}
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="ValueError",error=e)
        except Exception as e:
            error_message="Error: There was a problem with your entered data."
            IO.output_error_messages(message=error_message,error=e)
        return student_data

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays error messages on the console caused due to exceptions or invalid input

            ChangeLog: (Who, When, What)
            Rucha Nimbalkar,11.19.2024,Created function

            :param message : str containing error message as the first parameter
            :param error : Exception containing Exception occurred (default value is none)
            :return: None
        """
        print(message)  # Prints the message
        if error is not None: #Print the technical error message for Exception occurred.
            print("-- Technical Error Message -- ")
            print(error)  # Prints the custom message
            print(error.__doc__)
            print(error.__str__())
        return

#End of Function definitions---------------------------------------------------------------------------------------------------#

#Beginning of the main body of the script--------------------------------------------------------------------------------------#

# When the program starts, read the file data into a list of lists (table)
# Call function to extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(MENU)
    menu_choice=IO.input_menu_choice() #call the function to accept user choice after displaying the menu

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students) #call function to accept new student data
        continue

    # Present the current data
    elif menu_choice == "2":
        #Call function to display student course
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        print("Exiting the program")
        break  # out of the loop

    else:
        error_message="Please enter a valid option 1, 2 , 3 or 4"
        IO.output_error_messages(message=error_message)

print("Program Ended")#Program terminated
#End of the main body of the script--------------------------------------------------------------------------------------#