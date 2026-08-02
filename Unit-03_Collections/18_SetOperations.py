# ----------------------------------------------------
# Description:
# This program performs union,
# intersection, difference and
# symmetric difference on two sets.
# ----------------------------------------------------

set1 = set(map(int, input("Enter first set: ").split()))
set2 = set(map(int, input("Enter second set: ").split()))

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (Set1 - Set2):", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)