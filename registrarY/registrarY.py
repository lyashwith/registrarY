from json import dump,load
from os import name as os_name
from subprocess import run as sub_run
from tabulate import tabulate
__lazy_modules__ = ["openpyxl"]
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
    python_file_content =database
    with open(f"{database_name}.eL", "w") as file:
        dump(python_file_content,file)

def dump_database(database):
    python_file_content =database
    with open(f"{database_name}.eL", "w") as file:
        dump(python_file_content,file)

def load_database():
    with open(f"{database_name}.eL", "r") as file:
        content = load(file)
    return content

def load_custom_schema():
    with open(f"custom_schema-{database_name}.eLs", "r") as file:
        content = load(file)
    return content

def table_loader(database):
    headers=[]
    schema=load_custom_schema()
    for i,j in schema.items():
        headers.append(i)
        headers.extend(j.keys())
    rows=[]
    for a,b in database.items():
        rown=[a]
        for k,v in b.items():
            rown.append(v)
        rows.append(rown)
    return headers,rows

def clear_screen():
    if os_name=="nt":
        sub_run(['cls'],shell=True)
    else:
        sub_run(['clear'])

def custom_schema():
    primary_key=input("Enter unique primary key field:")
    fields=input("enter fields with data type(example name;str,age;int,gender;str):")
    schema={}
    schema[primary_key] = {}
    for i in fields.split(","):
        field_name, data_type = i.split(";",1)
        schema[primary_key][field_name] = data_type
    print("Custom schema created:",schema)
    with open(f"custom_schema-{database_name}.eLs", "w") as file:
        dump(schema,file)

def add_custom_data():
    try:
        schema=load_custom_schema()
        for key,value in schema.items():
            primary_key_name=key
        schema_lengths =len(schema[primary_key_name])
        num_entry=int(input("Enter the number of entries you want to add: "))
        try:
            database=load_database()
        except FileNotFoundError:
            database = {}
        if num_entry <= 0:
            print("Please enter a positive number of entries.")
        else:
            for i in range(num_entry):
                primary_key = input(f"Enter {primary_key_name} for entry number{i + 1}: ")
                if primary_key in database:
                    print("Primary key already exists you cannot add it to")
                else:
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

        python_file_content = database
        with open(f"{database_name}.eL", "w") as file:
            dump(python_file_content,file)
    except FileNotFoundError:
        print("scheme not found/error ") 
    except ValueError:
        print("type anly the assigned datatypes")
    except OSError as e:
        print(f"{e} has occured\nPlease allow your antivirus to make changes to a purticuular file/folder")
    except Exception as e:
        print(f"Error occured\nError name:{e}")

def view_all():
    database = load_database()
    headers,rows=table_loader(database)
    print(tabulate(rows,headers,tablefmt="rounded_grid"))
def search_database(primary_key):
    database=load_database()

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
    
    primary_key = input(f"Enter primary key to search: ")
        
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
        
        with open(f"{database_name}.eL", "w") as file:
            dump(database,file)
        print("Database Updated")
        print("=" * 100)
        print(f"      Primary key: {primary_key}")
        print("-" * 100)
        for field_name, value in database[primary_key].items():
            print(f"      {field_name}: {value}")
    else:
        print("roll number",primary_key,"not found in the database")

def delete_data_database():
    database=load_database()
    primary_key=str(input("enter the primary key of the desired to delete:"))
    if primary_key in database:
        search_database(primary_key)
        yn=input(f"do you want to delete {primary_key} y/n:")
        if yn.lower()=="y" or yn.lower()=="yes":
            del database[primary_key]
            dump_database(database)
        else:
            print("deletion abandoned")
    else:
        print("Primary key not found")
def export_file_as_excel(database):
    from openpyxl import Workbook as workbook       #lazy
    wbk=workbook()
    wak=wbk.active
    wak.title=f"{database_name}"
    headers,rows=table_loader(database)
    wak.append(headers)
    for i in rows:
        wak.append(i)
    from openpyxl.styles import Font
    for cell in wak[1]:
        cell.font = Font(bold=True)
    wbk.save(f"{database_name}.xlsx") 
def database_name_taker():
    while True:
        database_name=str(input("Enter the name of the database to do the operations:"))
        try:
            with open(f"{database_name}.eL", "r") as file:
                load(file)
            if database_name!="" or database_name!=" ":
                return database_name
        except FileNotFoundError:
            print(f"You will have create a new database {database_name} as the file doesnt exist \nand later continue to do operations on it") 
            question1=str(input("do you want to create new database?y/n:"))
            if question1.lower()=="y" or question1.lower()=="yes":
                with open(f"{database_name}.eL", "w") as file:
                    pass 
            return database_name
        except Exception as e:
            print(f"Error occured\nError name:{e}")
database_name=database_name_taker()
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
        clear_screen()
        create_default_database()
    elif option.lower()=="create custom schema" or option=="2":
        clear_screen()
        custom_schema()
    elif option.lower()=="add data" or option=="3":
        clear_screen()
        add_custom_data()
    elif option.lower()=="view all" or option=="4":
        clear_screen()
        view_all()
    elif option.lower()=="search" or option=="5":
        clear_screen()
        primary_key = input(f"Enter primary key to search: ")
        search_database(primary_key)
    elif option.lower()=="update" or option=="6":
        update_database()
    elif option.lower()=="help" or option=="7":
        clear_screen()
        help_data=[[1,"Create Default","Initialize a standard student database with predefined fields\n(Name, DOB, Father's Name, Mother's Name) and auto-generated\nunique Roll Numbers (e.g., A0001).",],[2,"Create Custom","Define your own database schema structure by specifying custom field\nnames and data types (str, int, float) to store tailored records.",],[3,"Add Data","Insert new entries into an existing database using its established\ncustom schema definition.",],[4,"View All","Display every record stored in the current active database file\nformatted field by field.",],[5,"Search","Find and display details for a specific record by entering its\nunique primary key or Roll Number.",],[6,"Update","Modify values in an existing record field by field. Press ENTER\nwithout typing to keep existing data unchanged.",],[7,"Help","Display this detailed navigation guide and system commands overview.",],[8,"Exit","Safely save all current operations, close database files, and terminate\nthe program session.",],]                          
        headers = ["Option", "Action", "Description"]
        print(tabulate(help_data,headers,tablefmt="rounded_grid"))
    elif option.lower()=="del":
        delete_data_database()
    elif option.lower()=="export":
        clear_screen()
        database=load_database()
        export_file_as_excel(database)
    elif option.lower()=="exit" or option=="8":
        clear_screen()
        print("""Kicking you out of the program......
DONE.""")
        break
    else:
        clear_screen()
        print("input valid option create/search")
    print("#" * 100)
