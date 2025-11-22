from Assignment2 import *
# This imports all the functions and lets us use them as is, without the file name in front of the function name
# import modified_test makes it so we have to write modified_list.function_name to use anything from that file. so the above way is more convienient 

test = True 
while test == True:
    main_menu()
    operate = input("Would you like to continue(y/yes), or exit the program(n/no)?\n").lower()
    if operate == "yes" or operate == "y":
        test = True
    else:
        test = False

print("Exiting, thanks for using the program.")
