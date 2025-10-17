#Grade Registry Program.
#This program stores students name and their accumulative GPA using a dictionary.
print("Welcome to the Grade Registry Program")
students = {} #Dictionary to store student names and GPA's.
add_student_raw = input("Would you like to add a new student ? y(yes),n(no)\n")
add_student = (add_student_raw.lower()) # this function changes all the user inputs into lowercase for error reduction
#Main loop to add students until the user decides to stop.
while add_student != "no" or add_student != "n": #Check if user wants to add a student.
    if add_student == "yes" or add_student == "y":
        name = input("Enter the student's name:\n")
        gpas = [] #List to store the student's GPA's.
        gpa = float(input("Enter the student's GPA for each subject. Enter -1 to stop entering GPA.\n"))
        #GPA input loop.
        while gpa != -1:
            gpas.append(gpa)
            gpa = float(input())
        #Compute average GPA or set to 0 if no GPA entered.
        if len(gpas)>0:
            average = sum(gpas)/len(gpas)
        else:
            average = 0
        students[name] = average #Store the student's name and GPA.
        add_student_raw = input("Would you like to add a new student ? y(yes),n(no)\n")
        add_student = (add_student_raw.lower()) 
    #If user wants to stop.
    elif add_student == "no" or add_student == "n":
        break
    #If user enters something invalid.
    else:
        print("Incorrect input, please enter y(yes) or n(no).")
        add_student = input("Would you like to add a new student ? y(yes),n(no)\n")
#Print the list of students and their average GPAs.
print("This is the list of students in the system, and their corresponding accumulative GPA.")
for name in students:
    print(name, round(students[name], 2))
    print("Thanks for using this program !")

