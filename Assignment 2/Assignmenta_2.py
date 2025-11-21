from modified_test import *
# This imports all the functions and lets us use them as is, without the file name in front of the function name
# import modified_test makes it so we have to write modified_list.function_name to use anything from that file. so the above way is more convienient 

operate = True 
while operate == True:
    main_menu()
    operate = input("Do you want to keep using the program? y(yes)/n(no):\n")
    if operate == "yes" or operate == "y":
        operate = True
    else:
        break

print("Exiting, thanks for using the program.")