global students
students = {}
id = []

def main_menu():
    print("What would you like to do today?\n-Find a student? \t\t\t\tenter 1\n-Edit a student's name using student ID? \tenter 2 \n-Add a new student? \t\t\t\tenter 3 \n-Remove a student? \t\t\t\tenter 4")
    choice = input(": ")
    return choice #sends the input back to the program file for the menu there
       
def run_add(): #- Removed students (dictionary) argument as it has been made a global variable
    while True:
        add_student()
        add = input("Do you want to add a new student?y(yes)/n(no)\n").lower().strip()
        if add in ('y', 'yes'):
            continue
        else:
            break   
    
def run_search(): 
    while True: # A while statement is used so that we can take input as many times as the user would like to use the program as well as to 
        id_str = input("Enter the student ID you want to search for, enter -1 to return to the main menu: \n")
        if id_str == '-1': #checking if the user wants to return to the main menu first 
            break
        elif not id_str.isdigit(): #checks if user input is a number or not, if not then loop continues
            print("Invalid input. Please enter a valid student ID.")
        else:
            id = int(id_str) #now that checks have been done to make sure that the number above is a valid input its now possible to convert input to a int
            search(id) #runs the search function with the converted input
           

def run_edit(): #a function to run the edit student function until the user decides they are done
    while True:
        edit_name()
        edit = input("Do you wish to edit another students name? y(yes)/n(no)\n ").lower()
        if edit == 'y' or edit == 'yes':
           continue
        else:  
            break

def run_remove(): # a function to run the remove student function to remove as many students as desired | Also nearly identical to the function above
    while True:
        remove()
        rem = input("Do you want to remove another student? y(yes)/n(no)\n")
        if rem in ('y', 'yes'):
            continue
        else:
            break
    

def add_student(): #Adds the student information to a list - Removed students (dictionary) argument as it has been made a global variable
    #removed while loop as it was redundant and breaking the program by locking it into the add while loop. 
    valuelist = []
    id = int(input("Enter id of the student, followed by the student's information.\nID:\n")) #this will break if not given a int type input
    if id in students:
        print("Student ID is already in the Registry") #prevents user from remaking a current student
        display_dict() #shows the current dictionary so that the user can see any taken id's
    else:
        name = input("Name:\n")
        gpa = input("GPA:\n")
        semester = input("Semester:\n")
        valuelist = [name, gpa, semester] #adding all inputs to a list to add to the students dictionary
        students[id] = valuelist # adds a new id(key)
        print("Student added") #user confirmation in two parts, telling the user that its added and showing the user the new addition
        display_specific(id) 
# Added a loop to check if the id is already in use
    

def display_dict(): #for displaying all the keys and the related values within the students dictionary
    print("The current record of students in this class are as follows:")
    for id in students:
         print("Student ID:",str(id) + ",", "Name:",f"{students[id][0]}" + ",", "GPA:",f"{students[id][1]}"+ ",", "Semester:",f"{students[id][2]}")

def display_specific(id):
    print("Student ID:",str(id) + ",", "Name:",f"{students[id][0]}" + ",", "GPA:",f"{students[id][1]}"+ ",", "Semester:",f"{students[id][2]}")
# Made it so the display changes to be on one line, but still looks clean and you can understand it
# ID needs to be converted to a string as you cant add an int and a string. just to make the commas work. 

def search(id): # Searches for a student based off of their ID 
    if id in students:
        print("Student found")
        display_specific(id) # displaying the student info consistently by using a display function
    else:
        print("Student not in Directory") #error message

def remove():
    id = int(input("Enter the ID of the student you want to remove from the Students' Registry:\n")).strip() #gets id from user, will break program if it isn't an integer input though
    if id in students: #checks if the id is in the students dictionary
        del students[id] #removes the student from the dictionary
        print("Student Removed") #confirmation of removal
    else:
        print("Student not in directory") #error message

def edit_name(): 
    num = int(input("Enter the id of the student. Enter -1 to return to the previous menu.\n")) #gets id from user, will break program if it isn't an integer input though
    if num in students: #checks if the id is in the students dictionary
        new_name = input("Enter the new name of the student:\n") 
        students[num][0] = new_name #changes the name inside the list inside the dictionary to be the new name 
        print("Student name modified for the student with id", num) #confirmation message 
        print("Students new name is", new_name) #afirming the user with evidence
    else:
        print("Id does not exist in directory") #error message