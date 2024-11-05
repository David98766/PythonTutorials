import sqlite3
# Define the Car class
class Car:

# Constructor for creating a car object
    def __init__(self, id, make, model, engine_capacity, top_speed, price):
        self.id = id
        self.make = make
        self.model = model
        self.engine_capacity = engine_capacity
        self.top_speed = top_speed
        self.price = price

# to string method to print a car object
    def __str__(self):
        return f"ID: {self.id}, Make: {self.make}, Model: {self.model}, Engine Capacity: {self.engine_capacity}, Top Speed: {self.top_speed} km/h, Price: €{self.price}"

    def __repr__(self):
        return str(self)