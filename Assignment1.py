print("Welcome to the Grade Registry Program..")
continue_option = 'y'
while continue_option == 'y':
    student_name = input("Please enter the name of the student you would like to enter: ")
    print("Please enter numbers, one at a time. Input -1 to end user inputs")
    sum = 0
    num = 0
    count = 0
    while num>-1:
        sum += num
        num = float(input())
        if num == -1:
            break
        count += 1

    gpa =[student_name, sum/count]
    # print(student_name, sum/count)
    continue_option = input("would you like to enter another student? (Y)es/(N)o " )
print(gpa)
print("Thanks for using the program")

'''
Im not sure if this is even the right direction, It was me messing around
'''