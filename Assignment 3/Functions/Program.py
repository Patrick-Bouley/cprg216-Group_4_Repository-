from Student import *

print("Welcome to the students record program!")
load(students, 'Saved_data.txt')
test = True 
while test == True:
    choice = main_menu()
    if choice == "1":
        run_add()
    elif choice == '2':
        run_search()
    elif choice == '3':
        run_edit()
    elif choice == '4':
        run_remove()
    elif choice == '5':
        display_dict()
    elif choice == '6':
        pass # Need a function to call for a file to save to data.txt
    else:
        print("Invalid input, please try again.")
    operate = input("Would you like to continue(y/yes), or exit the program(n/no)?\n").lower()
    if operate == "yes" or operate == "y":
        test = True
    else:
        test = False

print("Exiting, thanks for using the program.")
