from databaseD import database

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

print("-" * 40)
for roll_no, details in database.items():
        print(f"      Roll Number: {roll_no}")
        print("-" * 40)
        print(f"      Name         : {details['Name']}")
        print(f"      Date of Birth: {details['date_of_birth']}")
        print(f"      Father's Name: {details['father_name']}")
        print(f"      Mother's Name: {details['mother_name']}")
        print("-" * 40)
