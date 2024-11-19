import sqlite3
from Tutorial_13.model.User import User


class UserDao:
    def __init__(self):
        # creating the connection to the user.db when the UserDao object is created
        self.connection = sqlite3.connect("user.db")
        # we use cursor objects to execute SQL queries
        self.cursor = self.connection.cursor()
        # using the cursor to create the user table if it doesn't exist
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS user (
                  id INTEGER PRIMARY KEY,
                  firstName TEXT,
                  lastName TEXT,
                  email TEXT,
                  password TEXT
                  )""")

    # Destructor to close the connection when the UserDao object is no longer in use
    def __del__(self):
        self.connection.close()

    def addUser(self, user):
        # SQL query for insert; the '?' are placeholders for variables
        sql = ("INSERT INTO user VALUES(?, ?, ?, ?, ?)")
        # args is a tuple with the attributes of a user in order: firstName, lastName, email, password
        args = (user.id, user.first_name, user.last_name, user.email, user.password)
        # using the cursor to execute the query with the args tuple, filling in the '?' placeholders
        self.cursor.execute(sql, args)
        self.connection.commit()

    def getUser(self, email, password):
        sql = "SELECT * FROM user WHERE email = ? AND password = ?"
        args = (email, password)  # Tuple containing email and password for the query
        row = self.cursor.execute(sql, args).fetchone()  # Use fetchone() to get a single result

        if row:
            # Assuming the User constructor takes five arguments: id, firstName, lastName, email, password
            return User(row[0], row[1], row[2], row[3], row[4])
        else:
            return None  # Return None if no user is found with the given email and password

    def deleteUser(self, email):
        sql = ("DELETE FROM user WHERE email = ?")
        args = (email,)
        self.cursor.execute(sql, args)
        self.connection.commit()