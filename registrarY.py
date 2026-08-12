def create_database():
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
            dob=input("Enter the date of birth (YYYY-MM-DD): ")
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
option=str(input(""""What do you want to do? 
(1) Create Database
    to create type 'create'
(2) Search Database
    to search type 'search'
"""))
if option.lower()=="create":
    create_database()
elif option.lower()=="search":
    search_database()
else:
    print("input valid option create/search")