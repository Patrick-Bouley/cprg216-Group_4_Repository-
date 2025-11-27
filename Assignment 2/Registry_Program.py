from Registry_Functions import *
# This imports all the functions and lets us use them as is, without the file name in front of the function name
# import modified_test makes it so we have to write modified_list.function_name to use anything from that file. so the above way is more convienient 

'''
A rundown on how the program works

As the program starts, you are presented with a menu and a couple of options. You have to input what you would like to do from those options. Search, Edit, Add, Remove. (1, 2, 3, 4) any other input will be invalid.
As we are just starting the program, no data will be present, so you should start by adding a student. in the Terminal, type the Number '3'
In this sub-menu it will ask for a students ID, their name, their GPA, and the semseter they are in, in that order. You will provide this information with your own inputs, in the Terminal one at a time. Each option is clearly labeled
When a student has succesfully been added, it will display their information in the Terminal, (ID, Name, GPA, Semester) then ask if you would like to add another student. giving you the choice to say yes or no. 
Based on this choice, it will either repeat the student adding process. or ask if you would like to continue or exit the program, giving you another yes or no option.
Typing yes will return you to the main menu, where you will be presented with the previous options of 1, 2, 3, 4 (Search, Edit, Add, Remove)
From here, since there is data in the program now. We can select any of the other options to use. in the terminal Lets type the number '2'. Which is Edit
In the edit section, you will only be allowed to edit a students name that is in the program. 
It will first ask you to input the ID of the student you wish to edit. which you can then do so in the Terminal. Once the ID has been inputed, it will ask you to provide the new/edited name of the student, which you can provide in the terminal as well
After getting that info, it will the provide you with a confirmation that a student with the ID you inputed, now has the new name you provided.
After that, you will again be presented the option to do the same process again. If you dont, it will ask if you wish to continue, or end the program again. Each of the choices in the main menu will repeat this process.
Once back at the main menu, you are provided with the same options 1, 2, 3, 4. Lets type the number '1' which is Search
The search sub menu will open. and this one is pretty simple. You will be asked to search for the students information you want by using their ID. Input that in the Terminal. You will be provided that information in the same way you added a student. Their ID, Name, GPA, and Semseter.
It will then repeat its statement of "Enter the id of the student you wish to find, or press -1 to exit" pressing -1 will prompt you with another "continue? yes or no" input 
Once back at the main menu, we see our options. 1, 2, 3, 4. The last option being '4', we will select that one.
The last function is to remove the entirety of a students information from the program. 
The sub menu will open and ask you for the students ID you wish to delete. which you can do so in the Terminal. once that ID has been submitted, it will delete that student and all their information.
The consol will state "Student Deleted" meaning it was successful, and repeat its process and ask if you want to delete another student. pressing -1 will stop this process. giving you one last "do you want to continue" option.
If you select no, the menu will close and exit the program

Its important to note that this program does not save any of the information that gets inputed. It is all lost once you exit
Statements that ask you for IDs will also have failsafes for inputing information that is not correct or already in use
If trying to add a student with an ID already in the system, the terminal will state that the ID is already in use and will return you to a point where you can try inputting the ID again 
If using the search, edit or remove functions, It will let you know if that ID doesnt exist in the system and return to where you can try inputing the ID again

'''

print("Welcome to the students record program!")
test = True 
while test == True:
    choice = main_menu()
    if choice == "1":
        run_search()
    elif choice == '2':
        run_edit()
    elif choice == '3':
        run_add()
    elif choice == '4':
        run_remove()
    else:
        print("Invalid input, please try again.")
    operate = input("Would you like to continue(y/yes), or exit the program(n/no)?\n").lower()
    if operate == "yes" or operate == "y":
        test = True
    else:
        test = False

print("Exiting, thanks for using the program.")
