import os
cars = {}

class Car:
    def __init__(self, id, name, make, body, year, value):
        # Make all these private
        self.__id = id
        self.__name = name
        self.__make = make
        self.__body = body
        self.__year = year
        self.__value = value
 
    def set_id(self, value):
        self.__id = value

    def set_name(self, value):
        self.__name = value
 
    def set_make(self, value):
        self.__make = value
 
    def set_body(self, value):
        self.__body = value
 
    def set_year(self, value):
        self.__year = value
   
    def set_value(self, value):
        self.__value = value

def main_menu():
    # A function that displays the main menu and provides a choice for the user to main. It returns that choice so the overal program knows where to send the user
    print("What would you like to do today?\n-Add a car? \t\t\t\tenter 1\n-Search for a car? \t\t\tenter 2 \n-Edit the cars info? \t\t\tenter 3 \n-Remove a car? \t\t\t\tenter 4\n-Print the car list?\t\t\tenter 5\n-Save the cars to a file? \t\tenter 6\n-Exit? \t\t\t\t\tenter 0")
    choice = input(": ")
    return choice #sends the input back to the program file for the menu there
       
def run_add():
    # A function that runs the add car function, until the user decides they are done
    while True:
        add_car()
        add = input("Do you want to add more cars? y(yes)/n(no)\n").lower().strip()
        if add in ('y', 'yes'):
            continue
        else:
            break  
   
def run_search():
    # A function that runs the search function, until the user decides they are done
    while True: # A while statement is used so that we can take input as many times as the user would like to use the function
        id_str = input("To search using the ID enter 1. To search using the name of the car enter 2. Enter -1 to return to the previous menu. \n")
        if id_str == '1': #checking if the user wants to search using the ID.
            search_id = int(input("Please enter the ID of the car:\n"))
            ID_search(search_id)
        elif id_str == '2': #checking if the user wants to search using the name of the car.
            Name_search()
        elif id_str == '-1': #checking if the user wants to return to the previous menu.
            break
        elif not id_str.isdigit(): #checks if user input is a number or not, if not then loop continues
            print("Invalid input. Please enter a valid car ID.")
            
def run_edit():
    # a function to run the edit car function until the user decides they are done
    while True:
        edit = int(input("Enter the ID of the car. Enter -1 to return to the main menu.\n"))
        if edit == int(-1):
            break
        else:
            edit_car(edit)
  
def run_remove():
    # a function to run the remove car function to remove as many cars as desired | Also nearly identical to the function above
    while True:
        remove()
        rem = input("Do you want to remove another car? y(yes)/n(no)\n")
        if rem in ('y', 'yes'):
            continue
        else:
            break

def load():
    cars.clear()
    #We use this to clear the current memory (As in the program that just opened) and clears its cache, before loading all the info from the file. helps to prevent duplicates if we are constanly starting/stopping the program
    #This doesnt actually delete/remove anything from the file though. just a way to prevent possible error/duplications. 
    if os.path.exists("Saved_cars.txt"):
        with open("Saved_cars.txt", "r") as fid: # We want to read the file and take that data, so we use "r"
        # Using with makes it so we dont have to open and close the file, it does it automatically.
            for line in fid: # Since we are saving each car to one line. each line represents one car. This should loop through each line and take the data that is required.
                id, name, make, body, year, value = line.strip().split("|") # This takes the data and splits it with the |. so its easy to ready the file and keep the information seperate. Which is why we need to strip that info when we try to interpret that information in the functuons above.
                cars[int(id)] = Car(id, name, make, body, year, value)
            # The file should automatically add these to the private attributes.
            # made id an int because thats how we have been making it a key for our dictionary
        print("Car data loaded successfully.")

def save_info():
    with open("Saved_cars.txt", "w") as fid:
        # Choosing to write and not append. So that everytime we save the info, it updates the whole file, instead of just adding it to the bottom.
        for id in cars:
            line = (f"{id}|"f"{cars[id]._Car__name}|"f"{cars[id]._Car__make}|"f"{cars[id]._Car__body}|"f"{cars[id]._Car__year}|"f"{cars[id]._Car__value}\n")
            # This writes the line in a way that allows the Load function to read them properly. Because that info is all on one line.
            fid.write(line)
    print("Data saved successfully.")
   
