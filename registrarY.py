from ast import literal_eval
def create_default_database():
    while True:
        try:
            num_entry=int(input("Enter the number of entries you want to add: "))
            if num_entry > 0:
                break
            print("Enter a positive number.")
        except Exception as e:
            print("Enter a positive number")       
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    database = {}
    if num_entry <= 0:
        print("Please enter a positive number of entries.")
    else:
        for i in range(num_entry):
            if num_entry <= 0:
                print("Please enter a positive number of entries.")
                break
            name = input("Enter the name: ")
            dob=input("Enter the date of birth (DD-MM-YYYY): ")
            fname=input("Enter the father's name: ")
            mname=input("Enter the mother's name: ")
            detail_set= {"Name":name,"date_of_birth": dob,"father_name": fname,"mother_name": mname}

            letter_index = i // 1000
            number = (i % 1000) + 1
            roll_no = alphabet[letter_index] + f"{number:04d}"
            data={}
            data[roll_no]=detail_set

            print(roll_no)
            database.update(data)

    print(database)
    python_file_content =str(database)
    with open(f"{database_name}.py", "w") as file:
        file.write(python_file_content)


def load_database():
    with open(f"{database_name}.py", "r") as file:
        content = file.read()
    return literal_eval(content.strip())

def view_all():
    database = load_database()
    print("=" * 100)
    for roll_no, details in database.items():
            print(f"      Roll Number: {roll_no}")
            print("-" * 100)
            print(f"      Name         : {details['Name']}")
            print(f"      Date of Birth: {details['date_of_birth']}")
            print(f"      Father's Name: {details['father_name']}")
            print(f"      Mother's Name: {details['mother_name']}")
            print("_" * 100)
def search_database():
    database=load_database()

    roll_no = input("Enter roll number to search: ")

    if roll_no in database:
        print("=" * 100)
        print(f"      Roll Number: {roll_no}")
        print("-" * 100)
        print(f"      Name        : {database[roll_no]['Name']}")
        print(f"      DOB         : {database[roll_no]['date_of_birth']}")
        print(f"      Father Name : {database[roll_no]['father_name']}")
        print(f"      Mother Name : {database[roll_no]['mother_name']}")
        print("_" * 100)
    else:
        print("roll number",roll_no,"not found in tha database")
def update_database():
    database=load_database()
    
    roll_no = input("Enter roll number to search: ")
        
    if roll_no in database:
        print("-" * 40)
        print(f"      Roll Number: {roll_no}")
        print("-" * 40)
        print(f"      Name        : {database[roll_no]['Name']}")
        print(f"      DOB         : {database[roll_no]['date_of_birth']}")
        print(f"      Father Name : {database[roll_no]['father_name']}")
        print(f"      Mother Name : {database[roll_no]['mother_name']}")
        print("-" * 40)
        print("Enter the new details to update the database or press ENTER KEY to keep the original values")
        name = input("Enter the name: ")
        dob=input("Enter the date of birth (DD-MM-YYYY): ")
        fname=input("Enter the father's name: ")
        mname=input("Enter the mother's name: ")

        if name!="":
            database[roll_no]["Name"]=name
        if dob!="":
            database[roll_no]["date_of_birth"]=dob
        if fname!="":   
            database[roll_no]["father_name"]=fname
        if mname!="":
            database[roll_no]["mother_name"]=mname
        
        python_file_content =str(database)
        with open(f"{database_name}.py", "w") as file:
            file.write(python_file_content)
        print("Database Updated")
        print("-" * 40)
        print(f"      Roll Number: {roll_no}")
        print("-" * 40)
        print(f"      Name        : {database[roll_no]['Name']}")
        print(f"      DOB         : {database[roll_no]['date_of_birth']}")
        print(f"      Father Name : {database[roll_no]['father_name']}")
        print(f"      Mother Name : {database[roll_no]['mother_name']}")
        print("-" * 40)
    else:
        print("roll number",roll_no,"not found in tha database")

while True:
    database_name=str(input("Enter the name of the database to do the operations:"))
    try:
        with open(f"{database_name}.py", "r") as file:
            file.read()
        if database_name !="":
            break
    except Exception as e:
        question1=str(input("do you want to create new database?y/n"))
        if question1.lower()=="y" or question1.lower()=="yes":
            print(e,f"You will have create a new database {database_name} as the file doesnt exist \nand later continue to do operations on it") 
            break
while True:
    print(
        """"What do you want to do? 
    (1) Create default 
    (2) View all 
    (3) Search 
    (4) Update 
    (5) Help
    (6) Exit
"""
    )
    option=str(input("Enter your option>>>"))
    if option.lower()=="create_default" or option=="1":
        create_default_database()
    elif option.lower()=="view_all" or option=="2":
        view_all()
    elif option.lower()=="search" or option=="3":
        search_database()
    elif option.lower()=="update" or option=="4":
        update_database()
    elif option.lower()=="help" or option=="5":
        print("""OPTION  | ACTION          | DESCRIPTION
--------+-----------------+----------------------------------------------------
  1     | Create Default  | Add entries and auto-generate roll numbers.
  2     | View All        | Display all records currently in the database.
  3     | Search          | Look up a record by Roll Number.
  4     | Update          | Modify an existing record (Press ENTER to skip).
  5     | Help            | Display this menu.
  6     | Exit            | Quit the application.""")
    elif option.lower()=="exit" or option=="6":
        print("""Kicking you out of the program......
DONE.""")
        break
    else:
        print("input valid option create/search")
    print("#" * 100)
