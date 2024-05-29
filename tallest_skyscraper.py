# Tallest Skyscraper

# A city skyline can be represented as a 2-D list with 1s representing buildings. 

# In the example below, the height of the tallest building is 4 (second-most right column).

# [[0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 1, 0],
# [0, 0, 1, 0, 1, 0],
# [0, 1, 1, 1, 1, 0],
# [1, 1, 1, 1, 1, 1]]

# Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.

# UPER

# Understand
# Input: matrix - list of lists - numbers
# Output: number - height of tallest skyscraper
# 1's are buildings starting at the bottom list building upwards until a 0.

# Plan

# Option 1

# highest_building = 0
# Iterate thru last list
# if list[x] = 1
# check value in list above with same position point
# loop until 0
# if loop_count > highest_building:
# highest_building = # of loops

# Option 2
# Faster run time

# Check first list for 1's
# if none
# check next list for 1's
# proceed until found
# return reverse range(len(list_inputed)) verify this - num_of_loops


# Execute
# def tallest_skyscraper(lst):
#     floor_count = len(lst)
#     for floor_check in lst:
#         for building in floor_check:
#             if building == 1:
#                 return floor_count
#         floor_count -= 1


# Revise
def tallest_skyscraper(lst):
    floor_count = len(lst)
    for x in lst:
        print(x)
        for i in range(len(lst)):
            print('i', lst[i])
            if lst[x][i] == 1:
                print('yes')
        #     return x


# tallest_skyscraper([
#   [0, 0, 0, 0],
#   [0, 1, 0, 0],
#   [0, 1, 1, 0],
#   [1, 1, 1, 1]
# ])  # ➞ 3

# tallest_skyscraper([
#   [0, 1, 0, 0],
#   [0, 1, 0, 0],
#   [0, 1, 1, 0],
#   [1, 1, 1, 1]
# ])  # ➞ 4

tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
])  # ➞ 2
