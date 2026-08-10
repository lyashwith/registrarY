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
