

# UPER

# Understand
# Input: int
# Output: int
# Factorial of a non-negative integer is the multiplication of all positive integers smaller than or equal to n. 
# Is it safe to assume that all values will be non-negative? If not a try catch block will need to be added, perhaps with a custom execption type.
# For example factorial of 6 is 6*5*4*3*2*1 which is 720.

# Plan
# Option 1
# Create output var
# For loop on input
# multiple output * loop value
# return output

# Option 2
# Create output list
# For loop on input
# combine output list using numpy.prod()
# return output

# Execute


def factorial(num):
    output = num
    for n in range(1, num):
        output *= n
    return output

# Revise 
# Make variable names more descriptive


print(factorial(6))  # output: 720


# def multiplyList(myList):
 
#     # Multiply elements one by one
#     result = 1
#     for x in myList:
#         print(x)
#         result = result * x
#     return result
 
 
# # Driver code
# list1 = [1, 2, 3]
# list2 = [3, 2, 4]
# print(multiplyList(list1))
# print(multiplyList(list2))