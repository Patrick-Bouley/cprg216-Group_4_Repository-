
global students
students = {}
id = []

def main_menu(): # if main menu has the loops in it, can we also make it have the main continue option for using the whole program? 


    print("Welcome to the students record program What would you like to do today?\n -Find a student? enter 1\n -edit a student's info using student ID? enter 2 \n-Add a new student? enter 3 \n-Remove a student? enter 4 ")
    choice = input(": ")
    if choice == 1:
        run_add()
    elif choice == 2:
        run_search()
    elif choice == 3:
        run_edit()
    elif choice == 4:
        run_remove()
    else:
        print("Thanks for using the program")
    

def run_add(students):
    add = 'yes'
    while add == 'yes' or add == 'y':
        add_student
        add = input("Do you want to add a new student?y(yes)/n(no)").lower()

def run_search(students):
    find = 1
    while find == 1:
        find = int(input("Enter the ID of the student, Enter -1 to return to previous menu\n"))
        if find != -1:
            search()
        

def run_edit(students):
    edit = 1
    while edit == 1 :
        edit = int(input("Enter the ID of the student, Enter -1 to return to previous menu\n"))
        if edit != -1:
            edit_name

def run_remove(students):
    delete = 'yes'
    while delete == 'yes' or delete == 'y':
        remove
        delete = input("Do you want to remove more students?y(yes)/n(no)").lower()
    


def add_student(students): #Adds he student information to a list
    
    add = 'yes' #assigning the add variable to yes to make the while loop run the first time 
    while add == "yes" or add == "y":
        id = int(input("input a id for a student:\n"))
        x=3
        valuelist = []
        print("enter a name, gpa, then semester:")
        while x>0:
            x -= 1
            y = input("input:")
            valuelist.append(y) 
        students[id] = valuelist # adds a new id(key)
    return students
    

def display_dict(students): #for displaying all the keys and the related values within the students dictionary
    for id in students:
        print(id, f"{students[id][0]}",f"{students[id][1]}",f"{students[id][2]}")
        
def display_specific(id):
    print(id, f"{students[id][0]}",f"{students[id][1]}",f"{students[id][2]}")


def search(): # Searches for a student based off of their ID 
    id = input("Enter the ID of the student, Enter -1 to return to previous menu\n")
    try: 
        print("Student found")
        display_specific(id)
    except:
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





students = add_student()

search()

#  for name in dataStorage:
#         print("\t",name, f"{dataStorage[name]:.2f}")
