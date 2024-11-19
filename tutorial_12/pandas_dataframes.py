import pandas as pd
import time

##Load the CSV File into a dataframe
##dataframe is being called df
##Pandas library is being called pd

df = pd.read_csv('data.csv')
## Print the dataframe as a string in the output terminal (not the project terminal)
##to_string() prints the entire dataframe
#print(df.to_string())

## The number of rows returned is defined in the Pandas option settings
##You can check your systems number of maximum returned rows:
#print("System max rows:", pd.options.display.max_rows)

## The reason the print(df.to_string()) function printed more than your Pandas max_rows settings
## is because the to_string() function bypasses this rule and prints the entire dataframe

## when we use the print(df) statement, if the number of lines in the dataframe is greater than
## the Pandas max_rows settings then the print(df) statement will only print the header, the first 5
## and last 5 lines of the dataframe.
#print(df)

##lets change the Pandas max_rows settings
pd.options.display.max_rows = 9999
##now we will be able to print the entire dataframe into our terminal using the print(df) statement
#print(df)

## print the first 5 rows:
#print("This is the head:\n", df.head(), sep="")

## print the last five rows
#print("This is the tail\n", df.tail(), sep="")

## You can set a column as an index. Usually we would use an id column for this, but ours does not
## have an id column so we will just use Maxpulse. Notice how the Maxpulse column is now on the left
## instead of the column number
#df = pd.read_csv('data.csv', index_col="Maxpulse")
#print(df.tail())

## You can also give a column number
#df = pd.read_csv('data.csv', index_col=2)
#print(df.tail())

## Once you know how to read a CSV file from local storage into memory, reading data from other
## sources is easy. Its ultimately the same process, except that you're no longer passing a file
## path, but a URL
## Webpage URL
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
#
# # Define the column names
# col_names = ["sepal_length_in_cm",
#            "sepal_width_in_cm",
#            "petal_length_in_cm",
#            "petal_width_in_cm",
#            "class"]
#
# # Read data from URL
# iris_data = pd.read_csv(url, names=col_names)
#
# print(iris_data.head())

def load_sports_data():
    # URL for a csv file about MLB team from 2012
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/mlb_teams_2012.csv"

    # Define the column names
    col_names = ["Team", "Payroll(millions)", "Wins"]

    # Read data from URL
    # skiprows skips the first row (headers) because we are assigning the col_names manually
    # We are using the Team column as our index, as it is essentially a Primary Key
    sports_data = pd.read_csv(url, names=col_names, skiprows=1, index_col="Team")
    # Print the whole thing
    print(sports_data.to_string())

# This is a little like using an Application Programming Interface (API)
refresh_interval = 5 # seconds

# while true means it will run until it is manually stopped or interrupted
while True:
    # calling the function that grabs the data from the web file
    load_sports_data()
    # setting a pause or 'wait' time that pauses the loop (uses refresh_interval as an argument)
    time.sleep(refresh_interval)