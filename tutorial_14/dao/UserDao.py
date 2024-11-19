import sqlite3
from tutorial_14.model.User import User



class UserDao:
    def __init__(self):
        # Creating the connection to the "user.db" SQLite database when a UserDao object is created
        self.connection = sqlite3.connect("user.db")
        self.cursor = self.connection.cursor()
        # Creating the "user" table if it doesn't already exist
        # The table has columns: id (auto-incremented primary key), firstName, lastName, email (unique), and password
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS user (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  firstName TEXT,
                  lastName TEXT,
                  email TEXT UNIQUE,
                  password TEXT
                  )""")
        self.connection.commit()  # Commit the table creation to the database

    # Destructor method to close the database connection when the UserDao object is deleted or goes out of scope
    def __del__(self):
        self.connection.close()

    def addUser(self, user):
        # Using a "with" statement to open a new database connection that will be automatically closed after use
        with sqlite3.connect("user.db") as connection:
            cursor = connection.cursor()
            # Check if the email already exists in the database
            cursor.execute("SELECT * FROM user WHERE email = ?", (user.email,))
            existing_user = cursor.fetchone()  # Fetch one result, if any

            if existing_user:
                # Raise a ValueError if the email is already in use
                raise ValueError("A user with this email already exists.")

            # If the email is not in use, insert the new user into the "user" table
            sql = "INSERT INTO user (firstName, lastName, email, password) VALUES (?, ?, ?, ?)"
            args = (user.first_name, user.last_name, user.email, user.password)
            cursor.execute(sql, args)  # Execute the SQL query with the provided user details
            connection.commit()  # Commit the changes to the database

    def getUser(self, email, password):
        # Using a "with" statement to open a new database connection that will be automatically closed after use
      #  with sqlite3.connect("user.db") as connection:
         #   cursor = connection.cursor()
            # SQL query to retrieve a user based on email and password
        sql = "SELECT * FROM user WHERE email = ? AND password = ?"
        args = (email, password)
        row = self.cursor.execute(sql, args).fetchone()  # Execute the query and fetch one result

        if row:
            # If a matching user is found, return a User object with the retrieved data
            return User(row[0], row[1], row[2], row[3], row[4])
        else:
            # Return None if no user is found with the provided email and password
            return None
