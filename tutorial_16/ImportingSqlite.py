# import sqlite3
import sqlite3

# Create connection variable to hold reference the database
connection = sqlite3.connect('example.db')

# cursor object to perform database operations
cursor = connection.cursor()

# Closing the connection
connection.commit()

