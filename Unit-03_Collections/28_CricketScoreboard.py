# ----------------------------------------------------
# Description:
# This program stores the runs scored by
# players and displays the highest scorer.
# ----------------------------------------------------

scores = {}

n = int(input("Enter number of players: "))

for i in range(n):
    player = input("Enter Player Name: ")
    runs = int(input("Enter Runs: "))
    scores[player] = runs

print("\nScoreboard")

for player, runs in scores.items():
    print(f"{player} : {runs}")

highest_scorer = max(scores, key=scores.get)

print(f"\nHighest Scorer : {highest_scorer}")
print(f"Runs           : {scores[highest_scorer]}")