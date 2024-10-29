# you want to make a list of squares to a certain number
# there are multiple ways to can do this, which is the best

# 1st way we could just create a list called squares and iterate from 0-11 and put in the square of each number
squares = []
for x in range(0,11):
    squares.append(x**2)


# 2nd way we can also do it with a mapping function

# map function is expecting the first argument to be a function so we use a lamda function for this
# the lamda function is just square the number, so map will apply the lamda function to all numbers from 0-11
squareMap = map(lambda x: x**2, range(0, 11))
squaresListMap = list(squareMap)  # Convert map object to a list
print(squaresListMap)


# 3rd way and probably the best way for performance is using a list comprehension

# As can be seen made the list in one line of code and python optimises comprehensions to be fast
# can think of comprehensions like a formulae new_list = [expression for member in iterable]
# number*number = expression (this can be a function
# number = member
# range(0,11) = iterable
newList = [number*number for number in range(0,11)]
print(newList)


