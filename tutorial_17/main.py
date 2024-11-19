import tkinter as tk
from tkinter import messagebox
import sqlite3

class CRUDFinal:
    def __init__(self):
        self.connection = sqlite3.connect('students.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            grade TEXT
        );
        ''')

    def __del__(self):
        self.connection.close()

    def insert(self, students):
        self.cursor.executemany('''
        INSERT INTO students (name, age, grade) VALUES (?, ?, ?);
        ''', students)
        self.connection.commit()

    def update(self, student_id, grade):
        self.cursor.execute('''
        UPDATE students SET grade = ? WHERE id = ?;
        ''', (grade, student_id))
        self.connection.commit()

    def delete(self, student_id):
        self.cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        self.connection.commit()

    def retrieve(self):
        self.cursor.execute('SELECT * FROM students')
        return self.cursor.fetchall()

    def retrieve_by_age(self, age):
        self.cursor.execute('SELECT * FROM students WHERE age >= ?', (age,))
        return self.cursor.fetchall()

    def retrieve_by_id(self, student_id):
        self.cursor.execute('''
        SELECT * FROM students WHERE id = ?
        ''', (student_id,))


class StudentApp:
    def __init__(self, root, CRUDFinal):
        self.root = root
        self.CRUDFinal = CRUDFinal
        self.root.title("Student Management")

        # UI Elements

        # We are declaring the listbox first because if we declare it after the buttons it is likely to cause an error (the button's command methods call the listbox, when it may not yet be instantiated)
        # Listbox for displaying students
        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
        # Bind selection event (so we can populate entries of selected index)
        self.listbox.bind('<<ListboxSelect>>', self.populate_entry_boxes)

        self.name_label = tk.Label(root, text="Name")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.age_label = tk.Label(root, text="Age")
        self.age_label.grid(row=1, column=0, padx=10, pady=5)
        self.age_entry = tk.Entry(root)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5)

        self.grade_label = tk.Label(root, text="Grade")
        self.grade_label.grid(row=2, column=0, padx=10, pady=5)
        self.grade_entry = tk.Entry(root)
        self.grade_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.add_button.grid(row=3, column=0, padx=10, pady=5)

        self.update_button = tk.Button(root, text="Update Grade", command=self.update_student)
        self.update_button.grid(row=3, column=1, padx=10, pady=5)

        self.delete_button = tk.Button(root, text="Delete Student", command=self.delete_student)
        self.delete_button.grid(row=4, column=0, padx=10, pady=5)

        # This button essentially replaces the filter results with the entire db
        self.show_all = tk.Button(root, text="Show All", command=self.show_students)
        self.show_all.grid(row=4, column=1, padx=10, pady=5)

        self.age_filter_label = tk.Label(root, text="Filter by Age >=")
        self.age_filter_label.grid(row=5, column=0, padx=10, pady=5)
        self.age_filter_entry = tk.Entry(root)
        self.age_filter_entry.grid(row=5, column=1, padx=10, pady=5)
        self.filter_button = tk.Button(root, text="Filter", command=self.filter_by_age)
        self.filter_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        self.show_students() # Populate listbox with data


    def clear_entries(self):
        # Clears all input fields
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)
        self.age_filter_entry.delete(0, tk.END)

    def add_student(self):
        # Get the values from the input fields
        name = self.name_entry.get()
        age = self.age_entry.get()
        grade = self.grade_entry.get()

        # Check if all fields have values
        if name and age and grade:
            try:
                # we are calling the insert method from above
                # Insert the new student into the database (we are inserting the students tuple)
                self.CRUDFinal.insert([(name, int(age), grade)])
                # Show a success message
                messagebox.showinfo("Success", "Student added successfully.")
                # Refresh the student list
                self.show_students()
            except Exception as e:
                # Show an error message if the operation fails
                messagebox.showerror("Error", f"Failed to add student: {e}")
        else:
            # Show a warning if any field is empty
            messagebox.showwarning("Input Error", "Please fill all fields.")

        # Clear all input fields after the operation
        self.clear_entries()

    def update_student(self):
        # Get the selected student from the listbox
        selected_index = self.listbox.curselection()
        if selected_index:
            # Retrieve the selected item's ID (first part of the listbox entry)
            selected_item = self.listbox.get(selected_index)
            student_id = selected_item.split(":")[0]  # Extract the ID (before the colon)

            # Get the new grade from the input field
            grade = self.grade_entry.get()
            if grade:  # Check if the grade field is filled
                try:
                    # Update the student's grade in the database using the ID
                    self.CRUDFinal.update(student_id, grade)
                    # Show a success message
                    messagebox.showinfo("Success", "Student grade updated successfully.")
                    # Refresh the student list
                    self.show_students()
                except Exception as e:
                    # Show an error message if the operation fails
                    messagebox.showerror("Error", f"Failed to update student: {e}")
            else:
                # Show a warning if the grade field is empty
                messagebox.showwarning("Input Error", "Please provide a new grade.")
        else:
            # Show a warning if no student is selected
            messagebox.showwarning("Selection Error", "Please select a student to update.")

        # Clear all input fields after the operation
        self.clear_entries()

    def delete_student(self):
        # Get the selected student from the listbox
        selected_index = self.listbox.curselection()
        if not selected_index:  # Check if an item is selected
            messagebox.showwarning("Selection Error", "Please select a student to delete.")
            return

        # Retrieve the selected item's ID (first part of the listbox entry)
        selected_item = self.listbox.get(selected_index)
        selected_id = selected_item.split(":")[0]  # Extract the ID

        try:
            # Convert the ID to an integer
            selected_id = int(selected_id)
            # Delete the selected student from the database
            self.CRUDFinal.delete(selected_id)
            # Show a success message
            messagebox.showinfo("Success", "Student deleted successfully.")
            # Refresh the student list
            self.show_students()
        except Exception as e:
            # Show an error message if the operation fails
            messagebox.showerror("Error", f"Failed to delete student: {e}")

        # Refresh the student list after the operation
        self.show_students()

    def show_students(self):
        # Clear the listbox
        self.listbox.delete(0, tk.END)

        try:
            # Retrieve all students from the database
            students = self.CRUDFinal.retrieve()
            # Insert each student into the listbox
            # instead of using a list as we usually do, we are inserting formatted strings (f strings) into the listbox
            for student in students:
                self.listbox.insert(tk.END, f"{student[0]}: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
        except Exception as e:
            # Show an error message if the operation fails
            messagebox.showerror("Error", f"Failed to retrieve students: {e}")

        # Clear all input fields after refreshing the list
        self.clear_entries()

    def filter_by_age(self):
        # Get the age value from the filter input field
        age = self.age_filter_entry.get()
        if age:  # Check if the age field is filled
            try:
                # Retrieve students older than the given age
                students = self.CRUDFinal.retrieve_by_age(int(age))
                # Clear the listbox
                self.listbox.delete(0, tk.END)
                # Insert the filtered students into the listbox
                for student in students:
                    self.listbox.insert(tk.END, f"{student[0]}: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
            except Exception as e:
                # Show an error message if the operation fails
                messagebox.showerror("Error", f"Failed to filter students: {e}")
        else:
            # Show a warning if the age field is empty
            messagebox.showwarning("Input Error", "Please enter an age.")

    # Populates the entry boxes with the details of the selected student.
    def populate_entry_boxes(self, event):
        selected_index = self.listbox.curselection()  # Get the index of the selected item
        if selected_index:
            # Retrieve the selected item (formatted as "ID: Name, Age: X, Grade: Y")
            selected_item = self.listbox.get(selected_index)

            # Parse the string to extract the details
            parts = selected_item.split(": ", 1)  # Split by ": " to separate ID from the rest
            student_id = parts[0]  # Extract ID
            rest = parts[1]  # Extract the remaining details ("Name, Age: X, Grade: Y")

            name_part, age_part, grade_part = rest.split(", ")  # Split by ", " to separate fields
            name = name_part.strip()  # Extract the name
            age = age_part.split(": ")[1].strip()  # Extract the age (after "Age: ")
            grade = grade_part.split(": ")[1].strip()  # Extract the grade (after "Grade: ")

            # Populate the entry boxes
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)

            self.age_entry.delete(0, tk.END)
            self.age_entry.insert(0, age)

            self.grade_entry.delete(0, tk.END)
            self.grade_entry.insert(0, grade)


# Main Function
if __name__ == "__main__":
    root = tk.Tk()
    CRUDFinal = CRUDFinal()
    app = StudentApp(root, CRUDFinal)
    root.mainloop()
