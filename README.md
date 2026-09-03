# registrarY

[![Download for Windows](https://img.shields.io/badge/Download_for_Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/lyashwith/registrarY/releases/download/v1.2Beta/registrarY.exe)

A lightweight Python command-line interface (CLI) database application designed to generate, store, search, and update student records using structured, sequential roll numbers.

## 🚀 Features

* **Interactive Navigation Menu:** Seamlessly switch between creating entries, viewing records, searching, updating details, help, and exiting.
* **Automated Roll Number Generation:** Generates sequential roll numbers (e.g., `A0001`, `A0002`) based on entry index.
* **Safe Local Data Storage:** Saves data directly as dictionary literals in `database.py` and parses them back safely using Python's `ast.literal_eval`.
* **Record Display & Search:** Retrieve specific student details by roll number or view the complete database at once.
* **In-Place Updates:** Update specific fields (Name, DOB, Parents' names) while preserving unchanged values by pressing Enter.

---

## 🛠️ Project Structure

```text
registrarY/
├── registrarY.py      # Main CLI application script
├── database.py        # Local data storage file (dictionary literal)
└── README.md          # Project documentation
