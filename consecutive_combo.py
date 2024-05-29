# Combined Consecutive Sequence
# Write a function that returns True if two arrays, when combined, form a consecutive sequence. 
# A consecutive sequence is a sequence without any gaps in the integers, 
# e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.
# The input lists will have unique values.
# The input lists can be in any order.

# UPER

# Understand
# Input: 2 lists of numbers
# Output: bool
# check if lists combined make a straight

# Plan
# Option 1
# Combine lists
# Put in order
# Loop thru
# See if each next number is +1

# Option 2

# Execute
# def consecutive_combo(lst1, lst2):
#     lst = lst1 + lst2
#     lst.sort()
#     print(lst)
#     for x in range(len(lst) - 1):
#         if not lst[x] + 1 == lst[x+1]:
#             print(False)
#             return False
#     print(True)
#     return True

# Revise
def consecutive_combo(lst1, lst2):
    lst = lst1 + lst2
    lst.sort()
    for x in range(len(lst) - 1):
        print(False if not lst[x] + 1 == lst[x+1] else True)
        return False if not lst[x] + 1 == lst[x+1] else True



consecutive_combo([7, 4, 5, 1], [2, 3, 6])  # ➞ True

consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9])  # ➞ False

consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10])  # ➞ False

consecutive_combo([44, 46], [45])  # ➞ True
