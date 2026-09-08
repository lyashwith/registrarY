# registrarY

[![Download v1.3-beta Executable](https://img.shields.io/badge/registrarY.exe_(v1.3beta)-Download-0078D4?style=flat&size=large&logo=windows11&logoColor=white)](https://github.com/lyashwith/registrarY/releases/download/v1.3beta/registrarY-1.3-beta.exe)
[![Download v1.2.0.1beta Executable](https://img.shields.io/badge/registrarY.exe_(v1.2.0.1beta)-Download-0078D4?style=flat&size=large&logo=windows11&logoColor=white)](https://github.com/lyashwith/registrarY/releases/download/v1.2.0.1beta/registrarY.v1.2.0.1beta.exe)
[![GitHub Repository](https://img.shields.io/badge/GitHub-registrarY_Repository-181717?style=flat&size=large&logo=github&logoColor=white)](https://github.com/lyashwith/registrarY)
[![Download Source Code](https://img.shields.io/badge/Download-Source_Code_.ZIP_(v1.3beta)-24292E?style=flat&size=large&logo=github&logoColor=white)](https://github.com/lyashwith/registrarY/archive/refs/tags/v1.3beta.zip)

A lightweight Python command-line interface (CLI) database application designed to generate, store, search, and update student records using custom schemas or structured sequential roll numbers.

---

## 🚀 Features

- **Interactive Navigation Menu:** Seamlessly switch between creating entries, defining custom schemas, viewing records, searching, updating details, help, and exiting.
- **Custom Schema Creation:** Define dynamic primary key names and field attributes (`str`, `int`, `float`) saved independently to custom schema files (`custom_schema<db_name>.py`).
- **Custom Data Entry:** Add entries matching your defined custom schemas with data type handling.
- **Automated Roll Number Generation:** Generates sequential roll numbers (e.g., `A0001`, `A0002`) for default database setups.
- **Record Display & Search:** Retrieve specific records by primary key or view all formatted records line-by-line.
- **In-Place Updates:** Modify specific attributes while preserving unchanged values by pressing Enter.

---

## 🗺️ Roadmap & Upcoming Features

- **Text File Data Persistence:** Transition from stringified `.py` data files to standard `.txt` text files for safer storage and separation of data from code execution.
- **Input Validation & Exception Handling:** Prevent crashes on malformed user inputs during menu choices or numeric entries.
- **Database Encryption:** Add encryption capabilities (such as `cryptography.fernet`) to secure local database files.
- **Enhanced CLI Styling:** Integrate terminal formatting libraries (e.g., `rich`) for styled tables and colored output.

---

## 🐛 Known Issues & Limitations (v1.3 Beta)

- **Schema File Dependency:** Creating custom entries requires a corresponding `custom_schema<db_name>.py` file to exist first.
- **Overwriting Data File:** Creating new custom entries overwrites existing dataset files rather than appending to them.
