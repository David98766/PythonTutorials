import csv

# ------------------------exercise 1---------------------------------
# # exercise 1 = Write a Python script to open and read the contents of a CSV file,
# then print each row to the console.

# with open('data.csv', newline='') as data_file:
#     data_file_reader = csv.reader(data_file)
#
#     i = 0
#
#     for row in data_file_reader:
#         i += 1
#         print ("Here is row number", i, "of our file:", row)

# ---------------------------exercise 2---------------------------------
# Modify the script from Exercise 1 to store the CSV data (excluding the header) in a list of dictionaries.

# data = []
# with open('data.csv', newline = '') as data_file:
#     data_file_reader = csv.DictReader(data_file)
#
#     for row in data_file_reader:
#         data.append(row)
#
# print ("This is the data dictionary:", data)


# ------------------- Exercise 3 -------------------------
# # calculate the average age and the average score.

# total_age = 0
# total_score = 0
# count = 0
#
# for row in data:
#     total_age += int(row['age']) # age for this row. this row = the row currently going through the loop.
#     total_score += int(row['score']) # score for this row
#     count += 1 # increment count after each row
#
# avg_age = total_age / count
# avg_score = total_score / count
#
# # f strings allow us to insert variables into strings
# print(f"Average Age: {avg_age}")
# print(f"Average Score: {avg_score}")

# ------------------------------exercise 4------------------------------
#  # Write a Python script to find and print the name of the person with the highest score.
# max_score = 0
# top_scorer = ""
#
# for row in data:
#     if int(row['score']) > max_score:
#         max_score = int(row['score'])
#         top_scorer = row['name']
#
# print(f"Top Scorer: {top_scorer} with a score of {max_score}")

# ------------------------------exercise 5--------------------------------------
# # Write a new CSV file that contains only the rows of people whose score is above 80.

# filtered_data = [row for row in data if int(row['score']) > 80]
#
# with open('filtered_data.csv', 'w', newline='') as filtered_data_file:
#     fieldnames = ['name', 'age', 'score']
#     writer = csv.DictWriter(filtered_data_file, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerows(filtered_data)
#
# print("Filtered data has been written to filtered_data.csv")

# ------------------------------exercise 6--------------------------------------
# Sort the data by age in ascending order and write the sorted data to a new CSV file.
#
# sorted_data = sorted(data, key=lambda x: int(x['age']))
#
# with open('sorted_data.csv', 'w', newline='') as sorted_data_file:
#     fieldnames = ['name', 'age', 'score']
#     writer = csv.DictWriter(sorted_data_file, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerows(sorted_data)
#
# print("Sorted data has been written to sorted_data.csv")