# registrarY

[![Download Executable](https://img.shields.io/badge/Download_Windows_.EXE-0078D4?style=for-the-badge&logo=windows11&logoColor=white)](https://github.com/lyashwith/registrarY/releases/download/v1.2Beta/registrarY.exe)
[![Download Source Code](https://img.shields.io/badge/Download_Source_Code_.ZIP-24292E?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lyashwith/registrarY/archive/refs/tags/v1.2Beta.zip)

A lightweight Python command-line interface (CLI) database application designed to generate, store, search, and update student records using structured, sequential roll numbers.

---

## 🚀 Features

* **Interactive Navigation Menu:** Seamlessly switch between creating entries, viewing records, searching, updating details, help, and exiting.
* **Automated Roll Number Generation:** Generates sequential roll numbers (e.g., `A0001`, `A0002`) based on entry index.
* **Safe Local Data Storage:** Saves data directly as dictionary literals in `database.py` and parses them back safely using Python's `ast.literal_eval`.
* **Record Display & Search:** Retrieve specific student details by roll number or view the complete database at once.
* **In-Place Updates:** Update specific fields (Name, DOB, Parents' names) while preserving unchanged values by pressing Enter.

---

## 🐛 Known Issues & Limitations (v1.2 Beta)

* **Missing File Handling (`FileNotFoundError`):** Calling **View**, **Search**, or **Update** before running **Create default** crashes the program if `database.py` does not exist yet.
* **Overwriting Data:** Option `(1) Create default` completely overwrites `database.py` instead of appending new student records to existing ones.
* **Unvalidated Input:** Non-numeric input for the entry count will trigger a `ValueError` crash instead of prompting the user again.
* **Redundant Loop Condition:** The check `if num_entry <= 0:` inside the `for` loop in `create_default_database()` is redundant because the outer `else` block already ensures `num_entry > 0`.
* **Typos in CLI Messages:** Minor typos in user strings (e.g., `"not found in tha database"` instead of `"the database"`).

---

## 🛠️ Project Structure

```text
registrarY/
├── registrarY.py      # Main CLI application script
├── database.py        # Local data storage file (dictionary literal)
└── README.md          # Project documentation
https://github.com/lyashwith/registrarY
