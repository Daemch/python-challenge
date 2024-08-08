
import csv

# Create variables
total_votes = 0
candidate_votes = {}  

# Read the CSV file 
with open('election_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

    for row in reader:
        candidate = row[2]  
        votes = int(row[0])  

        # Update total votes
        total_votes += votes

         # Update candidate votes
        if candidate in candidate_votes:
            candidate_votes[candidate] += votes
        else:
            candidate_votes[candidate] = votes

# Calculate percentages and export to a text file
with open('PyPoll_Results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        text.write(f"{candidate}: {percentage:.2f}% ({votes} votes)\n")
        print(f"{candidate}: {percentage:.2f}% ({votes} votes)")
    text.write("-------------------------\n")
    winner = max(candidate_votes, key=candidate_votes.get)
    text.write(f"Winner: {winner} ({candidate_votes[winner]} votes)\n")
    print(f"Winner: {winner} ({candidate_votes[winner]} votes)")