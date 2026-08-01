# ----------------------------------------------------
# Description:
# This program merges two lists into
# a single list.
# ----------------------------------------------------

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

merged_list = list1 + list2

print("Merged List:")
print(merged_list)