# Pentagonal Number
# Write a function that takes a positive integer num and calculates how many dots exist in a pentagonal shape 
# around the center dot on the Nth iteration.

# Return the number of dots that exist in the whole pentagon on the Nth iteration.

# UPER

# Understand
# Input: num - number of dots on each side - number of dots fron center to edge
# Output: num

# Plan
# Option 1
# output = 0





def pentagonal(num):
    output = 1
    for x in range(1, num):
        i = 5 * x
        output += i
    print(output)
    return output


pentagonal(1)  # ➞ 1

pentagonal(2)  # ➞ 6

pentagonal(3)  # ➞ 16

# pentagonal(8)  # ➞ 141