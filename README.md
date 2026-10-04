# registrarY

[![Download v1.35 Beta Executable](https://img.shields.io/badge/registrarY.exe_%28v1.35_Beta%29-Download-0078D4?style=flat\&logo=windows11\&logoColor=white)](https://github.com/lyashwith/registrarY/releases/download/1.35beta/registrarY.1.35beta.exe)
[![Download v1.3 Beta Executable](https://img.shields.io/badge/registrarY.exe_%28v1.3_Beta%29-Download-0078D4?style=flat\&logo=windows11\&logoColor=white)](https://github.com/lyashwith/registrarY/releases/download/v1.3beta/registrarY-1.3-beta.exe)
[![GitHub Repository](https://img.shields.io/badge/GitHub-registrarY_Repository-181717?style=flat\&logo=github\&logoColor=white)](https://github.com/lyashwith/registrarY)
[![Download Source Code](https://img.shields.io/badge/Download-Source_Code-24292E?style=flat\&logo=github\&logoColor=white)](https://github.com/lyashwith/registrarY/archive/refs/heads/main.zip)

**registrarY** is a lightweight Python command-line interface (CLI) application for creating, storing, searching, updating, and deleting structured records.

It supports both **automatically generated student records** and **custom database schemas**, making it useful for learning about Python, file handling, JSON, CRUD operations, and basic database concepts.

> ⚠️ **Current Status:** registrarY is a beginner-friendly project currently under development. Features, storage methods, and internal behaviour may change in future versions.

---

## 🚀 Features

### 🧭 Interactive CLI

registrarY provides an interactive command-line interface for performing database operations.

Current operations include:

* Creating a default database
* Creating a custom schema
* Adding records
* Viewing records
* Searching records
* Updating records
* Deleting individual records
* Viewing help information
* Exiting the application

The main menu currently contains:

```text
(1) Create default
(2) Create custom Schema
(3) Add data
(4) View all
(5) Search
(6) Update
(7) Help
(8) Exit
```

The delete operation can currently be accessed using:

```text
del
```

---

## 📝 Custom Schema Creation

registrarY allows users to define their own database structure.

A custom schema consists of:

* A primary key
* Field names
* Data types

Currently supported data types:

```text
str
int
float
```

Example:

```text
name;str,age;int,percentage;float
```

Custom schemas are stored separately from the database.

---

## 🔢 Automatic Roll Number Generation

The default database mode automatically generates sequential roll numbers.

Example:

```text
A0001
A0002
A0003
A0004
```

The default student record contains fields such as:

```text
Name
Date of Birth
Father's Name
Mother's Name
```

---

## 💾 JSON-Based Storage

The current version uses JSON for database storage.

Database files use the custom:

```text
.eL
```

extension.

For example:

```text
students.eL
```

The database is loaded and saved using Python's built-in `json` module.

Custom schemas are also stored separately using `.eLs` files.

Example:

```text
custom_schema-students.eLs
```

---

## 🔍 Search

Records can be searched using their primary key.

If the requested key exists, the corresponding record is displayed.

If it does not exist, registrarY reports that the record could not be found.

---

## 📋 View Records

The **View All** operation displays the records currently stored in the selected database.

---

## ✏️ Update Records

Existing records can be updated using their primary key.

When updating a record, pressing **Enter** without entering a new value keeps the existing value.

---

## 🗑️ Delete Records

Individual records can be deleted using their primary key.

The program asks for confirmation before deleting the selected record.

The delete operation is currently accessed using:

```text
del
```

---

# 💻 Installation & Usage

## Option 1 — Run from Source

### 1. Clone the repository

```bash
git clone https://github.com/lyashwith/registrarY.git
```

### 2. Navigate to the project

```bash
cd registrarY
```

### 3. Install the dependency

```bash
pip install tabulate
```

### 4. Run registrarY

```bash
python registrarY/registrarY.py
```

Make sure Python 3 is installed and available in your system PATH.

---

## Option 2 — Windows Executable

If you do not want to install Python or the required Python packages, you can use the **pre-built Windows executable**.

The executable is intended for Windows systems and can be run directly after downloading.

### v1.35 Beta — Recommended

[![Download v1.35 Beta](https://img.shields.io/badge/Download-v1.35_Beta-0078D4?style=flat\&logo=windows11\&logoColor=white)](https://github.com/lyashwith/registrarY/releases/download/1.35beta/registrarY.1.35beta.exe)

**Download:** [registrarY v1.35 Beta](https://github.com/lyashwith/registrarY/releases/download/1.35beta/registrarY.1.35beta.exe)

### v1.3 Beta — Older Version

[![Download v1.3 Beta](https://img.shields.io/badge/Download-v1.3_Beta-0078D4?style=flat\&logo=windows11\&logoColor=white)](https://github.com/lyashwith/registrarY/releases/download/v1.3beta/registrarY-1.3-beta.exe)

**Download:** [registrarY v1.3 Beta](https://github.com/lyashwith/registrarY/releases/download/v1.3beta/registrarY-1.3-beta.exe)

> **Note:** v1.35 Beta is the newer executable. v1.3 Beta is provided as an older release.

No Python installation is required when using the pre-built executable.

---
## 🛡️ Windows Defender / Antivirus Notice

Some users may receive an antivirus warning when downloading or running the pre-built Windows executable.

The `registrarY` Windows executable is packaged from the Python source using **PyInstaller**. PyInstaller-packaged executables can sometimes trigger heuristic or machine-learning-based antivirus detections because the executable contains a bundled Python runtime and packaging components.

For example, Windows Defender may report:

```text
Trojan:Win32/Wacatac.C!ml
```

with a message such as:

```text
This program is dangerous and executes commands from an attacker.
```

### ⚠️ Important

This detection **does not by itself prove that registrarY contains malware**, but it should not be ignored.

The current executable should therefore be treated with caution until the detection has been independently verified.

**Do not disable Windows Defender or add an antivirus exclusion simply to run the executable.**

If Windows Defender blocks the executable:

1. Keep the file quarantined or removed.
2. Do not bypass the warning just to run the program.
3. Consider running the executable through multiple antivirus scanners.
4. The source code is available in this repository so that users can inspect and build the application themselves.
5. Future releases may provide updated builds after antivirus compatibility has been investigated.

### 🔧 Recommended: Run From Source

Users who do not want to use the pre-built executable can run registrarY directly from the Python source.

Install the required dependency:

```bash
pip install tabulate
```

Then run:

```bash
python registrarY/registrarY.py
```

Running from source allows users to inspect the Python code directly instead of using the packaged executable.

> **Note:** Antivirus detections can change between releases and antivirus engines. A detection such as `Wacatac.C!ml` is a heuristic/machine-learning classification and should be investigated rather than automatically assumed to be either malware or a false positive.

## 🧩 Custom Schema Format

Custom schemas use:

```text
field_name;type
```

Multiple fields are separated by commas.

Example:

```text
name;str,age;int,percentage;float
```

The first input when creating a custom database is used to define the primary key.

A schema can therefore be structured like:

```text
{
    "id": {
        "name": "str",
        "age": "int"
    }
}
```

---

## 🔄 Database Operations

registrarY follows a basic CRUD-style approach:

| Operation  | Description                                |
| ---------- | ------------------------------------------ |
| **Create** | Create a default database or custom schema |
| **Read**   | View and search records                    |
| **Update** | Modify existing records                    |
| **Delete** | Remove individual records                  |

---

# 🐛 Known Issues & Limitations

### 1. Entire JSON Database Is Loaded Into Memory

The current implementation loads the database into a Python dictionary before performing operations.

For example, searching does not currently work by reading only a small portion of the database.

Therefore, very large databases may require significant memory.

---

### 2. No Chunk-Based Searching

registrarY does not currently support loading a fixed number of records at a time.

For example, it does not currently perform:

```text
Load first 100 records
        ↓
Search
        ↓
Not found
        ↓
Load next 100 records
```

The complete JSON database is currently loaded instead.

---

### 3. Update May Change the Data Type

During record creation, custom values are converted according to their schema.

For example:

```text
age;int
```

can store:

```text
18
```

However, during an update, the new value is currently received as normal text input.

Therefore, a value that was originally an integer may become a string after being updated.

---

### 4. Limited Input Validation

Some invalid inputs are handled, but input validation is not yet comprehensive.

Incorrect values can still result in errors or unexpected behaviour in some situations.

---

### 5. `int` and `float` Conversion Errors

When a custom field is defined as:

```text
age;int
```

entering:

```text
abc
```

cannot be converted into an integer.

Similarly:

```text
percentage;float
```

cannot accept arbitrary non-numeric text.

These situations can produce a Python `ValueError`.

---

### 6. Limited Data Types

Only three data types are currently supported:

```text
str
int
float
```

Types such as:

```text
bool
date
list
dict
```

are not currently supported by the custom schema system.

---

### 7. Strict Schema Format

Custom schemas must follow the required format:

```text
field_name;type
```

For example:

```text
name;str,age;int,percentage;float
```

Incorrect formatting may result in parsing errors or unexpected behaviour.

---

### 8. Custom Schema Must Exist Before Adding Data

The **Add Data** operation depends on the corresponding custom schema file.

A custom schema must therefore be created before adding records using that schema.

---

### 9. Database and Schema Files Are Local Files

registrarY currently stores its database and schema files locally.

There is no built-in:

* Cloud synchronization
* Remote database
* Multi-user database access
* Network database support

---

### 10. No Authentication

registrarY does not currently provide:

* User accounts
* Passwords
* Authentication
* User permissions
* Role-based access control

Anyone who can access the database files can potentially modify them.

---

### 11. No Encryption

The `.eL` files are not encrypted.

The database contents can be read or modified by someone who has access to the files.

Therefore, registrarY should not currently be used for sensitive or confidential information.

---

### 12. `.eL` Is a Custom File Extension

`.eL` is a custom extension created for registrarY.

It is not a standard database format.

The contents are JSON data, so manually modifying the file incorrectly can make it unreadable by the program.

---

### 13. Delete Is Not a Numbered Menu Option

Although deleting records is supported, it is currently accessed using:

```text
del
```

rather than a numbered option in the main menu.

---

### 14. Fixed Default Database Fields

The default database is designed around student records.

Its fields are predefined and cannot be customized through the default database creation option.

Custom fields should be created using the custom schema feature.

---

### 15. No Transaction or Recovery System

registrarY does not currently provide:

* Transactions
* Automatic backups
* Rollback
* Crash recovery
* Version history

A damaged or accidentally modified database file may therefore require manual recovery.

---

### 16. Not Designed for Large Production Databases

registrarY is primarily a learning and hobby project.

It is not intended to replace established database systems such as:

* SQLite
* MySQL
* PostgreSQL
* MongoDB

Large-scale applications may experience performance and reliability limitations.

---

# 🛠️ Project Structure

```text
registrarY/
│
├── registrarY/
│   └── registrarY.py
│       └── Main CLI application
│
├── <database_name>.eL
│   └── JSON database file
│
├── custom_schema-<database_name>.eLs
│   └── JSON custom schema
│
├── LICENSE
│
└── README.md
```

Database and schema files may be generated dynamically while using registrarY.

---

# 🎯 Project Goals

registrarY was created as a learning and hobby project for exploring:

* Python programming
* Dictionaries
* JSON
* File handling
* Dynamic schemas
* Data type conversion
* CRUD operations
* Command-line interfaces
* Local data persistence
* Error handling
* Basic database concepts

The project is intended primarily for learning and experimentation rather than production use.

---

# 🔐 Data & Security

registrarY stores database information locally using JSON-based `.eL` files.

The current storage system does not provide:

* Encryption
* Authentication
* Access control
* Automatic backups
* Database recovery

Do not use registrarY for storing sensitive personal, financial, medical, password, or other confidential information.

---

# 📈 Future Improvements

Possible future improvements include:

* Better input validation
* Type-aware updates
* Improved error handling
* Chunk-based database searching
* More efficient handling of large databases
* Additional data types
* Better schema validation
* Adding Delete to the main numbered menu
* Database backup and recovery
* Export/import functionality
* Improved CLI formatting
* Optional encryption
* Improved database management

---

# 📄 License

registrarY is licensed under the **Free Use, No-Sale License (FUNSL) v1.0**.

The software may be used for:

* Personal purposes
* Educational purposes
* Research
* Internal organizational use
* Commercial purposes

However:

* The software itself may **not be sold**.
* The original software may be redistributed **free of charge** with attribution and the license included.
* Modified versions may be used privately or internally.
* Public redistribution of modified versions requires permission from the author.

See [`LICENSE`](LICENSE) for the complete license terms.

---

# 👤 Author

Developed by **Yashwith L.**

<a href="https://github.com/lyashwith"> <img src="https://avatars.githubusercontent.com/u/313887780?s=100" alt="GitHub Logo" width="50"> </a>

---

# ⭐ Support

If you find registrarY useful or interesting, consider giving the repository a ⭐ on GitHub.

**Repository:**

https://github.com/lyashwith/registrarY
**ai generated readme**
