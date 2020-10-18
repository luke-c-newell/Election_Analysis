# Election_Analysis
## Election Audit Overview
The Colorado Board of Elections has asked me to complete the election audit of a recent local congressional election. The request for the audit includes the following:

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on the popular vote
6. The voter turnout for each county
7. The percentage of votes from each county out of the total count
8. The county with the highest turnout

## Resources
To complete the audit, I used the below software to analyze the election data and publish the results.
- Data Source: [election_results.csv](https://github.com/luke-c-newell/Election_Analysis/blob/main/analysis/election_results.csv)
- Software: Python 3.8.5, Visual Studio Code, 1.49.1

## Election Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election
- The number of votes per county:
  - Jefferson county saw 10.5% of the vote with 38,855 votes cast
  - Denver county saw 82.8% of the vote with 306,055 votes cast
  - Arapahoe county saw 6.7% of the vote with 24,801 votes cast
- Denver was the county with the largest number of votes cast
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote with 85,213 votes
  - Diana DeGette received 73.8% of the vote with 272,892 votes 
  - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes
- The winner of the election was: 
  - Diana DeGette who received 73.8% of the vote with 272,892 votes

The results have been published in [election_analysis.txt which can be found here.](https://github.com/luke-c-newell/Election_Analysis/blob/main/analysis/election_analysis.txt) See the below screenshot for a visualization of the results.

![alt text](https://github.com/luke-c-newell/election_analysis/blob/main/Resources/Election_analysis.png "Election_analysis")

## Election Audit Summary
Overall, the audit was a success as I was able to determine that Diana DeGette won the election with 73.8% of the vote. In order to use this script for determining the result of any election, the code must be modified to ensure that it functions correctly. This assumes that the election results are available in csv format with three columns: Ballot ID, County and Candidate.

### 1. Ensure the election results are saved in the "Resources" folder as a csv file
You will need to change line 9 of the code to enable the script to read the results of another election. The code should be changed to match the filename of the new election results, by replacing "election_results.csv" with the new filename.

![alt text](https://github.com/luke-c-newell/election_analysis/blob/main/Resources/correct_results_filepath.png "correct_results_filepath")

### 2. Create a file for the election analysis, ensuring it is saved in the "analysis" folder as a txt file
You will need to change line 11 of the code to enable the script to write the results of another election to a new file. The code should be changed to match the filename of the new election analysis, by replacing "election_analysis.txt" with the new filename.

![alt text](https://github.com/luke-c-newell/election_analysis/blob/main/Resources/correct_analysis_filepath.png "correct_analysis_filepath")

## Code sample
```
# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county = ""
largest_county_votes = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write a decision statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a repetition statement to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        county_vote_count = county_votes[county_name]
        
        # 6c: Calculate the percent of total votes for the county.
        county_vote_percentage = float(county_votes[county_name]) / float(total_votes) * 100
        # 6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {county_vote_percentage:.1f}% ({county_votes[county_name]:,})\n")
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write a decision statement to determine the winning county and get its vote count.
        if (county_votes[county_name] > largest_county_votes):
            largest_county = county_name
            largest_county_votes = county_votes[county_name]
    # 7: Print the county with the largest turnout to the terminal.
    county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
```