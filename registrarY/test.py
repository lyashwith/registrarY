import tabulate as table
import pandas as pd
database={'1234567890': {'name': 'jojo', 'abcd_id': 987654321, 'value': 0.0, 'salary': -100}, '2345678901': {'name': 'happy', 'abcd_id': 1098765432, 'value': 12.0, 'salary': 2}}
table_data = []
for user_id, info in database.items():
    row = {'Primary key': user_id, **info}
    table_data.append(row)


print(table.tabulate(table_data, headers="keys", tablefmt="grid"))
with open("abcd.txt","w") as file:
    file.write(table.tabulate(table_data, headers="keys", tablefmt="grid"))

# 2. Convert data into a Pandas DataFrame
df = pd.DataFrame(table_data)

# 3. Export the DataFrame to an Excel file
df.to_excel("output.xlsx", sheet_name="Sheet1", index=False)
