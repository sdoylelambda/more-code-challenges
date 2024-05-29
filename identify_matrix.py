# Identity Matrix

# An identity matrix is defined as a square matrix with 
# 1s running from the top left of the square to the bottom right. 
# The rest are 0s. The identity matrix has applications ranging from machine learning to the general theory of relativity.

# Create a function that takes an integer n and returns the identity matrix of n x n dimensions. 
# For this challenge, if the integer is negative, return the mirror image of the identity matrix of n x n dimensions.. 
# It does not matter if the mirror image is left-right or top-bottom.

# UPER

# Understand - return list of lists x values long with 1's running diagnal starting top left. Negative reverse with 1 in top right.
# input - number
# output - list of lists
# Incompatible types passed as n should return the string "Error".

# Runs n number of times

# Plan
# Option 1
# Create output arr
# for x in input
# output += [1, + x 0s]

# counter
# move position over with counter + 1 each loop
# output += [x 0s]

# Option 2

# count = 0

# def display(n):
#     return [x**2 for x in range(n)]


def id_mtrx(n):
    if type(n) != int:
        return 'Error'
    
    is_negative = False
    
    if n < 0:
        n = n * -1
        is_negative = True
    # if num == 0:
    #     lst[n - 1] = 1

    output_list_of_lists = []
    lst = [0] * n

    print(is_negative)
    
    for num in range(n):
        print('num:', num)
        print('1st lst:', lst)

        if is_negative:
            num = num * - 1
        
        lst[num] = 1 # change to last
        print(lst)
        output_list_of_lists.append(lst)
        lst = [0] * n

    if is_negative:
        output_list_of_lists.pop(0)

    print('OUTPUT:', output_list_of_lists)
    return output_list_of_lists


id_mtrx(2)  # ➞ [
#   [1, 0],
#   [0, 1]
# ]

# id_mtrx(-2) ➞ [
#   [0, 1],
#   [1, 0]
# ]

# id_mtrx(0) ➞ []

# id_mtrx(-6)
