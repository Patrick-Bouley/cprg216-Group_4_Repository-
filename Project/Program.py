from Car import *

print("Welcome to the cars inventory system.")
load() # this is defined in the import page, meaning the user needs to have a file called "Saved_data.txt" ready to use before running this program.
operate = True 
while operate:
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
        display_all()
    elif choice == '6':
        save_info()
    elif choice == '0':
        break
    else:
        print("Invalid input, please try again.")
        continue
    while True:
        # Added this loop to prevent inputs other than Yes or No, and repeats the question until a proper input is added 
        operate = input("Would you like to go back to the main menu?(y/yes), or exit the program(n/no)?\n").lower()
        if operate == "yes" or operate == "y":
            operate = True
            break
        elif operate == "no" or operate == "n":
            operate = False
            break
        else:
            print("Invalid input. Please Try again")

print("Exiting, thanks for using the program.")