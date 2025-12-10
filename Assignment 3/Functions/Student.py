class Students:
    def __init__(self, id, first_name, last_name, gpa, semester):
        self.__id__ = id
        self.__fn__ = first_name
        self.__ln__ = last_name
        self.__gpa__ = gpa
        self.__semester__ = semester
 
    def set_id(self, value):
        self.__id__ = value
 
    def set_first_name(self, value):
        self.__fn__ = value
 
    def set_last_name(self, value):
        self.__ln__ = value
 
    def set_gpa(self, value):
        self.__gpa__ = value
   
    def set_semester(self, value):
        self.__semester__ = value
 
global students
students = {}
id = ()
 
def main_menu():
    # A function that displays the main menu and provides a choice for the user to main. It returns that choice so the overal program knows where to send the user
    print("What would you like to do today?\n-Add a student? \t\t\t\tenter 1\n-Search for a student? \t\t\t\tenter 2 \n-Edit a Students Info? \t\t\t\tenter 3 \n-Remove a student? \t\t\t\tenter 4\n-Print the Student List? \t\t\tenter 5\n-Save students to file? \t\t\tenter 6")
    choice = input(": ")
    return choice #sends the input back to the program file for the menu there
       
def run_add(): #- Removed students (dictionary) argument as it has been made a global variable
    # A function that runs the add students function, until the user decides they are done
    while True:
        add_student()
        add = input("Do you want to add more students? y(yes)/n(no)\n").lower().strip()
        if add in ('y', 'yes'):
            continue
        else:
            break  
   
def run_search():
    # A function that runs the search function, until the user decides they are done
    while True: # A while statement is used so that we can take input as many times as the user would like to use the program as well as to
        id_str = input("To search using the ID enter 1. To search using the first name and last name enter 2. Enter -1 to return to the previous menu. \n")
        if id_str == '1': #checking if the user wants to search using the ID.
            print("Please enter the ID of the student:")
            for id in Students:
                print("Student found", students)
        elif id_str == '2': #checking if the user wants to search using the first and last names.
            firstname = input("Please enter the first name of the student:\n")
            lastname = input("Please enter the last name of the student:\n")
            if firstname and lastname in Students:
                print("Student found", students)
            else:
                print("Student not found")
        elif id_str == '-1': #checking if the user wants to return to the previous menu.
            break
        elif not id_str.isdigit(): #checks if user input is a number or not, if not then loop continues
            print("Invalid input. Please enter a valid student ID.")
        else:
            id = int(id_str) #now that checks have been done to make sure that the number above is a valid input its now possible to convert input to a int
            search(id) #runs the search function with the converted input
           
def run_edit():
    # a function to run the edit student function until the user decides they are done
    while True:
        edit_name()
        edit = input("Do you wish to edit another students name? y(yes)/n(no)\n ").lower()
        if edit == 'y' or edit == 'yes':
           continue
        else:  
            break
 
def run_remove():
    # a function to run the remove student function to remove as many students as desired | Also nearly identical to the function above
    while True:
        remove()
        rem = input("Do you want to remove another student? y(yes)/n(no)\n")
        if rem in ('y', 'yes'):
            continue
        else:
            break
   
def add_student():
    # Adds students to a directory, based off the class system above
    id = int(input("Enter id of the student, followed by the student's information.\nID:\n"))
    #this will break if not given a number for an input
    if id in students: #prevents user from using the same ID to create multiple students.
        print("Incorrect ID. ID already exist in the system")
        return
    student = Students(id, input("First name:\n"), input("Last name:\n"), input("GPA:\n"), input("Semester:\n"))
    students[id] = student
    # for id in student:
    #     student = students[id]
    #     if (Students.__fn__ == first_name and
    #         Students.__ln__ == last_name):
    #         print("Error: A student with that first and last name already exists.")
    #         return
            # This checks to see if the first and last name are in use at the same time. students can have the same first name with a different last name, or vise versa
    print("Student Enrolled in the system.") #user confirmation in two parts, telling the user that its added and showing the user the new addition
    display_specific(id)
 
