global students
students = {}
id = []
name = []
gpa = []
semester = []

def main_menu(): # if main menu has the loops in it, can we also make it have the main continue option for using the whole program? 


    print("Welcome to the students record program What would you like to do today?\n-Find a student? \t\t\t\tenter 1\n-edit a student's info using student ID? \tenter 2 \n-Add a new student? \t\t\t\tenter 3 \n-Remove a student? \t\t\t\tenter 4 \n-Exit? \t\t\t\t\t\tenter -1")
    choice = input(": ")
    if choice == "1":
        run_search()
    elif choice == '2':
        run_edit()
    elif choice == '3':
        run_add()
    elif choice == '4':
        run_remove()
    elif choice == '-1':
        print("Exiting, thanks for using the program.")
    else:
        print("Invalid input, please try again.")
        main_menu()
    

def run_add(): #- Removed students (dictionary) argument as it has been made a global variable
    while True:
        add_student()
        add = input("Do you want to add a new student?y(yes)/n(no)").lower().strip()
        if add in ('y', 'yes'):
            continue
        else:
            main_menu()
            break
            
    

def run_search(): # - Removed students (dictionary) argument as it has been made a global variable
    while True:
        id_str = input("Enter the student ID you want to search for, enter -1 to return to the main menu: ")
        if id_str == '-1':
            main_menu()
            break
        if not id_str.isdigit():
            print("Invalid input. Please enter a valid student ID.")
            continue
        id = int(id_str)
        search(id)
       

def run_edit(): #- Removed students (dictionary) argument as it has been made a global variable
    while True:
        edit_name()
        new_name = input("Enter the new name for the student: ")
        if id not in students:
            print("Student ID not found.")
            return
        else:  
            students[id] = new_name
            print("Student name updated.")
            main_menu()
            break
           

def run_remove():   #- Removed students (dictionary) argument as it has been made a global variable
    while True:
        remove()
        rem = input("Do you want to remove another student? y(yes)/n(no)")
        if rem in ('y', 'yes'):
            continue
        else:
            break
        


def add_student(): #Adds the student information to a list - Removed students (dictionary) argument as it has been made a global variable
    #removed while loop as it was redundant and breaking the program by locking it into the add while loop. 
    id = int(input("input a id for a student:\n"))
    print("enter a name, gpa, then semester:")
    name = input("Name:")
    gpa = input("GPA:")
    semester = input("Semester:")
    valuelist = (name, gpa, semester)
    students[id] = valuelist # adds a new id(key)
    print("Student added")
    display_specific(id)
    return students
    

def display_dict(): #for displaying all the keys and the related values within the students dictionary
    print("The current record of students in this class are as follows:")
    for id in students:
        print("Student ID:",id, "\nName:",f"{students[id][0]}","\nGPA:",f"{students[id][1]}","\nSemester:",f"{students[id][2]}")
        
def display_specific(id):
    print("Student ID:",id, "\nName:",f"{students[id][0]}","\nGPA:",f"{students[id][1]}","\nSemester:",f"{students[id][2]}")


def search(id): # Searches for a student based off of their ID 
    if id in students:
        print("Student found")
        display_specific(id)
    else:
        print("Student not in Directory")

def remove():
    num2 = input("Enter the ID of the student you want to remove from the Students' Registry")
    for num2 in students:
        del students[num2]
        print("Student Removed")

def edit_name():
    num = input("Enter the id of the student you wish to edit: ")
    new_name = input("Enter the new name for the student with this id: ")
    print("Student name modified for the student with id", num)
    print("Students new name is", new_name)



main_menu()
# operate = True #the next few lines are to run the program until the user doesn't care.
# while operate == True:
#     main_menu()
#     operate = input("Do you want to keep using the program?")
#     if operate == "yes" or operate == "y":
#         operate = True
#     else:
#         break

#students = add_student()

#search()

#  for name in dataStorage:
#         print("\t",name, f"{dataStorage[name]:.2f}")
