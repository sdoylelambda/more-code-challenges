# Next Number Greater Than A and B and Divisible by B

# You are given two numbers a and b. 
# Create a function that 
# returns the next number greater than a and b and divisible by b.

# UPER

# Understand
# Input: a, b - both numbers
# Output: number

# Plan
# Option 1
# x = larger of a or b
# if x % b:
# return x
# else
# x += 1
# recurse

# def run_program(a, b):
#     if a % b == 0:
#         print('output', a)
#         return a
    
#     else:
#         b += 1

#     run_program(a, b)


def divisible_by_b(a, b):
    if a % b == 0:
        print('output', a)
        return a
    
    else:
        b += 1
        divisible_by_b(a, b)

# divisible_by_b(17, 8)  # ➞ 24

divisible_by_b(98, 3)  # ➞ 99

divisible_by_b(14, 11)  # ➞ 22
# Notes
# a will always be greater  # than b.