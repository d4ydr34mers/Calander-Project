import json
# importing the users previous data from a json file
with open('userdata.json', 'r') as importdata:
    dates = json.load(importdata)


# function to save new assignment
def savenew(date, assignment):
    if date in dates:
        dates[date].append(assignment)
    elif date not in dates:
        dates[date] = ['PH', assignment]

    with open('userdata.json', 'w') as exportdata:
        json.dump(dates, exportdata)


# function to delete assignment
def delete(date, assignment):
    dates[date].remove(assignment)

    with open('userdata.json', 'w') as exportdata:
        
        json.dump(dates, exportdata)


# function to update assignment
def update(date, oldassignment, newassignment):
    index = dates[date].index(oldassignment)
    dates[date][index] = newassignment

    with open('userdata.json', 'w') as exportdata:
        json.dump(dates, exportdata)


# function to view all assignments
def viewall():
    print(dates)


# calling savenew function with user information
def runsavenew():
    date = input("What is the due date of your assignment? ")
    name = input("Name your assignment: ").lower().strip()
    savenew(date, name)

# calling delete function with user information
def rundelete():
    date = input("What is the date of the assignment")
    name = input("which assignment do you want to delete").lower().strip()
    delete(date, name)

#calling update function with user information
def runupdate():
    date = input("What is the date of the assignment you would like to change ?")
    name1 = input("What was the old name of your assignment").lower().strip()
    name2 = input("What would you like to rename your assignment too?").lower().strip()
    update(date, name1, name2)


# Start screen

print("""Hi there, the list of commands to use the calendar are:
    
    New - saves new deadline
    Delete - deletes a deadline
    Update - updates a date or deadline
    View - Shows a list of all deadlines
    
    When entering dates please use dd/mm/yy, with a 0 in front of all single digits """)

# loop for command entry
repeat = True
while repeat:
    user_input = input("Type here : ").lower().strip()

    if user_input == "new":
        runsavenew()
    elif user_input == "delete":
        rundelete()
    elif user_input == "view":
        viewall()
    elif user_input == "update":
        runupdate()
    elif user_input == "close":
        repeat = False
    else:
        pass
