import sqlite3

# Step 1: Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect("user.db")  # This will create a file named "my_database.db" in the current directory

# Step 2: Create a cursor object to interact with the database
cursor = connection.cursor()

# Step 3: Write a SQL statement to create a table
# For example, let's create a "users" table with columns: id, first_name, last_name, email, and password
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  first_name TEXT NOT NULL,
                  last_name TEXT NOT NULL,
                  email TEXT UNIQUE NOT NULL,
                  password TEXT NOT NULL
                  )""")

# Step 4: Commit the changes to save them to the database
connection.commit()

# Step 5: Close the connection to the database
connection.close()

print("Database and table created successfully!")