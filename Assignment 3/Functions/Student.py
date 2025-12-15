import os

class Student:
    def __init__(self, id, first_name, last_name, gpa, semester):
        # Make all these private
        self.__id = id
        self.__fn = first_name
        self.__ln = last_name
        self.__gpa = gpa
        self.__semester = semester
 
    def set_id(self, value):
        self.__id = value
 
    def set_first_name(self, value):
        self.__fn = value
 
    def set_last_name(self, value):
        self.__ln = value
 
    def set_gpa(self, value):
        self.__gpa = value
   
    def set_semester(self, value):
        self.__semester = value
 
global students
students = {}

 
def main_menu():
    # A function that displays the main menu and provides a choice for the user to main. It returns that choice so the overal program knows where to send the user
    print("What would you like to do today?\n-Add a student? \t\t\t\tenter 1\n-Search for a student? \t\t\t\tenter 2 \n-Edit a Students Info? \t\t\t\tenter 3 \n-Remove a student? \t\t\t\tenter 4\n-Print the Student List? \t\t\tenter 5\n-Save students to file? \t\t\tenter 6")
    choice = input(": ")
    return choice #sends the input back to the program file for the menu there
       
def run_add():
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
    while True: 
        id_str = input("To search using the ID enter 1. To search using the first name and last name enter 2. Enter -1 to return to the previous menu. \n")
        if id_str == '1': #checking if the user wants to search using the ID.
            search_id = int(input("Please enter the ID of the student:\n"))
            ID_search(search_id)
        elif id_str == '2': #checking if the user wants to search using the first and last names.
            Name_search()
        elif id_str == '-1': #checking if the user wants to return to the previous menu.
            break
        elif not id_str.isdigit(): #checks if user input is a number or not, if not then loop continues
            print("Invalid input. Please enter a valid student ID.")
        
        
def run_edit():
    # a function to run the edit student function until the user decides they are done
    while True:
        edit_name()
        edit = input("Do you wish to edit another students info? y(yes)/n(no)\n").lower()
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
        print("ID already exists in the system")
        return
    student = Student(id, input("First name:\n"), input("Last name:\n"), float(input("GPA:\n")), int(input("Semester:\n")))
    for name in students.values():
        if (name._Student__fn.lower() == student._Student__fn.lower() and name._Student__ln.lower() == student._Student__ln.lower()):
            # We use .lower to avoid things like "John Smith" and "john smith" to be considered two different names.
            print("Error: That student Is already enrolled, no action is required.")
            return
            # This checks to see if the first and last name are in use at the same time. students can have the same first name with a different last name, or vise versa
    students[id] = student
    print("Student Enrolled in the system.") 
    # user confirmation in two parts, telling the user that its added and showing the user the new addition
    display_specific(id) 
    save_info() # Automatically saves that info to the file 
 
def display_all():
    #for displaying all the students in the save file
    if not students:
        print("No Students are currently saved to the system")
        return
        # This just checks to see if there even is anything saved to the file first, before trying to display something
    print("The current record of students in the system are as follows:")
# We put "for ID, student..."" here so it loops through all the IDs. to make sure all of them get read, with the information attactched to them.
    for id, student in students.items():
        # We use name mangling to gather the information needed. Its how we access the class variables from outside the class
        first = student._Student__fn
        last = student._Student__ln
        gpa = student._Student__gpa
        sem = student._Student__semester
        # This should loop through all the Students on the file
        print(f"ID: {id}, Name: {first} {last}, GPA: {gpa}, Semester: {sem}", sep = ",")

def display_specific(id):
    # Make sure the ID exists before displaying
    if id not in students:
        print("Student not found.")
        return
    # Name mangling for info
    first = students[id]._Student__fn
    last = students[id]._Student__ln
    gpa = students[id]._Student__gpa
    sem = students[id]._Student__semester
    # Display the student info clearly
    print(f"Student ID: {id}", f"Name: {first} {last}", f"GPA: {gpa}", f"Semester: {sem}", sep = ", ")
  
def ID_search(id):
    # Searches for a student based off of their ID
    if id in students:
        print("Student found")
        display_specific(id) # displaying the student info consistently by using a display function
    else:
        print("Student not in Directory") 

def Name_search():
    #Searches for a student based off their First and Last names 
    first = input("Please enter the first name of the student:\n").strip().lower()
    last = input("Please enter the last name of the student:\n").strip().lower()
    # We use Strip and lower to make sure its an easy comparision for the file. same reason we use lower in the function below as well
    for id, student in students.items():
        if (student._Student__fn.lower() == first and student._Student__ln.lower() == last):
            print("Student found")
            display_specific(id)
            return
    else:
        print("Student not found")
 
def remove():
    # Will remove all information on a student based off of the ID that is inputted
    id = int(input("Enter the ID of the student you want to remove from the Students' Registry:\n")) #gets id from user, will break program if it isn't an integer input though
    if id in students: 
        del students[id] #removes the student from the dictionary
        print("Student Removed") 
        save_info() # This will make sure the file gets changed to match what has been removed. Making sure there isnt any discrepancies/differences between whats saved, and currently on the program
    else:
        print("Student not in directory") #error message if there isnt a student with matching info
 
def edit_name():
    # Ask the user for a student ID
    id = int(input("Enter the ID of the student you want to edit:\n"))
    # The statement below checks to make sure the ID is in the system first
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
    display_specific(id)
    save_info()
    # Saves the info to the file automatically. just to update the information. Keeps the file consistent for what is stored in there and matches with the program that is currently running
 
def save_info():
    with open("Saved_students.txt", "w") as fid:
        # Choosing to write and not append. So that everytime we save the info, it updates the whole file, instead of just adding it to the bottom.
        for id in students:
            line = (f"{id}|"f"{students[id]._Student__fn}|"f"{students[id]._Student__ln}|"f"{students[id]._Student__gpa}|"f"{students[id]._Student__semester}\n")
            # This writes the line in a way that allows the Load function to read them properly. Because that info is all on one line.
            fid.write(line)
    print("Data saved successfully.")
# I believe we have to write to the file, cause apending would keep adding students, and eventually become out of sync with the program if students keep getting removed/edited

def load():
    students.clear()
    # We use this to clear the current memory (As in the program that just opened) and clears its cache, before loading all the info from the file. helps to prevent duplicates if we are constanly starting/stopping the program
    # This doesnt actually delete/remove anything from the file though. just a way to prevent possible error/duplications. 
    if os.path.exists("Saved_students.txt"):
        with open("Saved_students.txt", "r") as fid: # We want to read the file and take that data, so we use "r"
            # Using 'with' makes it so we dont have to open and close the file, it does it automatically.
            for line in fid: # Since we are saving each student to one line. each line represents one student. This should loop through each line and take the data that is required.
                id, fn, ln, gpa, sem = line.strip().split("|") # This takes the data and splits it with the |. so its easy to ready the file and keep the information seperate.
                students[int(id)] = Student(id, fn, ln, gpa, sem)
                # The file should automatically add these to the private attributes.
        print("Student data loaded successfully.")