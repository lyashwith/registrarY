# registrarY

A lightweight Python command-line interface (CLI) database application designed to generate, store, search, and update student records using structured, sequential roll numbers.

## 🚀 Features
* **Interactive Navigation Menu:** Seamlessly switch between creating entries, viewing all records, searching, updating details, viewing help, and exiting using a continuous loop.
* **Automated Roll Number Generation:** Automatically creates formatted sequential roll numbers (e.g., A0001, A0002, A0003) based on entry index using modulo and division arithmetic.
* **Record Display & Search:** Retrieve specific student details by searching roll numbers or view all stored records at once.
* **Record Update:** Update existing student details (Name, DOB, Father's Name, Mother's Name) while keeping original values for unchanged fields.
* **Persistent Local Storage:** Automatically saves database records locally in `database.py` across sessions.

## 📌 Current Limitations & Future Roadmap
* ⚠️ **No Delete Support:** Records cannot be deleted once added.
* 🔮 **Planned Feature:** Add a record deletion command to enable full CRUD management.

## 🛠️ Project Structure
```text
registrarY/
├── registrarY.py      # Main CLI application script
├── database.py        # Local database storage file
└── README.md          # Project documentation
