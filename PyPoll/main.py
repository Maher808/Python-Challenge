import csv
# Path to the CSV file
csv_path = r"PyPoll\Resources\election_data.csv"

# Function to analyze election data
def analyze_election_data(csv_path):
    # Initialize variables
    total_votes = 0
    candidate_votes = {}

    # Read CSV file
    with open(csv_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        
        # Skip header
        next(csvreader)

        # Loop through rows in the CSV
        for row in csvreader:
            candidate = row[2]

            # Count total votes
            total_votes += 1

            # Count votes for each candidate
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1

    # Find the winner
    winner = max(candidate_votes, key=candidate_votes.get)

    

    # Display results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Write in Txt file 
    file= open("Election Results.txt", "w")
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------")


# Call the function with the CSV file path
analyze_election_data(csv_path)