def display_dict():
    #for displaying all the keys and the related values within the students dictionary
    print("The current record of students in this class are as follows:")
 # Loop through every student ID stored in the dictionary
    for id in students: # Get each private attribute using the specific object in students.
        first = students[id]._Students__fn__
        last = students[id]._Students__ln__
        gpa = students[id]._Students__gpa__
        sem = students[id]._Students__semester__
        print(f"ID: {id}, Name: {first} {last}, GPA: {gpa}, Semester: {sem}")
        # I decided to change how the Information is formated,
 
 
def display_specific(id):
    # Make sure the ID exists before displaying
    if id not in students:
        print("Student not found.")
        return
    first = students[id].__fn__
    last = students[id].__ln__
    gpa = students[id].__gpa__
    sem = students[id].__semester__
 
    # Display the student info clearly
    print(f"Student ID: {id}", f"Name: {first} {last}", f"GPA: {gpa}", f"Semester: {sem}", sep = ", ")
 
 
def search(id):
    # Searches for a student based off of their ID
    if id in students:
        print("Student found")
        display_specific(id) # displaying the student info consistently by using a display function
    else:
        print("Student not in Directory") #error message
 
def remove():
    # Will remove all information on a student based off of the ID that is inputted
    id = int(input("Enter the ID of the student you want to remove from the Students' Registry:\n")) #gets id from user, will break program if it isn't an integer input though
    if id in students: #checks if the id is in the students dictionary
        del students[id] #removes the student from the dictionary
        print("Student Removed") #confirmation of removal
        save_info() # This will make sure the file gets changed to match what has been removed.
    else:
        print("Student not in directory") #error message
 
def edit_name():
    # Ask the user for a student ID
    id = int(input("Enter the ID of the student you want to edit:\n"))
    # Checks to make sure the ID is in the system first
    if id not in students:
        print("That ID does not exist in the system.")
        return
    # Ask for updated information, in relation to the objects in Students
    new_first = input("Enter the new first name:\n")
    new_last = input("Enter the new last name:\n")
    new_gpa = float(input("Enter the new GPA:\n"))
    new_sem = int(input("Enter the new semester:\n"))
    # We then use 'set' to update what those objects should be for that specific student bassed on the ID
    students[id].set_first_name(new_first)
    students[id].set_last_name(new_last)
    students[id].set_gpa(new_gpa)
    students[id].set_semester(new_sem)
    print("Student information updated successfully.")
    save_info()
 
def save_info():
    with open("Saved_data.txt", "w") as fid:
        # Choosing to write and not append. So that everytime we save the info, it updates the whole file, instead of just adding it to the bottom.
        for id in students:
            line = (f"{id}|"f"{students[id]._Students__fn}|"f"{students[id]._Students__ln}|"f"{students[id]._Students__gpa}|"f"{students[id]._Students__semester}\n")
            # This writes the line in a way that allows the Load function to read them properly. Cause I made that info all be on one line.
            fid.write(line)
    print("Data saved successfully.")
# I believe we have to write to the file, cause apending would keep adding students, and eventually become out of sync with the file if students keep getting removed.
   
 
def load():
    students.clear()
    #We use this to clear the current memory (As in the program that just opened) and clears its cache, before loading all the info from the file. helps to prevent duplicates if we are constanly starting/stopping the program
    with open("Saved_data.txt", "r") as fid: # We want to read the file and take that data, so we use "r"
        # Using with makes it so we dont have to open and close the file, it does it automatically.
        for line in fid: # Since we are saving each student to one line. each line represents one student. This should loop through each line and take the data that is required.
            id, fn, ln, gpa, sem = line.strip().split("|") # Just using this to seperate the info for now, We might not need this at all
            students[int(id)] = Students(id, fn, ln, gpa, sem)
            # The file should automatically add these to the private attributes.
            # made id an int because thats how we have been making it a key for our dictionary
    print("Student data loaded successfully.")