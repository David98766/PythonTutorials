import sqlite3

# Connect to the database
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# Insert data
students = [
    ('Alice', 20, 'A'),
    ('Bob', 22, 'B'),
    ('Charlie', 19, 'C')
]

# order matters if array is not in the same order as the insert command it will be wrong
cursor.executemany('''
INSERT INTO students (name, age, grade) VALUES (?, ?, ?);
''', students)

# Commit and close
connection.commit()
connection.close()