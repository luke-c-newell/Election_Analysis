# The data we need to retrieve.
import csv
import os

# Assign a variable for the file to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read and print the header row
    headers = next(file_reader)
    print(headers)
    # # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)


# Using the with statement and open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.

     txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")


# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote