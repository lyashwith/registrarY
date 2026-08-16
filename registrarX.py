def create_default_database():
    num_entry=int(input("Enter the number of entries you want to add: "))
        
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
            count = 0
            for letter in alphabet:
                for number in range(1, 1001):
                    roll_number = letter+f"{number:04d}"
                    count+=1
                    if count ==(i+1):
                        break
                if count ==(i+1):
                    break
            data={}
            data[roll_number]=detail_set

            print(roll_number)
            database.update(data)

    print(database)
    python_file_content = f"database = {database}"
    with open("database.py", "w") as file:
        file.write(python_file_content)

def search_database():
    from database import database

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
    else:
        print("roll number",roll_no,"not found in tha database")
def update_database():
    from database import database
    
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
        
        python_file_content = f"database = {database}"
        with open("database.py", "w") as file:
            file.write(python_file_content)
        print("database updated")
    else:
        print("roll number",roll_no,"not found in tha database")

              
while True:
    option=str(input(""""What do you want to do? 
    (1) Create default Database
    (2) Search Database
    (3) Update Database
    (4) Help
    (5) Exit
"""))
    if option.lower()=="create_default" or option=="1":
        create_default_database()
    elif option.lower()=="search" or option=="2":
        search_database()
    elif option.lower()=="update" or option=="3":
        update_database()
    elif option.lower()=="help" or option=="4":
        print("""(1) Create default Database: This option allows you to create a default database by entering the number of entries you want to add. You will be prompted to enter the name, date of birth, father's name, and mother's name for each entry. The roll number will be generated automatically based on the number of entries.)
(2) Search Database: This option allows you to search for a specific entry in the database by entering the roll number. If the roll number is found, the details of the entry will be displayed.
(3) Update Database: This option allows you to update the details of a specific entry in the database by entering the roll number. You will be prompted to enter the new details for the entry, and you can choose to keep the original values by pressing the ENTER key.
(4) Help: This option provides information about the available options in the program.
(5) Exit: This option allows you to exit the program.""")
    elif option.lower()=="exit" or option=="5":
        print("""Kicking you out of the program......
DONE.""")
        break
    else:
        print("input valid option create/search")
    print("-" * 40)
