import csv  # Import the csv module for reading from and writing to CSV files.

# # ------------------------exercise 1---------------------------------
# Exercise 1: Write a Python script to open and read the contents of a CSV file,
# then print each row to the console.
#
# # Open 'data.csv' in read mode. "newline=''" ensures consistent line endings.
# with open('data.csv', newline='') as data_file:
#     # # Create a CSV reader object to read the file line by line.
#     data_file_reader = csv.reader(data_file)
#
#     i = 0  # Initialize a counter to track row numbers.
#
#     for row in data_file_reader:  # Iterate over each row in the CSV file.
#         i += 1  # Increment the counter for each row.
#         # # Print the current row number and its contents.
#         print("Here is row number", i, "of our file:", row)

# ---------------------------exercise 2---------------------------------
# Exercise 2: Modify the script from Exercise 1 to store the CSV data (excluding the header) in a list of dictionaries.

data = []  # Initialize an empty list to store the CSV data as dictionaries.
with open('data.csv', newline='') as data_file:  # Open 'data.csv' again in read mode.
    # # Use DictReader to automatically map each row to a dictionary using header names.
    data_file_reader = csv.DictReader(data_file)

    for row in data_file_reader:  # Iterate over each row (now a dictionary) in the CSV file.
        data.append(row)  # Append each row dictionary to the 'data' list.

print("This is the data dictionary:", data)

# ------------------- Exercise 3 -------------------------
# # Exercise 3: Calculate the average age and the average score.

# total_age = 0
# total_score = 0
# count = 0  # number of rows
#
# for row in data:
#     total_age += int(row['age'])  # Add the age from the current row to the total age.
#     total_score += int(row['score'])  # Add the score from the current row to the total score.
#     count += 1  # Increment the counter for each processed row.
#
# avg_age = total_age / count
# avg_score = total_score / count
#
# # f-strings allow us to insert variables directly into strings.
# print(f"Average Age: {avg_age}")
# print(f"Average Score: {avg_score}")

# ------------------------------exercise 4------------------------------
# # Exercise 4: Write a Python script to find and print the name of the person with the highest score.
#
# highest_score = 0
# top_scorer = ""
#
# for row in data:
#     # # if the current row's score is higher than the current highest_score.
#     if int(row['score']) > highest_score:
#         highest_score = int(row['score'])  # Update highest_score with the current row's score.
#         top_scorer = row['name']  # Update top_scorer with the name associated with the new highest score.
#
# print(f"Top Scorer: {top_scorer} with a score of {highest_score}")

# ------------------------------exercise 5--------------------------------------
# # Exercise 5: Write a new CSV file that contains only the rows of people whose score is above 80.

# Create a list of dictionaries only for rows with scores above 80.
# filtered_data = [row for row in data if int(row['score']) > 80]
#
# # # Open a new file in write mode to save filtered data. 'w' = write mode
# with open('filtered_data.csv', 'w', newline='') as filtered_data_file:
#     # # Specify the column names to be used as headers in the new CSV.
#     # # fieldnames = headers = 'column names'
#     fieldnames = ['name', 'age', 'score']
#     # # Create a CSV writer object for dictionaries.
#     writer = csv.DictWriter(filtered_data_file, fieldnames=fieldnames)
#
#     writer.writeheader()  # Write the header to the new CSV file.
#     writer.writerows(filtered_data)  # Write all rows from 'filtered_data' to the new CSV file.
#
# print("Filtered data has been written to filtered_data.csv")

# ------------------------------exercise 6--------------------------------------
# Exercise 6: Sort the data by age in ascending order and write the sorted data to a new CSV file.

# Sort the list of dictionaries by the 'age' field in ascending order.
# sorted is a function
# a 'lambda' function is a one-line 'anonymous' function that does not need a name
# in this case, our lambda function is our SORTING KEY
# it extracts the 'age' value from each dictionary (x) in the list and converts it to an int
# the sorted function then sorts the list in order of age values.
sorted_data = sorted(data, key=lambda x: int(x['age']))

with open('sorted_data.csv', 'w', newline='') as sorted_data_file:
    fieldnames = ['name', 'age', 'score']
    writer = csv.DictWriter(sorted_data_file, fieldnames=fieldnames)

    writer.writeheader()  # Write the header to the new CSV file.
    writer.writerows(sorted_data)  # Write all rows from 'sorted_data' to the new CSV file.

print("Sorted data has been written to sorted_data.csv")
