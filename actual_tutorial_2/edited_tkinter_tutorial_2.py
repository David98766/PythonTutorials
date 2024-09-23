# Import the tkinter library and assign it an alias 'tk' for creating the GUI
import tkinter as tk

# Function to handle button click event for greeting
def greet():
    # Print message to console
    print("Hello, IS2208")
    # Change the text of the 'response' label to indicate the button has been clicked
    response.config(text="You clicked the button!")

# this function allows us not to keep copying and pasting this code into add, subtract, etc.
def getNumbers():
    # Retrieve the values from the two entry fields and convert them to integers
    num1 = int(num_entry_1.get())
    num2 = int(num_entry_2.get())
    # return the numbers so we can pass them to the other functions e.g add()
    return num1, num2

# this function allows us to populate the result entry box no matter what the sum is
def insertResult(sumResult):
    result.insert(0, sumResult)

    # Add this during part 3, not part 2. It appends the latest result to the big text box and adds a new line
    text_box.insert(tk.END, sumResult)
    text_box.insert(tk.END, "\n")

# Function to handle the addition of two numbers
def add():
    # call the getnumbers() function and assigning the num1 and num2 ints
    num1, num2 = getNumbers()
    # Perform the addition operation
    sumResult = num1 + num2
    # call the insertResult function and pass the sumResult variable
    insertResult(sumResult)

def subtract():
    num1, num2 = getNumbers()
    sumResult = num1 - num2
    insertResult(sumResult)

def multiply():
    num1, num2 = getNumbers()
    sumResult = num1 * num2
    insertResult(sumResult)

def divide():
    num1, num2 = getNumbers()
    sumResult = num1 / num2
    insertResult(sumResult)

# Function to clear all input fields and result field
def clear():
    # Clear the first number entry field
    num_entry_1.delete(0, tk.END)
    # Clear the second number entry field
    num_entry_2.delete(0, tk.END)
    # Clear the result entry field
    result.delete(0, tk.END)

def clearBigBox():
    #"1.0": This represents the starting position in the text box (line 1, character 0, i.e., the very beginning
    #tk.END: This represents the end of the content in the text box, ensuring everything is cleared.
    text_box.delete("1.0", tk.END)  # Clears the content of the text box

# Function to print the content of the text box to the console
def gettext():
    # Get the text from the text box from the start to the end and print it
    print(text_box.get("1.0", tk.END))

# Create the main application window
window = tk.Tk()

# Create a label widget that displays a greeting message
greeting = tk.Label(text="Hello, IS2208. Welcome to Tkinter")

# Create a button that triggers the greet function when clicked
button = tk.Button(text="Click Me", command=greet)

# Create a label that displays a response to the button click
response = tk.Label(text="You have not clicked yet.")

# Create entry fields to input two numbers for addition
num_entry_1 = tk.Entry(width=20)  # Entry field for first number
num_entry_2 = tk.Entry(width=20)  # Entry field for second number

# Create a button that triggers the add function to perform addition
button_add = tk.Button(text="Add", command=add)

# Create a button that triggers the subtract function to perform subtraction
button_subtract = tk.Button(text="Subtract", command=subtract)

button_multiply = tk.Button(text="Multiply", command=multiply)

button_divide = tk.Button(text="Divide", command=divide)

# Create a button that triggers the clear function to clear the input and result fields
button_clear = tk.Button(text="Clear", command=clear)

button_clearBigBox = tk.Button(text="Clear Big Box", command=clearBigBox)

# Create an entry field to display the result of the addition
result = tk.Entry(width=15)

# Create a button that triggers the gettext function to print the content of the text box
button_get_text = tk.Button(text="Get Text", command=gettext)

# Create a text box widget to allow multiline text input
text_box = tk.Text()

# Place the greeting label at the top of the window (row 0, spanning 3 columns)
greeting.grid(row=0, column=0, columnspan=3)

# Place the button and response label on the second row
button.grid(row=1, column=0)  # Button placed in column 0
response.grid(row=1, column=1)  # Response label placed in column 1

# Place the entry fields for numbers on the third and fourth rows
num_entry_1.grid(row=3, column=0)  # First number entry
num_entry_2.grid(row=4, column=0)  # Second number entry

# Place the add and clear buttons on the third row
button_add.grid(row=3, column=1)  # Add button placed in column 1
button_clear.grid(row=3, column=2)  # Clear button placed in column 2
button_clearBigBox.grid(row=7, column=1)

#Place the subtract, multiply, and divide buttons on the 5th row
button_subtract.grid(row=5, column=1)  # subtract button placed in column 1

button_multiply.grid(row=5, column=2)

button_divide.grid(row=7, column=2)

# Place the result entry field on the fourth row (spanning 2 columns)
result.grid(row=4, column=1, columnspan=2)

# Place the get text button on the fifth row (spanning 2 columns)
button_get_text.grid(row=5, column=0, columnspan=2)

# Place the text box on the sixth row (spanning 3 columns)
text_box.grid(row=8, column=0, columnspan=3)


# Start the Tkinter main event loop, which waits for user interactions and updates the GUI
window.mainloop()