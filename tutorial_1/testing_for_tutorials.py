print("Hello World!")

class Animal:
    # *NOTICE THE INDENTATION!*
    # initializing the Animal class
    def __init__(self, name):
        self.name = name

    # defining a class method
    # ignore where it says "1 usage" that text is auto-generated
    def introduce_yourself(self):
        print("Hi, my name is " + self.name)

# Creating an Animal object (dog)
# an object as an instance of a class, in this case dog(object) is an instance of Animal(class)
dog = Animal("Scooby-Doo")

# Calling an Animal class method (introduce_yourself()) to introduce the dog (we can do this because it is an object)
dog.introduce_yourself()
