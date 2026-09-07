from ast import literal_eval


def custom_schema():
    primary_key=input("Enter unique primary key field:")
    fields=input("enter fields with data type(example name:str,age:int,gender:str):")
    schema={}
    schema[primary_key] = {}
    for i in fields.split(","):
        field_name, data_type = i.split(":",1)
        schema[primary_key][field_name] = data_type
    print("Custom schema created:",schema)
    with open("custom_schema.py", "w") as file:
        file.write(str(schema))
def add_custom_data():
    database_name=input("Enter the database name to add data: ")
    with open("custom_schema.py", "r") as file:
        content = file.read()
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
add_custom_data()
