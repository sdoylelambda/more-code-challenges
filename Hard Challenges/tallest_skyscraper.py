# Tallest Skyscraper
# A city skyline can be represented as a 2-D list with 1s representing buildings. 
# In the example below, the height of the tallest building is 4 (second-most right column).

# [[0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 1, 0],
# [0, 0, 1, 0, 1, 0],
# [0, 1, 1, 1, 1, 0],
# [1, 1, 1, 1, 1, 1]]

# Create a function that takes a skyline (2-D list of 0's and 1's) and 
# returns the height of the tallest skyscraper.


# [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1]]

# UPER

# Understand
# Input: 2-D list
# Output: Number 
# Return the hight of the tallest building
# The count of the most sequential 1's in the same position point in each list

# Plan

# Option 1
# Find the lenght of the lists
# Check if any list has a 1 there

# Option 2
# Recursive Solution
# Does top floor exist? 
# If yes return the floor
# If no check the next floor down 
# repeat

# Execute

# Revise

# Option 1
# def tallest_skyscraper(lst):
#     tallest_building = 0
#     current_floor = len(lst)
#     for floor in range(len(lst)):
#         print(floor)
#         print(lst[floor])
#         # for building in floor:
#         #     print(building)
#         for x in lst[floor]:
#             if floor[x] == 1:
#                 return current_floor
#         current_floor -= 1
#     print('tallest_building:', tallest_building)
#     return tallest_building

# Option 2
# def tallest_skyscraper(lst):
#     current_floor = len(lst)
#     print(current_floor)
#     for floor in range(len(lst)):
#         print(floor)
#         print(lst[floor])
#         # Does top floor exist? 
#         if lst[floor] == 1:
#             # If yes return the floor
#             print('OUTPUT:', current_floor)
#             return current_floor
#         # If no check the next floor down 
#         current_floor -= 1
#         # repeat
      
# def tallest_skyscraper(lst):
#     current_floor = len(lst)
#     for floor in range(len(lst)):
#         level = lst[floor]
#         for building in level:
#             if building == 1:
#                 print('OUTPUT:', current_floor)
#                 return current_floor
#         current_floor -= 1

# def tallest_skyscraper(lst):
#     for floor in range(len(lst)):
#         if 1 in lst[floor]:
#             return len(lst) - floor

def tallest_skyscraper(lst):
    return len(lst) - next(floor for floor, level in enumerate(lst) if 1 in level)



# Examples
# tallest_skyscraper([
#   [0, 0, 0, 0],
#   [0, 1, 0, 0],
#   [0, 1, 1, 0],
#   [1, 1, 1, 1]
# ])  # ➞ 3

tallest_skyscraper([
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
])  # ➞ 4

# tallest_skyscraper([
#   [0, 0, 0, 0],
#   [0, 0, 0, 0],
#   [1, 1, 1, 0],
#   [1, 1, 1, 1]
# ])  # ➞ 2



# check each value, if equal to 1: return true

# lst = [0, 1]

# for x in lst:
#     print(x)
#     if lst[x] == 1:
#         print(True)