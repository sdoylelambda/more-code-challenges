# Length of Number

# UPER

# Understand - Create a function that takes a number num and returns its length.
# input: number
# output: number

# Plan
# option 1
# split apart number and return count of splits

# option 2
# recursion? - count outside of function - doesn't sound good

# option 3
# any suggestions?

# Execute

# Revise

# def number_length(num):
#     length = 0
#     for x in str(num):
#         length += 1
#     print(length)

# def number_length(num):
#     arr_num = []
#     str_number = str(num)
#     for char in str_number:
#         arr_num.append(char)

#     count = 0
#     for x in arr_num:
#         count += 1
#     print(count)
#     return count

# def number_length(num):
#     arr_num = [int(digit) for digit in str(num)]
#     count = sum(1 for x in arr_num)
#     return count


# Examples
number_length(10)  # ➞ 2

number_length(5000)  # ➞ 4

number_length(0)  #➞ 1