import sqlite3

class CRUDFinal:
    def __init__(self):
        self.connection = sqlite3.connect('example.db')
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

    def update(self, name, grade):
        self.cursor.execute('''
        UPDATE students SET grade = ? WHERE name = ?;
        ''', (grade, name))
        self.cursor.execute('SELECT * FROM students WHERE name = ?', (name,))
        row = self.cursor.fetchone()
        print(row)
        self.connection.commit()

    def delete(self, name):
        self.cursor.execute('DELETE FROM students WHERE name = ?', (name,))
        self.cursor.execute('SELECT * FROM students')
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
        self.connection.commit()

    def retrieve(self):
        self.cursor.execute('SELECT * FROM students')
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def retrieve_by_age(self, age):
        self.cursor.execute('SELECT * FROM students WHERE age > ?', (age,))
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

# Instantiate the class
crudFinal = CRUDFinal()

# Test the methods
students = [
    ('Aoife', 20, 'A'),
    ('James', 22, 'A'),
    ('Jim', 19, 'B')
]

crudFinal.insert(students)
print("All Students:")
crudFinal.retrieve()

print("\nStudents older than 20:")
crudFinal.retrieve_by_age(20)

print("\nUpdating David's grade to 'B':")
crudFinal.update('David', 'B')

print("\nDeleting David:")
crudFinal.delete('David')

print("\nFinal list of students:")
crudFinal.retrieve()