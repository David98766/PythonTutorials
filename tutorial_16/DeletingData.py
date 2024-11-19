import sqlite3

# Connect to the database
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# Delete Bob's record
cursor.execute('DELETE FROM students WHERE name = ?', ('Bob',))

# Retrieve and print all remaining records
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Commit and close
connection.commit()
connection.close()
