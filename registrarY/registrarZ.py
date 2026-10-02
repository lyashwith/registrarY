#AI code
#not human

"""import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from ast import literal_eval
import os

class RegistrarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Registrar Database Manager")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.database_name = None
        self.database = {}
        
        # Style configuration
        self.root.configure(bg="#f0f0f0")
        style = ttk.Style()
        style.theme_use('clam')
        
        self.setup_login_screen()
    
    def setup_login_screen(self):
        """Setup the database selection/creation screen"""
        self.clear_window()
        
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True)
        
        title = ttk.Label(frame, text="Registrar Database Manager", 
                         font=("Arial", 20, "bold"))
        title.pack(pady=20)
        
        ttk.Label(frame, text="Enter Database Name:", 
                 font=("Arial", 12)).pack(pady=10)
        
        self.db_entry = ttk.Entry(frame, width=30, font=("Arial", 12))
        self.db_entry.pack(pady=10)
        
        button_frame = ttk.Frame(frame)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="Load Database", 
                  command=self.load_database_name).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Create New", 
                  command=self.create_new_database).pack(side=tk.LEFT, padx=5)
    
    def load_database_name(self):
        """Load an existing database"""
        db_name = self.db_entry.get().strip()
        if not db_name:
            messagebox.showerror("Error", "Please enter a database name")
            return
        
        try:
            with open(f"{db_name}.py", "r") as file:
                file.read()
            self.database_name = db_name
            self.setup_main_menu()
        except FileNotFoundError:
            messagebox.showerror("Error", 
                               f"Database '{db_name}' not found.\nCreate a new database first.")
    
    def create_new_database(self):
        """Create a new database"""
        db_name = self.db_entry.get().strip()
        if not db_name:
            messagebox.showerror("Error", "Please enter a database name")
            return
        
        if os.path.exists(f"{db_name}.py"):
            messagebox.showerror("Error", f"Database '{db_name}' already exists")
            return
        
        self.database_name = db_name
        self.database = {}
        self.setup_main_menu()
    
    def setup_main_menu(self):
        """Setup the main menu screen"""
        self.clear_window()
        
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(expand=True, fill=tk.BOTH)
        
        title = ttk.Label(frame, text=f"Database: {self.database_name}", 
                         font=("Arial", 18, "bold"))
        title.pack(pady=20)
        
        menu_frame = ttk.LabelFrame(frame, text="Options", padding="20")
        menu_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        buttons = [
            ("1. Create Default Database", self.create_default),
            ("2. Create Custom Schema", self.create_custom_schema),
            ("3. Add Data", self.add_custom_data),
            ("4. View All", self.view_all),
            ("5. Search", self.search_database),
            ("6. Update", self.update_database),
            ("7. Help", self.show_help),
            ("8. Exit", self.root.quit)
        ]
        
        for btn_text, cmd in buttons:
            ttk.Button(menu_frame, text=btn_text, command=cmd, 
                      width=30).pack(pady=5, fill=tk.X)
    
    def create_default(self):
        """Create default database with roll numbers"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Create Default Database")
        dialog.geometry("400x200")
        
        ttk.Label(dialog, text="Number of Entries:", 
                 font=("Arial", 12)).pack(pady=10)
        num_entry = ttk.Entry(dialog, width=20, font=("Arial", 12))
        num_entry.pack(pady=5)
        
        def confirm():
            try:
                num = int(num_entry.get())
                if num <= 0:
                    messagebox.showerror("Error", "Enter a positive number")
                    return
                self.input_default_data(num, dialog)
            except ValueError:
                messagebox.showerror("Error", "Enter a valid number")
        
        ttk.Button(dialog, text="Continue", command=confirm).pack(pady=10)
    
    def input_default_data(self, num_entries, parent):
        """Input data for default database"""
        parent.destroy()
        
        data_window = tk.Toplevel(self.root)
        data_window.title("Enter Data")
        data_window.geometry("500x600")
        
        # Canvas with scrollbar for multiple entries
        canvas = tk.Canvas(data_window)
        scrollbar = ttk.Scrollbar(data_window, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        entries_list = []
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        for i in range(num_entries):
            frame = ttk.LabelFrame(scrollable_frame, text=f"Entry {i+1}", padding="10")
            frame.pack(fill=tk.X, padx=5, pady=5)
            
            fields = {}
            for label_text in ["Name:", "Date of Birth (DD-MM-YYYY):", 
                             "Father's Name:", "Mother's Name:"]:
                ttk.Label(frame, text=label_text).pack()
                entry = ttk.Entry(frame, width=40)
                entry.pack(pady=5)
                fields[label_text] = entry
            
            entries_list.append(fields)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        def save_data():
            self.database = {}
            for i, fields in enumerate(entries_list):
                name = fields["Name:"].get()
                dob = fields["Date of Birth (DD-MM-YYYY):"].get()
                fname = fields["Father's Name:"].get()
                mname = fields["Mother's Name:"].get()
                
                if not all([name, dob, fname, mname]):
                    messagebox.showerror("Error", f"Please fill all fields for Entry {i+1}")
                    return
                
                letter_index = i // 1000
                number = (i % 1000) + 1
                roll_no = alphabet[letter_index] + f"{number:04d}"
                
                self.database[roll_no] = {
                    "Name": name,
                    "date_of_birth": dob,
                    "father_name": fname,
                    "mother_name": mname
                }
            
            self.save_database()
            data_window.destroy()
            messagebox.showinfo("Success", "Database created successfully!")
            self.setup_main_menu()
        
        ttk.Button(data_window, text="Save Database", command=save_data).pack(pady=10)
    
    def create_custom_schema(self):
        """Create custom schema"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Create Custom Schema")
        dialog.geometry("600x300")
        
        ttk.Label(dialog, text="Primary Key Field:", 
                 font=("Arial", 12)).pack(pady=10)
        pk_entry = ttk.Entry(dialog, width=40, font=("Arial", 12))
        pk_entry.pack(pady=5)
        
        ttk.Label(dialog, text="Fields (format: fieldname;datatype, ...)", 
                 font=("Arial", 10)).pack(pady=10)
        ttk.Label(dialog, text="Example: name;str,age;int,salary;float", 
                 font=("Arial", 9), foreground="gray").pack()
        
        fields_entry = tk.Text(dialog, height=5, width=60, font=("Arial", 10))
        fields_entry.pack(pady=10, padx=10)
        
        def create():
            pk = pk_entry.get().strip()
            fields_text = fields_entry.get("1.0", tk.END).strip()
            
            if not pk or not fields_text:
                messagebox.showerror("Error", "Please fill all fields")
                return
            
            schema = {pk: {}}
            try:
                for field in fields_text.split(","):
                    field_name, data_type = field.split(";")
                    schema[pk][field_name.strip()] = data_type.strip()
                
                with open(f"custom_schema{self.database_name}.py", "w") as file:
                    file.write(str(schema))
                
                dialog.destroy()
                messagebox.showinfo("Success", "Custom schema created successfully!")
                self.setup_main_menu()
            except Exception as e:
                messagebox.showerror("Error", f"Invalid format: {str(e)}")
        
        ttk.Button(dialog, text="Create Schema", command=create).pack(pady=10)
    
    def add_custom_data(self):
        """Add data using custom schema"""
        try:
            with open(f"custom_schema{self.database_name}.py", "r") as file:
                content = file.read()
            schema = literal_eval(content)
        except FileNotFoundError:
            messagebox.showerror("Error", "Custom schema not found. Create one first.")
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Data")
        dialog.geometry("400x200")
        
        ttk.Label(dialog, text="Number of Entries to Add:", 
                 font=("Arial", 12)).pack(pady=10)
        num_entry = ttk.Entry(dialog, width=20, font=("Arial", 12))
        num_entry.pack(pady=5)
        
        def confirm():
            try:
                num = int(num_entry.get())
                if num <= 0:
                    messagebox.showerror("Error", "Enter a positive number")
                    return
                self.input_custom_data(num, schema, dialog)
            except ValueError:
                messagebox.showerror("Error", "Enter a valid number")
        
        ttk.Button(dialog, text="Continue", command=confirm).pack(pady=10)
    
    def input_custom_data(self, num_entries, schema, parent):
        """Input custom data"""
        parent.destroy()
        
        data_window = tk.Toplevel(self.root)
        data_window.title("Enter Data")
        data_window.geometry("600x700")
        
        canvas = tk.Canvas(data_window)
        scrollbar = ttk.Scrollbar(data_window, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        entries_list = []
        pk_name = list(schema.keys())[0]
        fields_info = schema[pk_name]
        
        for i in range(num_entries):
            frame = ttk.LabelFrame(scrollable_frame, text=f"Entry {i+1}", padding="10")
            frame.pack(fill=tk.X, padx=5, pady=5)
            
            fields = {}
            ttk.Label(frame, text=f"{pk_name}:").pack()
            entry = ttk.Entry(frame, width=40)
            entry.pack(pady=5)
            fields[pk_name] = entry
            
            for field_name, data_type in fields_info.items():
                ttk.Label(frame, text=f"{field_name} ({data_type}):").pack()
                entry = ttk.Entry(frame, width=40)
                entry.pack(pady=5)
                fields[field_name] = entry
            
            entries_list.append(fields)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        def save_data():
            self.database = {}
            try:
                for i, fields in enumerate(entries_list):
                    pk_value = fields[pk_name].get().strip()
                    
                    if not pk_value:
                        messagebox.showerror("Error", f"Please fill {pk_name} for Entry {i+1}")
                        return
                    
                    self.database[pk_value] = {}
                    
                    for field_name, data_type in fields_info.items():
                        value_str = fields[field_name].get().strip()
                        
                        if not value_str:
                            messagebox.showerror("Error", 
                                               f"Please fill {field_name} for Entry {i+1}")
                            return
                        
                        if data_type == "int":
                            self.database[pk_value][field_name] = int(value_str)
                        elif data_type == "float":
                            self.database[pk_value][field_name] = float(value_str)
                        else:
                            self.database[pk_value][field_name] = value_str
                
                self.save_database()
                data_window.destroy()
                messagebox.showinfo("Success", "Data added successfully!")
                self.setup_main_menu()
            except ValueError as e:
                messagebox.showerror("Error", f"Invalid data type: {str(e)}")
        
        ttk.Button(data_window, text="Save Data", command=save_data).pack(pady=10)
    
    def view_all(self):
        """View all records"""
        try:
            self.database = self.load_database()
        except FileNotFoundError:
            messagebox.showerror("Error", "Database file not found")
            return
        
        view_window = tk.Toplevel(self.root)
        view_window.title("View All Records")
        view_window.geometry("700x600")
        
        if not self.database:
            ttk.Label(view_window, text="Database is empty", 
                     font=("Arial", 12)).pack(pady=20)
            return
        
        canvas = tk.Canvas(view_window)
        scrollbar = ttk.Scrollbar(view_window, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        for primary_key, details in self.database.items():
            frame = ttk.LabelFrame(scrollable_frame, text=f"ID: {primary_key}", 
                                  padding="10")
            frame.pack(fill=tk.X, padx=5, pady=5)
            
            for field_name, value in details.items():
                ttk.Label(frame, text=f"{field_name}: {value}").pack(anchor=tk.W)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def search_database(self):
        """Search for a record"""
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Record")
        search_window.geometry("400x200")
        
        ttk.Label(search_window, text="Enter Primary Key to Search:", 
                 font=("Arial", 12)).pack(pady=10)
        search_entry = ttk.Entry(search_window, width=40, font=("Arial", 12))
        search_entry.pack(pady=10)
        
        def search():
            try:
                self.database = self.load_database()
            except FileNotFoundError:
                messagebox.showerror("Error", "Database file not found")
                return
            
            pk = search_entry.get().strip()
            if not pk:
                messagebox.showerror("Error", "Please enter a primary key")
                return
            
            if pk in self.database:
                result_window = tk.Toplevel(search_window)
                result_window.title(f"Search Result - {pk}")
                result_window.geometry("400x300")
                
                frame = ttk.LabelFrame(result_window, text=f"ID: {pk}", padding="20")
                frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
                
                for field_name, value in self.database[pk].items():
                    ttk.Label(frame, text=f"{field_name}: {value}", 
                             font=("Arial", 11)).pack(anchor=tk.W, pady=5)
            else:
                messagebox.showerror("Not Found", f"Primary key '{pk}' not found")
        
        ttk.Button(search_window, text="Search", command=search).pack(pady=10)
    
    def update_database(self):
        """Update a record"""
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Record")
        update_window.geometry("400x200")
        
        ttk.Label(update_window, text="Enter Primary Key to Update:", 
                 font=("Arial", 12)).pack(pady=10)
        pk_entry = ttk.Entry(update_window, width=40, font=("Arial", 12))
        pk_entry.pack(pady=10)
        
        def find_record():
            try:
                self.database = self.load_database()
            except FileNotFoundError:
                messagebox.showerror("Error", "Database file not found")
                return
            
            pk = pk_entry.get().strip()
            if not pk:
                messagebox.showerror("Error", "Please enter a primary key")
                return
            
            if pk not in self.database:
                messagebox.showerror("Not Found", f"Primary key '{pk}' not found")
                return
            
            update_window.destroy()
            self.edit_record(pk)
        
        ttk.Button(update_window, text="Find", command=find_record).pack(pady=10)
    
    def edit_record(self, pk):
        """Edit a specific record"""
        edit_window = tk.Toplevel(self.root)
        edit_window.title(f"Edit Record - {pk}")
        edit_window.geometry("500x400")
        
        frame = ttk.LabelFrame(edit_window, text=f"ID: {pk}", padding="20")
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        entries = {}
        for field_name, value in self.database[pk].items():
            ttk.Label(frame, text=f"{field_name}:", font=("Arial", 11)).pack()
            entry = ttk.Entry(frame, width=40, font=("Arial", 11))
            entry.insert(0, str(value))
            entry.pack(pady=5)
            entries[field_name] = entry
        
        def save_changes():
            for field_name, entry in entries.items():
                new_value = entry.get()
                if new_value:
                    self.database[pk][field_name] = new_value
            
            self.save_database()
            edit_window.destroy()
            messagebox.showinfo("Success", "Record updated successfully!")
            self.setup_main_menu()
        
        ttk.Button(edit_window, text="Save Changes", command=save_changes).pack(pady=10)
    
    def show_help(self):
        """Show help dialog"""
        help_window = tk.Toplevel(self.root)
        help_window.title("Help")
        help_window.geometry("700x500")
        
        help_text = """
REGISTRAR DATABASE MANAGER - HELP

1. CREATE DEFAULT DATABASE
   - Automatically generates roll numbers (A0001, A0002, etc.)
   - Stores: Name, Date of Birth, Father's Name, Mother's Name

2. CREATE CUSTOM SCHEMA
   - Define custom fields with data types
   - Format: fieldname;datatype (e.g., name;str,age;int)
   - Supported types: str, int, float

3. ADD DATA
   - Insert new records into the database
   - Must create custom schema first for custom databases

4. VIEW ALL
   - Display all records currently in the database
   - Shows all fields for each record

5. SEARCH
   - Look up a record by its Primary Key
   - Returns all details for that record

6. UPDATE
   - Modify an existing record
   - Leave field empty to keep original value
   - Or enter new value to update

7. HELP
   - Display this help menu

8. EXIT
   - Close the application
        """
        
        text_widget = tk.Text(help_window, height=25, width=80, 
                             font=("Courier", 10), wrap=tk.WORD)
        text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        text_widget.insert("1.0", help_text)
        text_widget.config(state=tk.DISABLED)
    
    def save_database(self):
        """Save database to file"""
        with open(f"{self.database_name}.py", "w") as file:
            file.write(str(self.database))
    
    def load_database(self):
        """Load database from file"""
        with open(f"{self.database_name}.py", "r") as file:
            content = file.read()
        return literal_eval(content.strip())
    
    def clear_window(self):
        """Clear all widgets from window"""
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrarGUI(root)
    root.mainloop()"""
