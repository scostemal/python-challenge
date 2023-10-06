import csv
from pathlib import Path

# Function to calculate election results
def calculate_election_results(csv_file_path):
    # Initialize variables to store election data
    total_votes = 0
    candidate_votes = {}
    winner = ""
    winner_votes = 0

    # Read the CSV file using the absolute path
    with open(csv_file_path, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the header row
        next(csvreader)

        for row in csvreader:
            total_votes += 1
            candidate = row[2]

            # If the candidate is not in the dictionary, add them with 1 vote
            if candidate not in candidate_votes:
                candidate_votes[candidate] = 1
            else:
                candidate_votes[candidate] += 1

    # Initialize variables to store the analysis results
    results = []

    # Calculate and store the results
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        results.append(f"{candidate}: {percentage:.3f}% ({votes})")
        if votes > winner_votes:
            winner_votes = votes
            winner = candidate

    return {
        "total_votes": total_votes,
        "results": results,
        "winner": winner
    }

# Get the absolute path to the CSV file
csv_file_path = Path("Resources/election_data.csv").resolve()

# Calculate election results
results = calculate_election_results(csv_file_path)

# Print the results to the terminal
print("Election Results")
print("-" * 25)
print(f"Total Votes: {results['total_votes']}")
print("-" * 25)
print("\n".join(results['results']))
print("-" * 25)
print(f"Winner: {results['winner']}")
print("-" * 25)

# Export the results to a text file
with open("election_results.txt", "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("-" * 25 + "\n")
    textfile.write(f"Total Votes: {results['total_votes']}\n")
    textfile.write("-" * 25 + "\n")
    textfile.write("\n".join(results['results']) + "\n")
    textfile.write("-" * 25 + "\n")
    textfile.write(f"Winner: {results['winner']}\n")
    textfile.write("-" * 25 + "\n")

print("Results have been exported to election_results.txt")
