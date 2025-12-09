file_name = 'Saved_data.txt'
class Students:
    def __init__(self, id, first_name, last_name, gpa, semester):
        self.__id = int(id)
        self.__fn = str(first_name)
        self.ln = str(last_name)
        self.gpa = float(gpa)
        self.semester = int(semester)

    def set_id(self, value):
        self.__id = value

    def set_first_name(self, value):
        self.__fn = value

    def set_last_name(self, value):
        self.ln = value

    def set_gpa(self, value):
        self.gpa = value
    
    def set_semester(self, value):
        self.semester = value

global students
students = {}
id = []

def main_menu():
    # A function that displays the main menu and provides a choice for the user to main. It returns that choice so the overal program knows where to send the user
    print("What would you like to do today?\n-Add a student? \t\t\t\tenter 1\n-Search for a student? \tenter 2 \n-Edit a Students Info? \t\t\t\tenter 3 \n-Remove a student? \t\t\t\tenter 4\n-Print the Student List? \t\t\tenter 5\n-Save the data to a file? \t\t\t enter 6")
    choice = input(": ")
    return choice #sends the input back to the program file for the menu there
       
def run_add(): #- Removed students (dictionary) argument as it has been made a global variable
    # A function that runs the add students function, until the user decides they are done
    while True:
        add_student()
        add = input("Do you want to add more students? y(yes)/n(no)\n").lower().strip()
        if add in ('y', 'yes'):
            continue
        else:
            break   
    
def run_search(): 
    # A function that runs the search function, until the user decides they are done
    while True: # A while statement is used so that we can take input as many times as the user would like to use the program as well as to 
        id_str = input("To search using the ID enter 1. To search using the first name and last name enter 2. Enter -1 to return to the previous menu. \n")
        if id_str == '1': #checking if the user wants to search using the ID.
            print("Please enter the ID of the student:")
            for id in Students:
                print("Student found", students)
        elif id_str == '2': #checking if the user wants to search using the first and last names.
            firstname = input("Please enter the first name of the student:\n")
            lastname = input("Please enter the last name of the student:\n")
            if firstname and lastname in Students:
                print("Student found", students)
            else:
                print("Student not found")
        elif id_str == '-1': #checking if the user wants to return to the previous menu.
            break
        elif not id_str.isdigit(): #checks if user input is a number or not, if not then loop continues
            print("Invalid input. Please enter a valid student ID.")
        else:
            id = int(id_str) #now that checks have been done to make sure that the number above is a valid input its now possible to convert input to a int
            search(id) #runs the search function with the converted input
           
def run_edit(): 
    # a function to run the edit student function until the user decides they are done
    while True:
        edit_name()
        edit = input("Do you wish to edit another students name? y(yes)/n(no)\n ").lower()
        if edit == 'y' or edit == 'yes':
           continue
        else:  
            break

def run_remove(): 
    # a function to run the remove student function to remove as many students as desired | Also nearly identical to the function above
    while True:
        remove()
        rem = input("Do you want to remove another student? y(yes)/n(no)\n")
        if rem in ('y', 'yes'):
            continue
        else:
            break
    
def add_student(): 
    #Adds the student information to a list - Removed students (dictionary) argument as it has been made a global variable
    valuelist = []
    id = int(input("Enter id of the student, followed by the student's information.\nID:\n")) #this will break if not given a int type input
    #removed while loop as it was redundant and breaking the program by locking it into the add while loop. 
    if id in students:
        print("Incorrect ID. ID already exist in the system") #prevents user from remaking a current student
        display_dict() #shows the current dictionary so that the user can see any taken id's
    else:
        firstname = input("First name:\n")
        lastname = input("Last name:\n")
        gpa = input("GPA:\n")
        semester = input("Semester:\n")
        s1 = Students(id, firstname, lastname, gpa, semester) #adding all inputs to a list to add to the students dictionary
        students[id] = s1 # adds a new id(key)
        print("Student Enrolled in the system.") #user confirmation in two parts, telling the user that its added and showing the user the new addition
        display_specific(id) 
    # Added a loop to check if the id is already in use
    if valuelist in students:
        print("The student's already enrolled. No action is required..")

    
def display_dict(): 
    #for displaying all the keys and the related values within the students dictionary
    print("The current record of students in this class are as follows:")
    for id in students:
         print("Student ID:",str(id) + ",", "Name:",f"{students[id][0]}" + ",", "GPA:",f"{students[id][1]}"+ ",", "Semester:",f"{students[id][2]}")

def display_specific(id):
    print("Student ID:",str(id) + ",", "Name:",f"{students[id][0]}" + ",", "GPA:",f"{students[id][1]}"+ ",", "Semester:",f"{students[id][2]}")
# Made it so the display changes to be on one line, but still looks clean and you can understand it
# ID needs to be converted to a string as you cant add an int and a string. just to make the commas work. using end = "," adds way too many commas and makes the text look ugly

def search(id): 
    # Searches for a student based off of their ID 
    if id in students:
        print("Student found")
        display_specific(id) # displaying the student info consistently by using a display function
    else:
        print("Student not in Directory") #error message

def remove():
    # Will remove all information on a student based off of the ID that is inputted
    id = int(input("Enter the ID of the student you want to remove from the Students' Registry:\n")).strip() #gets id from user, will break program if it isn't an integer input though
    if id in students: #checks if the id is in the students dictionary
        del students[id] #removes the student from the dictionary
        print("Student Removed") #confirmation of removal
    else:
        print("Student not in directory") #error message

def edit_name(): 
    # Edits only the name of a student in the program based off the ID that is inputed
    num = int(input("Enter the id of the student. Enter -1 to return to the previous menu.\n")) #gets id from user, will break program if it isn't an integer input though
    if num in students: #checks if the id is in the students dictionary
        firstname = input("First name:\n")
        students[num][0] = firstname
        lastname = input("Last name:\n")
        students[num][1] = lastname
        gpa = input("GPA:\n")
        students[num][2] = gpa
        semester = input("Semester:\n")
        students[num][3] = semester 
        print("Student's new info is", students)
        return
    else:
        print("Id does not exist in directory") #error message

def save_info():
    fid = open(file_name, 'r')
    

def load():
    fid = open(file_name, 'r')
    lines = fid.readlines