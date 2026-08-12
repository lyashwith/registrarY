# registrarY

A lightweight Python command-line interface (CLI) database application designed to generate, store, and search student records using structured, sequential roll numbers.

---

## 🚀 Features

- **Interactive Navigation Menu:** Seamlessly switch between creating entries, searching records, and exiting using a continuous loop.
- **Automated Roll Number Generation:** Automatically creates formatted sequential roll numbers (e.g., `A0001`, `A0002`, `A0003`) based on entry index.
- **Record Search:** Quick and clean lookup system to retrieve student details by roll number.
- **Persistent Local Storage:** Saves database records locally in `database.py` for retrieval across sessions.

---

## 🛠️ Project Structure

```text
registrarY/
├── registrarY.py      # Main CLI application script
├── database.py        # Local database storage file
└── README.md          # Project documentation
