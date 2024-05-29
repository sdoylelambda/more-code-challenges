# Basic Arithmetic Operations on a String Number

# Create a function to perform basic arithmetic operations that includes 
# addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

# Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, 
# we are going to have only two numbers between 1 valid operator. The return value should be a number.
# eval() is not allowed. 

# In case of division, whenever the second number equals "0" return -1.
# "15 // 0"  ➞ -1

# All the inputs are only integers.
# The operators are * - + and //.

# Hint: Think about the single space that appears before and after the arithmetic operator.

# UPER

# Understand - Create calculator that takes in a math problem as a string. 
# Input: String - Math problem as a string.
# Output: Number - answer to math problem passed in.
# Addition, subtraction, multiplication and division.
# In case of division, whenever the second number equals "0" return -1.

# Plan
# Option 1
# Regex before and after operator 

# Option 2
# Split string into list.
# First value of list = first number of math problem
# Second value of list = operator
# Third value of list = second number of math problem --- if this is 0 return -1

# def arithmetic_operation(n):
#     n_list = n.split()
#     first_value = int(n_list[0])
#     second_value = int(n_list[2])
#     operator_value = n_list[1]
#     # x = { "+": first_value + second_value, "-": first_value - second_value, }

#     if second_value == 0 and operator_value == "//":
#         return -1

#     if operator_value == "+":
#         return first_value + second_value
    
#     if operator_value == "-":
#         return first_value - second_value
    
#     if operator_value == "//":
#         return first_value // second_value
    
#     if operator_value == "*":
#         return first_value * second_value

def arithmetic_operation(n):
    n_list = n.split()
    first_value = int(n_list[0])
    second_value = int(n_list[2])
    operator_value = n_list[1]

    if second_value == 0 and operator_value == "//":
        return -1
    
    math_dict = { "+": first_value + second_value, "-": first_value - second_value, "*": first_value * second_value, "//": first_value // second_value }

    for i in math_dict:
        if operator_value == i:
            return math_dict.get(operator_value)
    

    # math_problem = int(first_value) int(operator_value) int(second_value)
    # print(math_problem)


arithmetic_operation("122 // 0")
 
# arithmetic_operation("12 + 0")  # ➞ 24 // 12 + 12 = 24

# arithmetic_operation("12 - 12")  # ➞ 24 // 12 - 12 = 0

# arithmetic_operation("12 * 12")  # ➞ 144 // 12 * 12 = 144

# arithmetic_operation("12 // 0")  # ➞ -1 // 12 / 0 = -1
