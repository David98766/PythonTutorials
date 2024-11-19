import sqlite3

from Tutorial_13.model.Car import Car

# Define the DAO class
class CarDao:

    # Constructor and destructor
# constructor to create a CarDao object
    def __init__(self):
        # creating the connection to the cars.db when the carDao Object is created
        self.connection = sqlite3.connect("cars.db")
        # we use cursor objects to execute sql queries
        self.cursor = self.connection.cursor()
        # using the cursor to create the car table if it dosen't exist
        # three quotes because that is how you do a multiline string in Python
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS car (
            id INTEGER PRIMARY KEY,
            make TEXT,
            model TEXT,
            engine_capacity FLOAT,
            top_speed INTEGER,
            price INTEGER
            )""")

    # destructor for closing the connection when python destroys the unused CarDao object
    def __del__(self):
        self.connection.close()

    # CRUD operations

    # CREATE
    def addCar(self, car):
        # sql query for insert the '?' are placeholders for variables
        sql = ("INSERT INTO car VALUES(NULL, ?, ?, ?, ?, ?)")
        # args is a tuple and you put the attributes of a car into this tuple
        args = (car.make, car.model, car.engine_capacity, car.top_speed, car.price)
        # using the cursor method to execute the query with the args tuple so will fill in the '?' in order given so order matters!!
        self.cursor.execute(sql, args)
        self.connection.commit()

    # READ
    def getCar(self, id):
        # sql query for insert the '?' are placeholders for the id
        sql = ("SELECT * FROM car WHERE id = ?")
        args = (id,)  # Note the comma to make it a tuple
        # row is the variable holding the data retrieved from database, the fetchall()[0] means return first record
        row = self.cursor.execute(sql, args).fetchall()[0]
        # converting row to a Car object, all the values on the record are passed to the car constructor
        return Car(row[0], row[1], row[2], row[3], row[4], row[5])

    def getAllCars(self):
        # Create empty list to hold all car objects retrieved
        cars = []
        # rows will hold all the retrieved rows from the database, fetchall() means return all records
        rows = self.cursor.execute("SELECT * FROM car").fetchall()
        # for loop to convert every row returned into a car object
        for row in rows:
            # append each new car object onto the list
            cars.append(Car(row[0], row[1], row[2], row[3], row[4], row[5]))
            #return the populated list
        return cars

    # UPDATE
    def updateCar(self, car):
        # update query for the car table
        sql = ("""UPDATE car
            SET make = ?, model = ?, engine_capacity = ?, top_speed = ?, price = ?
            WHERE id = ?""")
        args = (car.make, car.model, car.engine_capacity, car.top_speed, car.price, car.id)
        # using cursor to execute the query, no return of row not using the data just changing it
        self.cursor.execute(sql, args)
        # commit the change to the database
        self.connection.commit()

    # DELETE
    def deleteCar(self, id):
        # write sql query for delete given an id
        sql = ("DELETE FROM car WHERE id = ?")
        # pass the id argument in
        args = (str(id))
        # use cursor to execute the query
        self.cursor.execute(sql, args)
        # commit change to database
        self.connection.commit()