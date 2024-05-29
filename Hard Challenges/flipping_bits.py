# Flipping Bits

# You will be given a list of 32-bit unsigned integers.

# Flip all the bits 1 -> 0 and 0 -> 1 and return the result as an unsigned integer.

# Worked Example
# flipping_bits(4)  # ➞ 4294967291
# n = 4
# 4 is 0100 in binary. We are working in 32 bits so:


# 00000000000000000000000000000100 = 4
# 11111111111111111111111111111011 = 4294967291
# return 4294967291


# UPER

# Understand
# Input: Number
# Output: Number
# Take in a number.
# Convert it to 32 bit
# Flip the 1's and 0's
# Return the 32-bit new number


# Plan
# Option 1
# binary_number = convert_to_binary(n)
# flipped_num = ''
# for num in binary_number:
#   if num == 1:
#       flipped_num += '0'
#   if num == 0:
#       flipped_num += '1'
# a_dec = int(flipped_num, 2)
# return a_dec

# Option 2

# Execute

# Revise
# def flipping_bits(n):
#     binary_number = '{:032b}'.format(n)
#     flipped_binary = ''.join('0' if num == '1' else '1' for num in binary_number)
#     return int(flipped_binary, 2)


def flipping_bits(n):
    return int(''.join('0' if num == '1' else '1' for num in '{:032b}'.format(n)), 2)



# Passes All Tests
# def flipping_bits(n):
#     binary_number = '{:032b}'.format(n)
#     flipped_binary = ''
#     for num in binary_number:
#         if num == '1':
#             flipped_binary += '0'
#         if num == '0':
#             flipped_binary += '1'
#
#     flipped_num = int(flipped_binary, 2)
#     print(flipped_num)
#     return flipped_num


# Examples
flipping_bits(2147483647)  # ➞ 2147483648
flipping_bits(1)  # ➞ 4294967294
flipping_bits(4)  # ➞ 4294967291
