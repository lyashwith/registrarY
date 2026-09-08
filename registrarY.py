from ast import literal_eval
import re
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

def load_custom_schema():
    with open(f"custom_schema{database_name}.py", "r") as file:
        content = file.read()
    return content

def custom_schema():
    primary_key=input("Enter unique primary key field:")
    fields=input("enter fields with data type(example name;str,age;int,gender;str):")
    schema={}
    schema[primary_key] = {}
    for i in fields.split(","):
        field_name, data_type = i.split(";",1)
        schema[primary_key][field_name] = data_type
    print("Custom schema created:",schema)
    with open(f"custom_schema{database_name}.py", "w") as file:
        file.write(str(schema))

def add_custom_data():
    content=load_custom_schema()
    schema = literal_eval(content)
    for key,value in schema.items():
        primary_key_name=key
    schema_lengths =len(schema[primary_key_name])
    num_entry=int(input("Enter the number of entries you want to add: "))
    database = {}
    if num_entry <= 0:
        print("Please enter a positive number of entries.")
    else:
        for i in range(num_entry):
            primary_key = input(f"Enter {primary_key_name} for entry number{i + 1}: ")
            database[primary_key] = {}
            for j in range(schema_lengths):
                field_name = list(schema[primary_key_name].keys())[j]
                data_type = schema[primary_key_name][field_name]
                if data_type == "str":
                    value = input(f"Enter {field_name} (string): ")
                elif data_type == "int":
                    value = int(input(f"Enter {field_name} (integer): "))
                elif data_type == "float":
                    value = float(input(f"Enter {field_name} (float): "))
                else:
                    print(f"Unsupported data type: {data_type}")
                    continue
                database[primary_key][field_name] = value
    print(database)       

    python_file_content = str(database)
    with open(f"{database_name}.py", "w") as file:
        file.write(python_file_content)

def view_all():
    database = load_database()
    print("=" * 100)
    for primary_key, details in database.items():
            print(f"      Roll Number: {primary_key}")
            print("-" * 100)
            for field_name, value in details.items():
                print(f"      {field_name}: {value}")
            print("_" * 100)
def search_database():
    database=load_database()

    primary_key = input("Enter roll number to search: ")

    if primary_key in database:
        print("=" * 100)
        print(f"      Primary key: {primary_key}")
        print("-" * 100)
        for field_name, value in database[primary_key].items():
            print(f"      {field_name}: {value}")
        print("_" * 100)
    else:
        print("roll number",primary_key,"not found in the database")
def update_database():
    database=load_database()
    
    primary_key = input("Enter roll number to search: ")
        
    if primary_key in database:
        print("=" * 100)
        print(f"      Primary key: {primary_key}")
        print("-" * 100)
        for field_name, value in database[primary_key].items():
            print(f"      {field_name}: {value}")
        print("_" * 100)
        print("-" * 40)
        print("Enter the new details to update the database or press ENTER KEY to keep the original values")
        for field_name, value in database[primary_key].items():
            new_value = input(f"      {field_name} (current value: {value}): ")
            if new_value != "":
                database[primary_key][field_name] = new_value
        
        python_file_content =str(database)
        with open(f"{database_name}.py", "w") as file:
            file.write(python_file_content)
        print("Database Updated")
        print("=" * 100)
        print(f"      Primary key: {primary_key}")
        print("-" * 100)
        for field_name, value in database[primary_key].items():
            print(f"      {field_name}: {value}")
    else:
        print("roll number",primary_key,"not found in the database")

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
    (2) Create custom Schema
    (3) Add data 
    (4) View all 
    (5) Search 
    (6) Update 
    (7) Help
    (8) Exit
"""
    )
    option=str(input("Enter your option >>>"))
    if option.lower()=="create default" or option=="1":
        create_default_database()
    elif option.lower()=="create custom schema" or option=="2":
        custom_schema()
    elif option.lower()=="add data" or option=="3":
        add_custom_data()
    elif option.lower()=="view all" or option=="4":
        view_all()
    elif option.lower()=="search" or option=="5":
        search_database()
    elif option.lower()=="update" or option=="6":
        update_database()
    elif option.lower()=="help" or option=="7":
        print("""OPTION  | ACTION          | DESCRIPTION
+-------+-----------------+---------------------------------------------------+
| 1     | Create Default  | Add entries and auto-generate roll numbers.       |
| 2     | Create Custom   | Define a custom schema for the database.          |
| 3     | Add Data        | Insert new records into the database.             |
| 4     | View All        | Display all records currently in the database.    |
| 5     | Search          | Look up a record by Roll Number.                  |
| 6     | Update          | Modify an existing record (Press ENTER to skip).  |
| 7     | Help            | Display this menu.                                |
| 8     | Exit            | Quit the application.                             |
+-------+-----------------+---------------------------------------------------+""")                           
    elif option.lower()=="exit" or option=="8":
        print("""Kicking you out of the program......
DONE.""")
        break
    else:
        print("input valid option create/search")
    print("#" * 100)
