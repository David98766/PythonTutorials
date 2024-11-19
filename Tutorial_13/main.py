# Demonstrating the use of the Car class
from Tutorial_13.dao.CarDao import CarDao
from Tutorial_13.model.Car import Car

if __name__ == "__main__":
    # create CarDao object
    # the () after CarDao, calls the __init__ method of the CarDao class
    myCarDao = CarDao()
    # print all the objects in the database
    print(myCarDao.getAllCars())

    # add a created car to the database
    myCarDao.addCar(Car(0, "Ford", "Fiesta", 1.2, 130, 10500))
    print(myCarDao.getAllCars())

    # delete the car
    myCarDao.deleteCar(2)
    print(myCarDao.getAllCars())

    # update the car object
    myCarDao.updateCar(Car(7, "Ford", "Mondeo", 2.0, 195, 37250))
    print(myCarDao.getAllCars())

    print("\n", myCarDao.getCar(1), "\n")


    del myCarDao