#file copied and adjusted from modified_test.py
students = {
    100:['Alice', 3.6,3],
    101:['Bob', 3.2,2],
    102:['Charlie', 3.8,4],
    103:['Diana', 3.5,1],
    104:['Ethan', 3.9,3],
    105:['Fiona', 3.4,2],
    106:['George', 3.1,4],
    107:['Hannah', 3.7,1],
    108:['Ian', 3.0,2],
    109:['Jane', 3.85,3],
    110:['Kevin', 3.65,4],
    111:['Laura', 3.45,1],
    112:['Mike', 3.25,2],
    113:['Nina', 3.95,3],
    114:['Oscar', 3.15,4],
    115:['Paula', 3.55,1],
    116:['Quinn', 3.75,2],
    117:['Rachel', 3.35,3],
    118:['Sam', 3.05,4],
    119:['Tina', 3.9,1],
    120:['Uma', 3.6,2],
    121:['Vince', 3.8,3],
    122:['Wendy', 3.4,4]
    }
id = []


def main_menu():
    print("Welcome to the students record program What would you like to do today?\n-Find a student? \t\t\t\tenter 1\n-Edit a student's name using student ID? \tenter 2 \n-Add a new student? \t\t\t\tenter 3 \n-Remove a student? \t\t\t\tenter 4 \n-Exit? \t\t\t\t\t\tenter -1")
    choice = input(": ")
    if choice == "1" or choice == 'find': 
        run_search()
    elif choice == '2' or choice == 'edit':
        run_edit()
    elif choice == '3' or choice == 'add':
        run_add()
    elif choice == '4' or choice == 'remove':
        run_remove()
    elif choice == '5': #easter egg to show the whole dictionary
        display_dict()
    elif choice in ('-1', 'exit', 'Exit','quit','Quit', 'stop','Stop'): #added more keywords here to prevent mistakes
        # print("Exiting, thanks for using the program.")
        exit()
    else: 
        print("Invalid input, please try again.")
    

def run_add(): #- Removed students (dictionary) argument as it has been made a global variable
    while True:
        add_student()
        add = input("Do you want to add a new student?y(yes)/n(no)\n").lower().strip()
        if add in ('y', 'yes'):
            continue
        else:
            break
            

def run_search(): # - Removed students (dictionary) argument as it has been made a global variable
    while True: #while loop included to prevent crashing the program and for catching input errors
        id_str = input("Enter the student ID you want to search for, enter -1 to return to the main menu: \n")
        if id_str == '-1':
            break
        elif not id_str.isdigit():
            print("Invalid input. Please enter a valid student ID.")
            continue
        id = int(id_str)
        search(id)
    

def run_edit(): #- Removed students (dictionary) argument as it has been made a global variable
    while True: #while loop included to prevent crashing the program and for catching input errors
        edit_name()
        edit = input("Do you wish to edit another students name? y(yes)/n(no)\n ").lower()
        if edit in ('y', 'yes', '1'):
           continue
        else:  
            break


def run_remove():   #- Removed students (dictionary) argument as it has been made a global variable
    while True: #while loop included to prevent crashing the program and for catching input errors
        remove()
        rem = input("Do you want to remove another student? y(yes)/n(no)")
        if rem in ('y', 'yes','1'):
            continue
        else:
            break
        

def add_student(): #Adds the student information to a list - Removed students (dictionary) argument as it has been made a global variable
    #removed while loop as it was redundant and breaking the program by locking it into the add while loop. 
    valuelist = []
    id = int(input("input a id for a student:\n"))
    if id in students:
        print("Student ID is already in the Registry")
        display_dict()
    else:
        print("enter a name, gpa, then semester:")
        name = input("Name:")
        gpa = input("GPA:")
        semester = input("Semester:")
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
    input("To continue press any key. . .")


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
    id = int(input("Enter the ID of the student you want to remove from the Students' Registry: \n"))
    if id in students:
        del students[id]
        print("Student Removed")
    else:
        print("Student not in directory")


def edit_name():
    while True: #while loop included to prevent crashing the program and for catching input errors
        try: # try function to attempt to get a valid int input for the student id (in this case num)
            num = int(input("Enter the id of the student you wish to edit: "))
            if num in students:
                break # this breakes out of the first while loop to continue on to the next one 
            else:
                print("Error, Please Try Again, ID not found in system.")
        except ValueError:
            print("please try again")
    while True:  #while loop included to prevent crashing the program and for catching input errors
        new_name = input("Enter the new name for the student with this id: ")

# ____________________________________ TO REMOVE EASTER EGG DELETE BELOW HERE AND ABOVE NEXT LINE ______________________________________

        if new_name == "": # if user doesn't add a name I thought this might be an interesting easter egg of more content
            print("Welcome to the hidden menu! You now have the option to change the id, gpa, or semester of the student as well.") #letting user know its an easter egg
            display_specific(num) 
            field = input("Which attribute would you like to edit? (1/id|2/gpa|3/semester): ").lower()
            if field in ('1', 'id'):
                new_id = int(input("Enter the new ID for the student: "))
                if new_id in students: #prevent an overwrite error
                    print("This ID is already in use. Edit aborted.")
                else:
                    students[new_id] = students.pop(num) #removes the current id while assigning the previous info to the new id
                    print(f"Student ID changed from {num} to {new_id}.") #notifying user of change made
                    display_specific(new_id) 
                    return
            elif field in ('2', 'gpa'):
                new_gpa = input("Enter the new GPA for the student: ")
                students[num][1] = new_gpa #editing the specific value of the list inside the dictionary 
                print(f"Student GPA updated to {new_gpa}.")
                display_specific(num)
                return
            elif field in ('3', 'semester'):
                new_semester = input("Enter the new semester for the student: ")
                students[num][2] = new_semester #editing the specific value of the list inside the dictionary 
                print(f"Student semester updated to {new_semester}.")
                display_specific(num)
                return
            else:
                print("Invalid field selection. Edit aborted.")
        else: #back to the actual required code which does the name edit when a "proper name" is given (proper used extremely loosely lol)

#___________________________________ TO REMOVE EASTER EGG DELETE ABOVE THIS LINE ______________________________________
#                                         (ALSO DE-INDENT FOLLOWING 4 LINES)



            students[num][0] = new_name
            print("Student name modified for the student with id", num)
            print("Students new name is", new_name)
            return



while True:
    main_menu() #quick while loop to run the program simply for testing purposes