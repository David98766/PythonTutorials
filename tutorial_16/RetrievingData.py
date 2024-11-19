import sqlite3

# Connect to the database
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# Retrieve data
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

# Print each record
for row in rows:
    print(row)

# Close the connection
connection.close()