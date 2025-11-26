global students
students = {}
id = []

def main_menu():
    print("What would you like to do today?\n-Find a student? \t\t\t\tenter 1\n-Edit a student's name using student ID? \tenter 2 \n-Add a new student? \t\t\t\tenter 3 \n-Remove a student? \t\t\t\tenter 4")
    choice = input(": ")
    return choice
       
def run_add(): #- Removed students (dictionary) argument as it has been made a global variable
    while True:
        add_student()
        add = input("Do you want to add a new student?y(yes)/n(no)\n").lower().strip()
        if add in ('y', 'yes'):
            continue
        else:
            break   
    
def run_search(): 
    while True:
        id_str = input("Enter the student ID you want to search for, enter -1 to return to the main menu: \n")
        if id_str == '-1':
            break
        elif not id_str.isdigit():
            print("Invalid input. Please enter a valid student ID.")
            break
        else:
            id = int(id_str)
            search(id)
           

def run_edit(): 
    while True:
        edit_name()
        edit = input("Do you wish to edit another students name? y(yes)/n(no)\n ").lower()
        if edit == 'y' or edit == 'yes':
           continue
        else:  
            break

def run_remove():
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
    id = int(input("Enter id of the student, followed by the student's information.\nID:\n"))
    if id in students:
        print("Student ID is already in the Registry")
        display_dict()
    else:
        name = input("Name:\n")
        gpa = input("GPA:\n")
        semester = input("Semester:\n")
        valuelist = [name, gpa, semester]
        students[id] = valuelist # adds a new id(key)
        print("Student added")
        display_specific(id)
        return students
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
        display_specific(id)
    else:
        print("Student not in Directory")

def remove():
    id = int(input("Enter the ID of the student you want to remove from the Students' Registry:\n"))
    if id in students:
        del students[id]
        print("Student Removed")
    else:
        print("Student not in directory")

def edit_name():
    num = int(input("Enter the id of the student. Enter -1 to return to the previous menu.\n"))
    if num in students:
        new_name = input("Enter the new name of the student:\n")
        students[num][0] = new_name
        print("Student name modified for the student with id", num)
        print("Students new name is", new_name)
    else:
        print("Id does not exist in directory")