id = []
name = []
gpa = []
semester = []
students = [id, name, gpa, semester] 

def show_menu(): #Must take no arguments, just prints the main menu
    print()
    print("Welcome to the Software !")
    print("Please choose from the following options:")
    print("-Add a new student: 1")
    print("-Modify an existing student: 2")
    print("-Remove a student: 3")
    print("-Search for a student: 4")
    print("-Exit: 5")
    return input("Choose an option from 1 to 5: ").strip()
    # This is just what he did in the example, I dont know if this is correct
    
# Add, Remove, Edit_name, Search, all sound like they need to bve their own seperate menues with dialog to direct what the person needs to do, 
# the run commands seem to take the student list (the one that holds everything (name, id, gpa, semester), and based off the option we want, will put that through the function we create)
def add():
    while True:
        print("Enter the id of the student, followed by their information:")
        get_id = int(input("id: "))
        get_name = input("name: ")
        get_gpa = float(input("gpa: "))
        get_semester = int(input("semester: "))

        id.append(get_id)
        name.append(get_name)
        gpa.append(get_gpa)
        semester.append(get_semester)
    
        print("Student added.")
        print(students)

        add_another_student = input("Do you want to add another student ? y(yes)/n(no)")
        if add_another_student not in ["y"or"yes"]:
            break
    # I assume we will have to append this new name into the list of students, while making sure they arent already added
    # Takes a list of each input, which are (Name), (ID), (GPA), (Semester)
    

def edit_name():
    while True:
        id = int(input("Enter the ID of the student, enter -1 to go back to the main menu"))
        if id == -1:
            break
        new_name = input("Enter the name of the new student")

        if edit_name:
            print("Student name with id", id, "changed successfully")
            print("Student's new name is", new_name)
        else:
            print("Student not found")
        #Takes the students and id lists as parameters, and allows the user to change the name of the student that matches the name/id
   
def remove():
    while True:
        removeid = input("Enter the ID of the student that you want to remove from the students' registry. Enter -1 to go back to the main menu")
        if removeid == -1:
            break
        for id in students:
            if removeid == id:
                del students[name, id, gpa, semester]
        # Takes the students and id lists as parameters, and removes all info of that student from the lists that match the name/id

def search():
    while True:
        id = int(input("Enter the ID of the student, enter -1 to go back to the main menu"))
        if id == -1:
            break
        for id in students:
            print("Student Found/n", id, name, gpa)
        else:
            print("Student not found in registy.")
    #Takes the names/ids as arguments, then searches to see if that student exsists in the list

def run_search(students):
    #takes the entierty of the students list as an argument and shows the search menu
    search()



def run_edit(students):
    #Takes the entirety of the students list as an argument, and shows the edit menu
    edit_name()


def run_add(students):
    #Takes the entirety of the students list as an argument and shows the add menu
    add()


def run_remove(students):
    # #Takes the entirety of the students list as an argument and shows the remove menu
    remove()

def run():
    while True:
        option = show_menu()
        if option == "1":
            run_add(students)
        elif option == "2":
            run_edit(students)
        elif option == "3":
            run_remove(students)
        elif option == "4":
            run_search(students)
        elif option == "5":
            print("Exiting.")
            break

run()
