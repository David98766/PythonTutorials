# import sqlite3
import sqlite3

# Create connection variable to hold reference the database
connection = sqlite3.connect('example.db')

# cursor object to perform database operations
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    grade TEXT
);
''')

# Commit change to the database and close connection
connection.commit()
connection.close()

