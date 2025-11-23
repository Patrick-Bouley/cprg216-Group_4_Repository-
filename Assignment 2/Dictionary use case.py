import os
global students
students = {120:["jimy",3,3],121:["john",2,2]}
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
    
def specific_edit():
    student_id = int(input("Which student would you like to edit?\nID:"))
    if student_id in students[student_id]:
        print("OK, what would you like to edit for student",student_id,"?\n1:Their name | Current Name:",students[student_id][0],"\n2:Their GPA | Current GPA:",students[student_id][1],"\n:3:Their Semester | Current Semester:", students[student_id][2])
        choice = input(":")
        if choice == "1" or choice == "name" or choice == "Name":
            new_name = input("Please type the new name here:")
            students[student_id][0] = new_name
            print("Student",student_id,"has the name",students[student_id][0])
        elif choice == "2" or choice == "GPA" or choice== "gpa":
            new_gpa = input("Type New GPA here:")
            students[student_id][1] = new_gpa
            print("Student",student_id,"has the GPA of",students[student_id][1])           
        elif choice == "3" or choice == "Semester" or choice== "semester":
            new_gpa = input("Type New semester here:")
            students[student_id][2] = new_gpa
            print("Student",student_id,"has the semester",students[student_id][2])        
        else:
            print("your dum")
    else:
        print("please try again")
        specific_edit()
        

def run_remove():   #- Removed students (dictionary) argument as it has been made a global variable
    os.system("cls")
    delete = 'yes'
    while delete == 'yes' or delete == 'y':
        remove()
        delete = input("Do you want to remove more students?y(yes)/n(no)").lower()
        if delete != "y" or delete != "yes":
            break
    main_menu()
    


def add_student(): #Adds he student information to a list - Removed students (dictionary) argument as it has been made a global variable
    #removed while loop as it was redundant and breaking the program by locking it into the add while loop. 
    os.system("cls")
    id = int(input("input a id for a student:\n"))
    valuelist = []
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
    num = int(input("Enter the ID of the student you want to remove from the Students Registry"))
    try:
        print("You are trying to remove the student:",students[num][0], "\nif this is correct type their student number once again below")
        are_you_sure = int(input(":"))
        if are_you_sure == num:
            del students[num]
            print("Student Removed")
        else:
            print("Deletion Aborted")
    except:
        print("No student found")

def edit_name(edit): # made use of the edit variable from run_edit()
    print(edit)
    print("Enter the new name for the student with the id")
    new_name = input(":")
    students[edit][0] = new_name
    print("Student name modified for the student with id", edit)
    print("Students new name is", students[edit][0])



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