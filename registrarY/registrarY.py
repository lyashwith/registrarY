from json import dump,load
from os import name as os_name
from subprocess import run as sub_run
from tabulate import tabulate
__lazy_modules__ = ["openpyxl","subprocess","os"]
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
    with open(f"{database_name}.eL", "w") as file:
        dump(database,file)

def load_database():
    try:
        with open(f"{database_name}.eL", "r") as file:
            k=load(file)
            if k==None:
                return {}
            else:
                return k
    except FileNotFoundError as e:
        print(f"Database file not found: {e}")

def load_custom_schema():
    try:
        with open(f"custom_schema-{database_name}.eLs", "r") as file:
            content = load(file)
            if content==None:
                return {}
            else:
                return content
    except FileNotFoundError as e:
        print(f"Database file not found: {e}")


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
        dump_database(database)
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
        headers,table_list=table_loader(database)
        for i,j in enumerate(table_list):
            if primary_key in j:
                print(tabulate([table_list[i]],headers,tablefmt="rounded_grid"))
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
            print("Deletion done")
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
            if database_name!="" and database_name!=" ":
                return database_name
        except FileNotFoundError:
            print(f"You will have create a new database {database_name} as the file doesnt exist \nand later continue to do operations on it") 
            question1=str(input("do you want to create new database?y/n:"))
            if question1.lower()=="y" or question1.lower()=="yes":
                with open(f"{database_name}.eL", "w") as file:
                    dump({},file)
            return database_name
        except Exception as e:
            print(f"Error occured\nError name:{e}")
database_name=database_name_taker()
while True:
    menu = [["(1)", "Create default"],["(2)", "Create custom Schema"],["(3)", "Add data"],["(4)", "View all"],["(5)", "Search"],["(6)", "Update"],["(7)", "Delete"],["(8)", "Export"],["(9)", "Help"],["(10)", "Exit"]]
    print("What do you want to do? ")
    print(tabulate(menu,tablefmt="rounded_grid"))
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
    elif option.lower()=="del" or option.lower()=="delete" or option.lower()=="7":
        delete_data_database()
    elif option.lower()=="export" or option.lower()=="8":
        clear_screen()
        database=load_database()
        print("File save successfully")
        export_file_as_excel(database)
    elif option.lower()=="help" or option=="9":
        clear_screen()
        help_data = [
    [1, "Create Default\n",
     "Create a standard student database with predefined fields\n"
     "Name, Date of Birth, Father's Name, and Mother's Name. \n"
     "Automatically generate unique Roll Numbers (e.g., A0001) \n"
     "for each student record.\n"],

    [2, "Create Custom Schema\n",
     "Design a database structure by specifying a unique primary key \n"
     "and custom field names with their data types (str, int, float). \n"
     "The schema defines the fields available when adding and managing records.\n"],

    [3, "Add Data\n",
     "Insert new records into the active database using its defined schema. \n"
     "Enter a unique primary key and provide values matching the assigned \n"
     "data types. Existing primary keys cannot be reused.\n"],

    [4, "View All\n",
     "Display all records in the active database in a structured table. \n"
     "Column headers are generated from the schema, making records easier \n"
     "to read and compare.\n"],

    [5, "Search\n",
     "Retrieve a specific record by entering its unique primary key \n"
     "or Roll Number. Displays the matching record's primary key, \n"
     "field names, and stored values.\n"],

    [6, "Update\n",
     "Modify the field values of an existing record by entering its \n"
     "primary key. Press ENTER without typing a new value to retain \n"
     "the existing value. Changes are saved to the database file.\n"],

    [7, "Delete\n",
     "Remove a record from the active database using its primary key. \n"
     "The record is displayed before deletion, and confirmation is \n"
     "requested to help prevent accidental data loss.\n"],

    [8, "Export\n",
     "Export the active database records to an Excel (.xlsx) file. \n"
     "The first row contains column headers formatted in bold, followed \n"
     "by the database records. Requires the openpyxl package.\n"],

    [9, "Help\n",
     "Display this navigation guide, including menu options, feature \n"
     "descriptions, and supported commands for managing the database.\n"],

    [10, "Exit\n",
     "Terminate the registrarY session. Database modifications are \n"
     "saved by their respective operations before exiting.\n"]
]
        headers = ["Option", "Action", "Description"]
        print(tabulate(help_data,headers,tablefmt="rounded_grid"))
    elif option.lower()=="exit" or option=="10":
        clear_screen()
        print("""Kicking you out of the program......
DONE.""")
        break
    else:
        clear_screen()
        print("input valid option create/search")
    print("#" * 100)
