from Car import *

'''
Created By Patrick Bouley, Joshua Dyke, Ahmed Yassine Messaoudi. Group 4
December, 15, 2025

This program was made to register, and save a cars information to a database. Using a class system to gather information.  
The user can come back to the same database whenever they need to add, edit or remove cars.
They can view all the information saved on the file as well. 
A file will automatically be created if one doesnt exist. 

'''

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
        operate = False
    else:
        print("Invalid input, please try again.")
        continue

print("Exiting, thanks for using the program.")