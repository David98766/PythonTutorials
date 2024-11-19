import sqlite3

# Connect to the database
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# Update Charlie's grade to "B"
cursor.execute('''
UPDATE students SET grade = ? WHERE name = ?;
''', ('B', 'Charlie'))

# Retrieve and print the updated record
cursor.execute('SELECT * FROM students WHERE name = ?', ('Charlie',))
row = cursor.fetchone()
print(row)

# Commit and close
connection.commit()
connection.close()