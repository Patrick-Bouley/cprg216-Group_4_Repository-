global students
students = {}
id = []

def main_menu(): # if main menu has the loops in it, can we also make it have the main continue option for using the whole program? 


    print("Welcome to the students record program What would you like to do today?\n-Find a student? \t\t\t\tenter 1\n-edit a student's info using student ID? \tenter 2 \n-Add a new student? \t\t\t\tenter 3 \n-Remove a student? \t\t\t\tenter 4 ")
    choice = input(": ")
    if choice == "1":
        run_search()
    elif choice == '2':
        run_edit()
    elif choice == '3':
        run_add()
    elif choice == '4':
        run_remove()
    else:
        print("Thanks for using the program")
    

def run_add(): #- Removed students (dictionary) argument as it has been made a global variable
    add = 'yes'
    while add == 'yes' or add == 'y':
        add_student()
        add = input("Do you want to add a new student?y(yes)/n(no)").lower()
        if add != "y" or add != "yes":
            break
    main_menu()

def run_search(): # - Removed students (dictionary) argument as it has been made a global variable
    find = 1
    while find == 1:
        find = int(input("Enter the ID of the student, Enter -1 to return to previous menu\n"))
        if find != -1:
            search(find)
        else:
            break
    main_menu()
        

def run_edit(): #- Removed students (dictionary) argument as it has been made a global variable
    edit = 1
    while edit == 1 :
        edit = int(input("Enter the ID of the student, Enter -1 to return to previous menu\n"))
        if edit != -1:
            edit_name(edit)
        else:
            break
    main_menu()
    

def run_remove():   #- Removed students (dictionary) argument as it has been made a global variable
    delete = 'yes'
    while delete == 'yes' or delete == 'y':
        remove()
        delete = input("Do you want to remove more students?y(yes)/n(no)").lower()
        if delete != "y" or delete != "yes":
            break
    main_menu()
    


def add_student(): #Adds he student information to a list - Removed students (dictionary) argument as it has been made a global variable
    #removed while loop as it was redundant and breaking the program by locking it into the add while loop. 
    id = int(input("input a id for a student:\n"))
    x=3
    valuelist = []
    print("enter a name, gpa, then semester:")
    while x>0:
        x -= 1
        y = input("input:")
        valuelist.append(y) 
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