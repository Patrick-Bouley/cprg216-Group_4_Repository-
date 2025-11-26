from Registry_Functions import *
# This imports all the functions and lets us use them as is, without the file name in front of the function name
# import modified_test makes it so we have to write modified_list.function_name to use anything from that file. so the above way is more convienient 
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
