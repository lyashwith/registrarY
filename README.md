# registrarY

[![Download v1.3 Beta Executable](https://img.shields.io/badge/registrarY.exe_\(v1.3_Beta\)-Download-0078D4?style=flat\&logo=windows11\&logoColor=white)](https://github.com/lyashwith/registrarY/releases/download/v1.3beta/registrarY-1.3-beta.exe)
[![Download v1.2.0.1 Beta Executable](https://img.shields.io/badge/registrarY.exe_\(v1.2.0.1_Beta\)-Download-0078D4?style=flat\&logo=windows11\&logoColor=white)](https://github.com/lyashwith/registrarY/releases/download/v1.2.0.1beta/registrarY.v1.2.0.1beta.exe)
[![GitHub Repository](https://img.shields.io/badge/GitHub-registrarY_Repository-181717?style=flat\&logo=github\&logoColor=white)](https://github.com/lyashwith/registrarY)
[![Download Source Code](https://img.shields.io/badge/Download-Source_Code_.ZIP_(v1.3beta)-24292E?style=flat&size=large&logo=github&logoColor=white)](https://github.com/lyashwith/registrarY/archive/refs/tags/v1.3beta.zip)


A lightweight Python command-line interface (CLI) application for creating, storing, searching, and updating records.

registrarY supports both **automatically generated sequential roll numbers** and **fully custom schemas**, making it suitable for managing student records and other structured record collections.

> ⚠️ **Current Status:** registrarY is a beginner-friendly project currently in beta development. Some features and storage behaviour may change in future releases.

---

## 🚀 Features

### 🧭 Interactive CLI Menu

Navigate through options for:

* Creating databases and entries
* Creating custom schemas
* Adding custom data
* Viewing records
* Searching records
* Updating existing records
* Viewing help information
* Exiting the application

### 📝 Custom Schema Creation

Create databases with your own:

* Primary key name
* Field names
* Data types

Currently supported data types include:

```text
str
int
float
```

Custom schemas are stored separately using files such as:

```text
custom_schema<database_name>.py
```

### 🔢 Automatic Roll Number Generation

For default databases, registrarY can automatically generate sequential roll numbers such as:

```text
A0001
A0002
A0003
...
```

### 🔍 Record Search

Search for individual records using their primary key.

### 📋 View Records

Display all records stored in a database.

### ✏️ Update Records

Update individual fields while keeping existing values unchanged.

Pressing **Enter** without entering a new value preserves the current value.

---

## 💻 Installation & Usage

### Option 1: Run from Source

#### 1. Clone the repository

```bash
git clone https://github.com/lyashwith/registrarY.git
```

#### 2. Navigate to the project folder

```bash
cd registrarY
```

#### 3. Run the application

```bash
python registrarY.py
```

Make sure Python is installed and available in your system PATH.

---

### Option 2: Windows Executable

You can download a pre-built Windows executable from the releases:

* **v1.3 Beta:** Use the download button at the top of this README.
[![Download v1.3 Beta Executable](https://img.shields.io/badge/registrarY.exe_\(v1.3_Beta\)-Download-0078D4?style=flat\&logo=windows11\&logoColor=white)](https://github.com/lyashwith/registrarY/releases/download/v1.3beta/registrarY-1.3-beta.exe)
* **v1.2.0.1 Beta:** Also available from the download button above.

No Python installation is required when using the executable.

---

## 🧩 Custom Schema Format

Custom schemas currently use the following format:

```text
field_name;type
```

Multiple fields are separated using commas.

### Example

```text
name;str,age;int,percentage;float
```

This creates fields similar to:

```text
Name        → String
Age         → Integer
Percentage  → Float
```

---

## 🗺️ Roadmap

Planned improvements for future versions include:

* [ ] **Improved Data Persistence**
  Move away from storing data in Python scripts and use dedicated data files.

* [ ] **Better Input Validation**
  Re-prompt users when invalid values are entered.

* [ ] **Improved Exception Handling**
  Prevent crashes caused by malformed menu choices or incorrect numeric input.

* [ ] **Database Encryption**
  Explore optional encryption for locally stored database files.

* [ ] **Improved CLI Interface**
  Add better formatting, tables, and coloured terminal output.

* [ ] **Duplicate Key Protection**
  Warn users before overwriting an existing record.

* [ ] **Custom Primary Key Prompts**
  Replace hardcoded references to "Roll Number" with the configured primary key name.

---

### 🐛 Known Issues & Limitations

* Schema File Dependency

Before adding data using a custom schema, you must first create the schema.

Option `(3) Add data` depends on the corresponding schema file existing:

```text
custom_schema<database_name>.py
```

---

* Data File Overwriting

Adding new custom entries or creating default entries may overwrite existing dataset files instead of appending new records.

---

* Invalid Data Type Input

Entering text when an `int` or `float` is expected can currently raise an unhandled:

```text
ValueError
```

Instead of automatically asking the user to enter the value again.

---

* Python File Storage

Database data is currently stored using `.py` files containing Python dictionary data.

The file must maintain valid Python dictionary syntax.

If the file becomes corrupted or contains invalid syntax, the program may fail when reading it with:

```python
ast.literal_eval()
```

---

* Hardcoded "Roll Number" Prompts

Some search and viewing prompts explicitly reference:

```text
Roll Number
```

even when a database uses a custom primary key name.

---

* Duplicate Primary Keys

If a primary key already exists, entering the same key may overwrite the existing record without displaying a confirmation warning.

---

* Strict Schema Formatting

Schema definitions must follow the required format:

```text
field_name;type
```

Multiple fields must be separated using commas.

Example:

```text
name;str,age;int,percentage;float
```

Incorrect formatting may cause parsing errors or unexpected schema behaviour.

---

* Entry Count Validation

In `create_default_database()`, non-numeric entry counts are handled.

However, entering:

```text
0
```

or a negative number may display an error without correctly re-prompting the user before data collection.

---

## 🛠️ Project Structure

```text
registrarY/
│
├── registrarY.py
│   └── Main CLI application
│
├── database.py
│   └── Database-related data or functionality
│
├── registrarZ.py
│   └── Additional project script
│
├── <database_name>.py
│   └── Generated database storage file
│
├── custom_schema<database_name>.py
│   └── Generated custom schema file
│
├── LICENCE
│   └── Project license
│
└── README.md
    └── Project documentation
```

> Some database and schema files are generated dynamically when using the application.

---

## 🎯 Project Goals

registrarY was created as a lightweight project for exploring concepts such as:

* Python programming
* Dictionaries and nested data structures
* File handling
* Dynamic schemas
* Data validation
* CRUD operations
* Command-line interfaces
* Local data persistence

It is designed primarily as a learning and hobby project rather than a production-ready database system.

---

## 📄 License

registrarY is licensed under the **Free Use, No-Sale License (FUNSL) v1.0**.

The Software may be used for personal, educational, research, internal organizational, and commercial purposes.

However:

* The Software itself may **not be sold**.
* The original Software may be redistributed **free of charge** with attribution and this License.
* Modified versions may be used privately or internally.
* Public redistribution of modified versions requires permission from the author.

See the [`LICENSE`](LICENSE) file for the complete license terms.

---

## 👤 Author

Developed by **Yashwith L**

[![GitHub](https://img.shields.io/badge/GitHub-lyashwith-181717?style=flat\&logo=github\&logoColor=white)](https://github.com/lyashwith)

---

⭐ If you find this project useful or interesting, consider giving the repository a star!
