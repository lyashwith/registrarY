<div align="center">
# registrarY
</div>

[![Download v1.35 Beta Executable](https://img.shields.io/badge/registrarY.exe_\(v1.35_Beta\)-Download-0078D4?style=flat\&logo=windows11\&logoColor=white)](https://github.com/lyashwith/registrarY/releases/download/1.35beta/registrarY.1.35beta.exe)
[![Download v1.3 Beta Executable](https://img.shields.io/badge/registrarY.exe_\(v1.3_Beta\)-Download-0078D4?style=flat\&logo=windows11\&logoColor=white)](https://github.com/lyashwith/registrarY/releases/download/v1.3beta/registrarY-1.3-beta.exe)
[![GitHub Repository](https://img.shields.io/badge/GitHub-registrarY_Repository-181717?style=flat\&logo=github\&logoColor=white)](https://github.com/lyashwith/registrarY)
[![Download Source Code](https://img.shields.io/badge/Download-Source_Code_.ZIP_\(v1.3beta\)-24292E?style=flat\&logo=github\&logoColor=white)](https://github.com/lyashwith/registrarY/archive/refs/tags/v1.3beta.zip)

**registrarY** is a lightweight Python command-line interface (CLI) application for creating, storing, searching, updating, and managing structured records.

It supports both **automatically generated sequential roll numbers** and **fully custom schemas**, making it suitable for managing student records and other structured collections of data.

> ⚠️ **Current Status:** registrarY is a beginner-friendly project currently in beta development. Features, storage methods, and internal behaviour may change in future releases.

---

## 🚀 Features

### 🧭 Interactive CLI

registrarY provides an interactive command-line interface for performing database operations.

Current operations include:

* Creating databases
* Creating custom schemas
* Adding records
* Viewing records
* Searching records
* Updating records
* Deleting records using a primary key
* Viewing help information
* Exiting the application

### 📝 Custom Schema Creation

Create databases with your own:

* Primary key
* Field names
* Data types

Currently supported data types:

```text
str
int
float
```

Example schema:

```text
name;str,age;int,percentage;float
```

Custom schema definitions are stored separately using files such as:

```text
custom_schema<database_name>.py
```

### 🔢 Automatic Roll Number Generation

Default databases can automatically generate sequential roll numbers.

Example:

```text
A0001
A0002
A0003
A0004
```

### 🔍 Record Search

Search for individual records using their primary key.

### 📋 View Records

Display records stored in a database.

### ✏️ Update Records

Update individual fields while preserving existing values.

Pressing **Enter** without entering a new value keeps the existing value.

### 🗑️ Delete Records

Delete an individual record using its primary key.

The delete operation works on a specific record rather than deleting the entire database.

---

## 💻 Installation & Usage

### Option 1 — Run from Source

#### 1. Clone the repository

```bash
git clone https://github.com/lyashwith/registrarY.git
```

#### 2. Navigate to the project directory

```bash
cd registrarY
```

#### 3. Run registrarY

If `registrarY.py` is located in the current directory:

```bash
python registrarY.py
```

If it is inside the `registrarY` directory:

```bash
python registrarY/registrarY.py
```

Make sure Python 3 is installed and available in your system PATH.

---

### Option 2 — Windows Executable

Pre-built Windows executables are available from the GitHub releases.

#### v1.35 Beta

[![Download v1.35 Beta](https://img.shields.io/badge/Download-v1.35_Beta-0078D4?style=flat\&logo=windows11\&logoColor=white)](https://github.com/lyashwith/registrarY/releases/download/1.35beta/registrarY.1.35beta.exe)

#### v1.3 Beta

[![Download v1.3 Beta](https://img.shields.io/badge/Download-v1.3_Beta-0078D4?style=flat\&logo=windows11\&logoColor=white)](https://github.com/lyashwith/registrarY/releases/download/v1.3beta/registrarY-1.3-beta.exe)

No Python installation is required when using the pre-built executable.

---

## 🧩 Custom Schema Format

Custom schemas use the following format:

```text
field_name;type
```

Multiple fields are separated using commas.

### Example

```text
name;str,age;int,percentage;float
```

This produces fields equivalent to:

```text
Name        → String
Age         → Integer
Percentage  → Float
```

The first field can also be used as the primary key depending on the database configuration.

---

## 🔄 Database Operations

registrarY follows a simple CRUD-style approach:

| Operation  | Description                                |
| ---------- | ------------------------------------------ |
| **Create** | Create a default database or custom schema |
| **Read**   | View and search records                    |
| **Update** | Modify existing record fields              |
| **Delete** | Remove a record using its primary key      |

This makes the project useful for learning the basic concepts behind database management systems.

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
  Add improved formatting, tables, and coloured terminal output.

* [ ] **Duplicate Key Protection**
  Warn users before overwriting an existing record.

* [ ] **Custom Primary Key Prompts**
  Replace hardcoded references to `"Roll Number"` with the configured primary key name.

* [ ] **Improved Database Management**
  Add additional operations for managing database files and records.

---

## 🐛 Known Issues & Limitations

### Schema File Dependency

Before adding data using a custom schema, the corresponding schema must first be created.

Option `(3) Add data` depends on the corresponding schema file existing:

```text
custom_schema<database_name>.py
```

---

### Data File Overwriting

Some operations involving default or custom entries may overwrite existing dataset files instead of appending records.

This behaviour may change in future versions.

---

### Invalid Data Type Input

Entering text when an `int` or `float` value is expected can currently raise an unhandled:

```text
ValueError
```

The application may not automatically re-prompt for valid input.

---

### Python File Storage

Database data is currently stored using `.py` files containing Python dictionary data.

The files must maintain valid Python dictionary syntax.

If a database file becomes corrupted or contains invalid syntax, the program may fail while reading it with:

```python
ast.literal_eval()
```

---

### Hardcoded `"Roll Number"` Prompts

Some search and viewing prompts explicitly reference:

```text
Roll Number
```

even when a database uses a custom primary key.

This is planned for improvement.

---

### Duplicate Primary Keys

If a primary key already exists, entering the same key may overwrite the existing record without displaying a confirmation warning.

---

### Strict Schema Formatting

Schema definitions must follow the required format:

```text
field_name;type
```

Multiple fields must be separated using commas.

Example:

```text
name;str,age;int,percentage;float
```

Incorrect formatting may result in parsing errors or unexpected behaviour.

---

### Entry Count Validation

In `create_default_database()`, non-numeric entry counts are handled.

However, entering:

```text
0
```

or a negative number may not currently re-prompt the user correctly before data collection.

---

## 🛠️ Project Structure

```text
registrarY/
│
├── registrarY.py
│   └── Main CLI application
│
├── database.py
│   └── Database-related functionality
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
├── LICENSE
│   └── Project license
│
└── README.md
    └── Project documentation
```

> Database and schema files may be generated dynamically when registrarY is used.

---

## 🎯 Project Goals

registrarY was created as a learning and hobby project for exploring concepts such as:

* Python programming
* Dictionaries and nested data structures
* File handling
* Dynamic schemas
* Data validation
* CRUD operations
* Command-line interfaces
* Local data persistence
* Basic database-management concepts

The project is intended primarily for learning and experimentation rather than use as a production database system.

---

## 🔐 Data & Security

registrarY currently uses local files for storing database information.

Because the current storage system is based on Python-readable files, these files should be treated as application data rather than a secure database format.

Future versions may introduce optional encryption and a more dedicated storage format.

---

## 📄 License

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

## 👤 Author

Developed by **Yashwith L.**

<a href="https://github.com/lyashwith">
  <img src="https://avatars.githubusercontent.com/u/313887780?s=100" alt="GitHub Logo" width="50">
</a>

---

## ⭐ Support

If you find registrarY useful or interesting, consider giving the repository a ⭐ on GitHub.

**Repository:**
https://github.com/lyashwith/registrarY
