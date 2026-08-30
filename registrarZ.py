from datetime import datetime
dictionary_database={}
count=1
while True:
    customer_no=count
    if customer_no not in dictionary_database:
        dictionary_database[customer_no] = {"date_time": str(datetime.now()),"items": {},}
    while True:
        item_name=str(input("Enter the item name: "))
        unit_price=float(input("Enter the unit price: "))
        quantity=int(input("Enter the quantity: "))
        total_price=unit_price*quantity
        dictionary_database[customer_no]["items"][item_name]={"unit_price":unit_price,"quantity":quantity,"total_price":total_price}
        extra_lines=input("Do you want to add more items? (yes/no): ")
        if extra_lines.lower() != "yes" and extra_lines.lower() != "y":
            break
    count+=1
    if input("Do you want to add another customer? (yes/no): ").lower() != "yes":
        break
print(dictionary_database)
