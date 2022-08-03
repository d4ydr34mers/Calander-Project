import json
# importing the users previous data from a json file and storing it under the variable dates
with open('data.json', 'r') as importdata:
    dates = json.load(importdata)


# function to save new assignment
def savenew(date, assignment):
    if date in dates:
        dates[date].append(assignment)
    elif date not in dates:
        dates[date] = ['PH', assignment]

    with open('data.json', 'w') as exportdata:
        json.dump(dates, exportdata, indent=4, sort_keys=True)

    print(f"~{assignment.capitalize()} added to calendar~")


# function to delete assignment
def delete(date, assignment):
    dates[date].remove(assignment)
    with open('data.json', 'w') as exportdata:
        json.dump(dates, exportdata, indent=4, sort_keys=True)
    print(f"~{assignment} removed from {date}~")


# function to update assignment
def update(date, oldassignment, newassignment):
    index = dates[date].index(oldassignment)
    dates[date][index] = newassignment

    with open('data.json', 'w') as exportdata:
        json.dump(dates, exportdata, indent=4, sort_keys=True)
    print(f"~{oldassignment} from {date} changed to {newassignment}~")


# function to view all assignments
def viewall():
    for key, value in dates.items():
        print(key, ":", ", ".join(value).replace("PH,","").capitalize())

# function that when called, prints the bellow information on the commands and tips on how to use the program
def help():
    print("""
                    ~~~LIST OF COMMANDS~~~
                    (Command input only)
        New - add a new assignment due date to the calender
        Delete - delete an assignment from the calender
        Update - change the name of an assignment
        Viewall - view the full list of assignment due dates 
        Close - Closes the program
                (Can be inputted anywhere in the program)
        Help - shows all commands and important tips, can be inputted at any point
        Cancel - can be inputted at any point to return to the initial command input
        
        - Reminders
            - The program is not case sensitive 
            - Use dd/mm/yy when entering dates, with a 0 in front of all single digits
            - ! is an error message
            - ~ is a successfully completed process
            """)


# calling savenew function with user information
def runsavenew():
    # loop to ask again for user's input if their previous input was invalid
    while True:
        date = input("What is the due date of your assignment ? ").strip()
        if date == "cancel":
            print("~Back to command input~")
            break
        elif date == "help":
            help()
            pass
        else:
            # loop to ask again for user's input if their previous input was invalid
            givendate = date
            while True:
                name = input("Name your assignment : ").lower().strip()

                if name == "cancel":
                    print("~Back to command input~")
                    return

                elif name == "help":
                    help()

                else:
                    savenew(givendate, name)
                    return


# calling delete function with user information
def rundelete():
    # loop to ask again for user's input if their previous input was invalid
    while True:
        date = input("What is the due date of the assignment ? ").strip()
        if date == "cancel":
            print("~Back to command input~")
            break
        elif date == "help":
            help()
            pass
        elif date not in dates:
            print("!Date not found (input 'cancel' to go back)!")
            pass
        else:
            # after the user enters valid information, this loop repeats until a valid input is given or the
            # user inputs "cancel"
            givendate = date
            while True:
                name = input("Which assignment do you want to delete ? ").lower().strip()
                if name == "cancel":
                    print("~Back to command input~")
                    return False
                elif name == "help":
                    help()
                    pass
                elif name not in dates[givendate]:
                    print("!Item not found (input 'cancel' to go back)!")

                elif name in dates[givendate]:
                    delete(givendate, name)
                    return False


# calling update function with user information
def runupdate():
    # loop to ask again for user's input if their previous input was invalid
    while True:
        date = input("What is the due date of the assignment you would like to change ? ").strip()
        if date == "cancel":
            print("~Back to command input~")
            break
        elif date == "help":
            help()
            pass
        if date not in dates:
            print("!Date not found (input 'cancel' to go back)!")
            pass
        else:
            # loop to ask again for user's input if their previous input was invalid
            givendate = date
            while True:
                name1 = input("What is the current name of your assignment ? ").lower().strip()
                if name1 == "cancel":
                    print("~Back to command input~")
                    return False
                elif name1 == "help":
                    help()
                    pass
                elif name1 not in dates[givendate]:
                    print("!Date not found(input 'cancel' to go back)!")
                    pass
                else:
                    name2 = input("What would you like to rename your assignment too ? ").lower().strip()
                    if name2 == "cancel":
                        print("~Back to command~")
                        return False
                    elif name2 == "help":
                        help()
                        pass
                    else:
                        update(givendate, name1, name2)
                        return False


# Start screen

print("""
Hi there, welcome to my calender :)

Here are the list of commands:
                    (Command input only)
        New - add a new assignment due date to the calender
        Delete - delete an assignment from the calender
        Update - change the name of an assignment
        Viewall - view the full list of assignment due dates 
        Close - Closes the program
        
            (Can be inputted anywhere in the program)
        Help - shows all commands and important tips
        Cancel - returns you to the initial command input
        
        - Reminders
            - The program is not case sensitive 
            - Use dd/mm/yy when entering dates, with a 0 in front of all single digits
            - ! is an error message
            - ~ is a successfully completed process""")

# loop for command entry
while True:

    user_input = input("""
    Input your command : """).lower().strip()

    if user_input == "new":
        runsavenew()
    elif user_input == "delete":
        rundelete()
    elif user_input == "viewall":
        viewall()
    elif user_input == "update":
        runupdate()
    elif user_input == "close":
        print("All assignments have been saved, thank you for using the calendar :)")
        break
    elif user_input == "help":
        help()
    else:
        print("!Command not recognised (input 'help' to see commands)!")
        pass