def add_car():
    # Adds cars to a directory, based off the class system above
    id = int(input("Enter id of the car, followed by the car's information.\nID:\n"))
    if id in cars: #prevents user from using the same ID to create multiple cars.
        print("Incorrect ID. ID already exists in the system")
        return
    car = Car(id, input("Name:\n"), input("Make:\n"), input("Body:\n"), int(input("Year:\n")), float(input("Value:\n")))
    for c in cars.values():
        if (c._Car__name.lower() == car._Car__name.lower() and c._Car__make.lower() == car._Car__make.lower() and c._Car__body.lower() == car._Car__body.lower() and c._Car__year == car._Car__year and c._Car__value == car._Car__value):
            # We use .lower to avoid things like "Mazda" and "mazda" to be considered two different names.
            print("Error: That car is already in the inventory, no action is required.")
            return
            # This checks to see if the name is in use at the same time.
    cars[id] = car
    print("Car added to inventory.") #user confirmation in two parts, telling the user that its added and showing the user the new addition
    display_specific(id) #Shows the car that was just added 
    save_info() # Automatically saves that info to the file 

def ID_search(id):
    # Searches for a car based off of its ID
    if id in cars:
        print("Car found")
        display_specific(id) # displaying the car info consistently by using a display function
    else:
        print("Car not in inventory") #error message

def Name_search():
    #Searches for a car based off its name. 
    name = input("Enter the car name:\n").lower()
    # We use lower to make sure its an easy comparision for the file
    for id, car in cars.items():
        if (car._Car__name.lower() == name):
            print("Car found")
            display_specific(id)
            return
    else:
        print("Car not found")
 
def remove():
    # Will remove all information on a car based off of the ID that is inputted
    id = int(input("Enter the ID of the car you want to remove from the cars inventory:\n")) #gets id from user, will break program if it isn't an integer input though
    if id in cars: #checks if the id is in the cars inventory
        del cars[id] #removes the car from the inventory
        print("Car Removed") #confirmation of removal
        save_info() # This will make sure the file gets changed to match what has been removed. Making sure There would be any discrepancies/differences 
    else:
        print("Car not in inventory") #error message if there isnt a car with matching info
 
def edit_car(id):
    # The statement below checks to make sure the ID is in the system first
    if id not in cars:
        print("That ID does not exist in the system.")
        return
    # Ask for updated information, in relation to the objects in Car
    new_name = input("Enter the new name:\n")
    new_make = input("Enter the new make:\n")
    new_body = input("Enter the new body:\n")
    new_year = int(input("Enter the new year:\n"))
    new_value = float(input("Enter the new value:\n"))
    # We then use 'set' to update what those objects should be for that specific car based on the ID
    cars[id].set_name(new_name)
    cars[id].set_make(new_make)
    cars[id].set_body(new_body)
    cars[id].set_year(new_year)
    cars[id].set_value(new_value)
    print("Car information updated successfully.")
    display_specific(id)
    save_info()
    # Saves the info to the file automatically. just to update the information. Keeps the file consistent for what is stored in there and the program that is currently running

def display_all():
    #for displaying all the cars in the save file
    if not cars:
        print("No cars are currently saved in the inventory.")
        return
        # This just checks to see if there even is anything saved to the file first, before trying to display something
    print("The current record of cars in the inventory are as follows:")
 # Loop through every car ID stored in the dictionary
    for id, car in cars.items():
        name = car._Car__name
        make = car._Car__make
        body = car._Car__body
        year = car._Car__year
        value = car._Car__value
        # This should loop through all the cars on the file
        print(f"ID: {id}, Name: {name} , Make: {make}, Body: {body}, Year: {year}, Value: {value}", sep = ",")

def display_specific(id):
    # Make sure the ID exists before displaying
    if id not in cars:
        print("Car not found.")
        return
    name = cars[id]._Car__name
    make = cars[id]._Car__make
    body = cars[id]._Car__body
    year = cars[id]._Car__year
    value = cars[id]._Car__value
    # Display the car info clearly
    print(f"Car ID: {id}", f"Name: {name}", f"Make: {make}", f"Body: {body}", f"Year: {year}", f"Value: {value}", sep = ", ")
