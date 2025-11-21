global students
students = {}
id = []

def main_menu():
    print("Welcome to the students record program.\nWhat would you like to do today?\n-Find a student? \t\t\t\tenter 1\n-Edit a student's name using student ID? \tenter 2 \n-Add a new student? \t\t\t\tenter 3 \n-Remove a student? \t\t\t\tenter 4 \n-Exit? \t\t\t\t\t\tenter -1")
    choice = input(": ")
    if choice == "1":
        run_search()
    elif choice == '2':
        run_edit()
    elif choice == '3':
        run_add(students)
    elif choice == '4':
        run_remove()
    elif choice == '-1':
        print("Exiting, thanks for using the program.")
    else:
        print("Invalid input, please try again.")
        main_menu()

def run_add(): #- Removed students (dictionary) argument as it has been made a global variable
    while True:
        add_student(students)
        add = input("Do you want to add a new student?y(yes)/n(no)").lower().strip()
        if add in ('y', 'yes'):
            continue
        else:
            # main_menu()
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
    edit = 1
    while edit == 1 :
        edit = int(input("Enter the ID of the student, Enter -1 to return to previous menu\n"))
        if edit != -1:
            edit_name(edit)
        else:
            break
    # main_menu()
    

def run_remove():   #- Removed students (dictionary) argument as it has been made a global variable
    delete = 'yes'
    while delete == 'yes' or delete == 'y':
        remove()
        delete = input("Do you want to remove more students?y(yes)/n(no)").lower()
        if delete != "y" or delete != "yes":
            break
    # main_menu()
    
 
def add_student(students): #Adds the student information to a list - Removed students (dictionary) argument as it has been made a global variable
    #removed while loop as it was redundant and breaking the program by locking it into the add while loop. 
    valuelist = []
    id = int(input("input a id for a student:\n"))
    if id in students:
        print("ID already in system")
        add_student()
    else:
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
        print("Student ID:",str(id) + ",", "Name:",f"{students[id][0]}" + ",", "GPA:",f"{students[id][1]}"+ ",", "Semester:",f"{students[id][2]}")
        # I removed the "\n" between the information pieces, just to align it more with the assignment output example. I dont know how exact he requires us to be, but we can re add them after I ask the teacher haha
        # Did the same with the Display Specific function below

def display_specific(id):
    print("Student ID:",str(id) + ",", "Name:",f"{students[id][0]}" + ",", "GPA:",f"{students[id][1]}"+ ",", "Semester:",f"{students[id][2]}")

# These two display functions are optional but do help make the code look better if we implement them properly. We do have to format the prining in the menues, so these 2 functions help with that

def search(id): # Searches for a student based off of their ID 
    if id in students:
        print("Student found")
        display_specific(id)
    else:
        print("Student not in Directory")

def remove():
    num = input("Enter the ID of the student you want to remove from the Students' Registry")
    for num in students:
        del students[id]
        print("Student Removed")

def edit_name():
    num = input("Enter the id of the student you wish to edit")
    id[num] = input("Enter the new name for the student with this id")
    print("Student name modified for the student with id", + num)
    print("Students new name is ", + id[num])



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