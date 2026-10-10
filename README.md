# registrarY

[![Download v1.35 Beta](https://img.shields.io/badge/Download-v1.35_Beta-0078D4?style=flat&logo=windows11&logoColor=white)](https://github.com/lyashwith/registrarY/releases/download/1.35beta/registrarY.1.35beta.exe)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=flat&logo=github&logoColor=white)](https://github.com/lyashwith/registrarY)

**registrarY** is a Python-based command-line application for creating and managing structured records using JSON-based local storage. It supports predefined student records, user-defined schemas, CRUD operations, formatted table views, and Excel export.

The project explores Python dictionaries, file handling, JSON serialization, schema-based data entry, and basic database management.

## Features

- **Database selection:** Enter a database name at startup and create a new database when the corresponding file does not exist.
- **Default database:** Create student records with predefined fields and automatically generated roll numbers.
- **Custom schemas:** Define a primary key, field names, and data types.
- **Add records:** Insert records using the selected custom schema.
- **View records:** Display stored records in a formatted table.
- **Search records:** Find a record using its primary key.
- **Update records:** Modify existing field values while retaining unchanged values.
- **Delete records:** Remove records after confirmation.
- **Excel export:** Export database records to an `.xlsx` file with bold column headers.
- **Interactive help:** View the available menu options and their descriptions.

## Menu

The application provides the following numbered options:

| Option | Operation |
|:---:|---|
| 1 | Create default |
| 2 | Create custom schema |
| 3 | Add data |
| 4 | View all |
| 5 | Search |
| 6 | Update |
| 7 | Delete |
| 8 | Export |
| 9 | Help |
| 10 | Exit |

You can select an operation using its number or, where supported, its command name.

## Requirements

- Python 3
- `tabulate` for formatted tables
- `openpyxl` for Excel export

The `json`, `os`, and `subprocess` modules are part of the Python standard library.

## Installation

### Option 1: Run from source

Clone the repository:

```bash
git clone https://github.com/lyashwith/registrarY.git
```

Navigate to the project directory:

```bash
cd registrarY
```

Install the required packages:

```bash
python -m pip install tabulate openpyxl
```

Run the application:

```bash
python registrarY/registrarY.py
```

Depending on your installation, you may need to use `python3` instead of `python`.

### Option 2: Windows executable

A pre-built Windows executable is available for users who prefer not to run the Python source directly.

**Latest listed executable: v1.35 Beta**

[Download registrarY v1.35 Beta](https://github.com/lyashwith/registrarY/releases/download/1.35beta/registrarY.1.35beta.exe)

[View all repository releases](https://github.com/lyashwith/registrarY/releases)

The executable is packaged using PyInstaller. No separate Python installation is normally required to run a compatible packaged build.

### Option 3: Run Directly Using Python (No Git Required)

If you have Python installed, you can run registrarY directly from its GitHub source without cloning the repository or using Windows-specific tools.

**1. Install the required packages**

```bash
python -m pip install tabulate openpyxl
```

**2. Run registrarY**

```python
import urllib.request

try:
    url = "https://raw.githubusercontent.com/lyashwith/registrarY/refs/heads/main/registrarY/registrarY.py"

    with urllib.request.urlopen(url) as response:
        code = response.read().decode("utf-8")

    exec(code)

except Exception as e:
    print(e)
```

Save this snippet as `run_registrarY.py` and execute it:

```bash
python run_registrarY.py
```

**Requirements**
- Python 3
- `tabulate`
- `openpyxl` (required for Excel export)

**Note:** This method requires an internet connection each time you run the launcher. It executes Python code downloaded from the repository, so review the source code before running it. Exceptions raised during the execution are caught and printed.

## Creating a database

When registrarY starts, enter a database name.

For example:

```text
Enter the name of the database to do the operations: students
```

The application looks for `students.eL`. If the file does not exist, it offers the option to create a new database.

Database names should be simple names rather than paths or names containing filesystem-special characters.

## Default student database

Choose **1 — Create default** and enter the number of student records.

Each record contains the following fields:

| Field | Description |
|---|---|
| `Name` | Student's name |
| `date_of_birth` | Date of birth |
| `father_name` | Father's name |
| `mother_name` | Mother's name |

Roll numbers are generated sequentially, beginning with identifiers such as:

```text
A0001
A0002
A0003
```

The date of birth is requested in `DD-MM-YYYY` format.

## Custom schemas

Choose **2 — Create custom schema** to define a record structure.

First, provide the primary key field name. Then enter the other fields and their data types in this format:

```text
name;str,age;int,percentage;float
```

For example, entering `id` as the primary key produces a schema similar to:

```json
{
  "id": {
    "name": "str",
    "age": "int",
    "percentage": "float"
  }
}
```

### Supported data types

| Type | Description | Example |
|---|---|---|
| `str` | Text | `"Yashwith"` |
| `int` | Integer | `18` |
| `float` | Floating-point number | `93.17` |

The primary key identifies each record and must be unique within the database.

Create the custom schema before using **Add Data** with that schema.

## Adding records

Choose **3 — Add data**.

The application requests the primary key for each record, followed by the values of the fields defined in the custom schema.

For example:

```text
Enter id for entry number1: 101
Enter name (string): Arun
Enter age (integer): 18
Enter percentage (float): 93.17
```

The record is stored under its primary key. If a key already exists, the application rejects the duplicate rather than adding another record with the same key.

## Viewing and searching records

### View all

Choose **4 — View all** to display the database as a formatted table using `tabulate`.

### Search

Choose **5 — Search** and enter a primary key.

The application displays the matching record if it exists; otherwise, it reports that the key was not found.

## Updating records

Choose **6 — Update** and enter the primary key of the record to modify.

The application displays the existing record and prompts for replacement values. Press **Enter** without typing a new value to keep the current value.

Updated records are saved to the database file.

**Note:** The current update implementation accepts new values as text. Consequently, updating an integer or floating-point field may change its stored Python type to a string.

## Deleting records

Choose **7 — Delete** and enter the primary key of the record to remove.

The application displays the selected record and asks for confirmation. Confirming the operation removes the record and saves the updated database.

## Exporting to Excel

Choose **8 — Export** to export the active database to an Excel workbook.

For a database named `students`, the output is:

```text
students.xlsx
```

The exported worksheet contains the column headers followed by the database records. The header row is formatted in bold.

Excel export requires `openpyxl`. Install it using:

```bash
python -m pip install openpyxl
```

## File formats and storage

registrarY uses JSON serialization through Python's built-in `json` module. The file extensions are custom to this project; they do not represent separate database formats.

| File | Purpose |
|---|---|
| `<database_name>.eL` | Stores database records |
| `custom_schema-<database_name>.eLs` | Stores the custom schema |
| `<database_name>.xlsx` | Exported Excel workbook |

For example, a database named `students` may use:

```text
students.eL
custom_schema-students.eLs
students.xlsx
```

The `.eL` and `.eLs` files contain JSON data despite their custom extensions.

The current implementation loads the database into a Python dictionary for operations. It is not a chunk-based or indexed storage engine.

## Windows Defender and antivirus notice

A previously distributed PyInstaller executable, `registrarY.1.35beta.exe`, was reported by Windows Defender as:

```text
Trojan:Win32/Wacatac.C!ml
```

This detection alone does not establish whether the executable is malicious or a false positive. The executable should be treated cautiously until the detection has been independently investigated.

If an antivirus product flags the executable:

- Do not ignore the warning or disable antivirus protection simply to run it.
- Keep the flagged file quarantined or removed while the detection is investigated.
- Consider inspecting the source code and building the application yourself.
- Remember that running from source also requires reviewing the code and installing dependencies from trusted sources.

The availability of source code does not, by itself, establish that a compiled executable is safe.

## Current limitations

- **Local storage:** Database files are stored locally; there is no built-in cloud synchronization or remote database.
- **Memory usage:** The complete JSON database is loaded into memory during operations.
- **Input validation:** Some inputs are validated, but validation is not comprehensive.
- **Update types:** Updated values are not automatically converted according to the schema.
- **Supported schema types:** Only `str`, `int`, and `float` are implemented.
- **Schema formatting:** Custom schema input must follow the required comma- and semicolon-separated format.
- **Security:** Database files are not encrypted, and the application does not provide authentication or access control.
- **Recovery:** Automatic backups, transactions, and rollback are not implemented.
- **Production suitability:** The application is intended for learning and experimentation rather than critical or large-scale database workloads.

Avoid storing sensitive or confidential information in the current version.

## Project structure

```text
registrarY/
├── registrarY/
│   └── registrarY.py
├── LICENSE
└── README.md
```

Database files, schema files, and Excel exports are generated as needed when using the application.

## License

registrarY is distributed under the **Free Use, No-Sale License (FUNSL) v1.0**.

The license permits specified uses while restricting the sale of the software and the public redistribution of modified versions without permission. Refer to the [`LICENSE`](LICENSE) file for the complete terms.

## Author

**Yashwith L.**
<a href="https://github.com/lyashwith"> <img src="https://avatars.githubusercontent.com/u/313887780?s=100" alt="GitHub Logo" width="50"> </a>

## Repository

[![GitHub Repository](https://img.shields.io/badge/GitHub-registrarY_Repository-181717?style=flat\&logo=github\&logoColor=white)](https://github.com/lyashwith/registrarY)

If you find the project interesting, consider giving it a ⭐.
