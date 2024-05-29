# Postman Harry

# Harry is a postman. He's got a post office with a size of n*m(a matrix / 2D list). 
# Each slot at the 2D list represents the number of letters in that spot. 
# Harry can only go right and down. He starts at (0, 0), and ends at (n-1, m-1). n represents the height, and m the length. 
# Return the maximum amount of letters he can pick up. 
# He can only pick up letters if he is on that spot.

# ?
# input: (n, m)

# UPER

# Understand
# Input: lists of lists containing numbers
# Output: number - total value of path
# [1, 2],
# [3, 4]
# From top left, going only either right or down, find path with the highest combined values and return their total.
# Matrix could be different values and different amounts of lists.

# Plan
# Option 1
# for number of lists:
# check each list with position
# if x[0][1] < y[1][0]:
# marker goes to

# Option 2
# declare matrix var
# if x[0][1] < y[1][0]:

# Execute

# Revise

# ------------------------------------------------------------------------------------------------------------------------

# Edge case

# Like you saw in example 3, if the matrix is empty, return -1.


def harry(po):
	[m1, m2] = po
	count = len(po)
	while count > 1:
            for x in range(len(po)):
                print(m1[x + 1], m2[x])
                first_val = m1[x + 1]
                second_val = m2[x]
                if first_val > second_val:
                     marker = 
		


# Examples
harry([[5, 2]
	, [5, 2]])  # ➞ 12
# (5+5+2)


# harry([
#   [1, 2, 3, 4, 5],
#   [6, 7, 8, 9, 10],
#   [11, 12, 13, 14, 15]
# ])  # ➞ 72
# # (1+6+11+12+13+14+15)
# harry([[]]) ➞ -1


# Test.assert_equals(harry([
# 	[9, 9, 9],
# 	[0, 0, 9],
# 	[0, 0, 9]
# ]), 45)
# # >->->-V-V = 9 + 9 + 9 + 9 + 9 = 45