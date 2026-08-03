# ----------------------------------------------------
# Description:
# This program simulates a simple voting
# system using a dictionary to count votes
# received by each candidate.
# ----------------------------------------------------

votes = {}

n = int(input("Enter the number of votes: "))

for i in range(n):
    candidate = input("Enter candidate name: ")

    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1

print("\nElection Results")

for candidate, count in votes.items():
    print(f"{candidate} : {count}")

winner = max(votes, key=votes.get)

print(f"\nWinner: {winner}")
print(f"Votes Received: {votes[winner]}")