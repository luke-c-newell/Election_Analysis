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
