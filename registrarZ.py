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
    with open("custom_schema.py", "r") as file:
        content = file.read()
    schema = literal_eval(content)
    for key,value in schema.items():
        primary_key=key
    schema_lengths =len(schema[primary_key])
    for j in range(schema_lengths):
        print("hiS")
custom_schema()
add_custom_data()

