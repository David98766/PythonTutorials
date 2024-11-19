import sqlite3

# Connect to the database
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# Retrieve students with age > 20
age_threshold = 20
cursor.execute('SELECT * FROM students WHERE age > ?', (age_threshold,))
rows = cursor.fetchall()

# Print each record
for row in rows:
    print(row)

# Close the connection
connection.close()