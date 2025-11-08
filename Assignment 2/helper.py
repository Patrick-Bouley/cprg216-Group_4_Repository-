id = ()
name = ()
gpa = ()
semester = ()
students = [id, name, gpa, semester]

def show_menu(): #Must take no arguments, just prints the main menu
    print("welcome to the software")
    print("Please choose from the following options:")
    print("-Add a new student: 1")
    print("-Modify an existing student: 2")
    print("-Remove a student: 3")
    print("-Add a new student: 4")
    print("-Exit")
    option = (input())
    # This is just what he did in the example, I dont know if this is correct
    
# Add, Remove, Edit_name, Search, all sound like they need to bve their own seperate menues with dialog to direct what the person needs to do, 
# the run commands seem to take the student list (the one that holds everything (name, id, gpa, semester), and based off the option we want, will put that through the function we create)

def add():
    get_id = input("Enter the ID of the student, followed by the students information/n" "ID: ")
    id.append(get_id)
    get_name = input("Name:/n")
    name.append(get_name)
    get_gpa = input("GPA:/n")
    gpa.append(get_gpa)
    get_semester = input("Semester:/n")
    semester.append(get_semester)
    # I assume we will have to append this new name into the list of students, while making sure they arent already added
    # Takes a list of each input, which are (Name), (ID), (GPA), (Semester)
    

def edit_name():
    input("Enter the ID of the student. Enter -1 to return to the previous menu./n")
    for id in students:
        students[name] = input("Enter the name of the new Student:/n")
    # Takes the Students name from the List and student ID as input, and the new name to be changed with the one selected 
   
def remove():
    input("Enter the ID of the student that you want to remove from the students' registry./n")
    for id in students:
        del students[name, id, gpa, semester]
    # Takes the students and id lists as parameters, and removes all info of that student from the lists that match the name/id

def search(id):
    input("Enter the ID of the student. Enter -1 to return to the previous menu./n")
    for id in students:
        print("Student Found/n", id, name, gpa)
    else:
        print("Student not found in registy.")
    input("Would you like to continue(y/yes), or exit the program(n/no)?")
    #Takes the names/ids as arguments, then searches to see if that student exsists in the lists

def run_search(students):
    #takes the entierty of the students list as an argument and shows the search menu

def run_edit(students):
    #Takes the entirety of the students list as an argument, and shows the edit menu

def run_add(students):
    #Takes the entirety of the students list as an argument and shows the add menu

def run_remove(students):
    # #Takes the entirety of the students list as an argument and shows the remove menu