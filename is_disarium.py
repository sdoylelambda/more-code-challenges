# Disarium Number

# A number is said to be Disarium if 
# the sum of its digits raised to their respective positions is the number itself.

# Create a function that determines whether a number is a Disarium or not.

# Position of the digit is 1-indexed.
# A recursive version of this challenge can be found via this link.

# UPER

# Understand
# Input: num
# Output: bool
# For each digit in the input number, 
# x = Each digit to the power of 1 (+1 each itteration)
# add all x's together == input number
# return True
# else False

# Plan
# Option 1
# temp = []
# For num in n:
# temp.append(num^1) 
# 1 += 1
# add temp values together
# if that equals input
# return True
# else return false

# Option 2
# split n into list
# while list has length
# x = list.pop(1)
# x^1
# temp.append(num^1) 
# 1 += 1
# add temp values together
# if that equals input
# return True
# else return false


# def is_disarium(n):
#     n_list = list(str(n))
#     temp = []
#     power = 1
#     for num in n_list:
#         temp.append(int(num) ** power) 
#         power += 1

#     total = sum(temp)
#     if total == n:
#         return True
    
#     return False


def is_disarium(n):
    r = 0
    for i in range(len(str(n))):
        r += int(str(n)[i]) ** (i + 1)
    print(r == n)
    return r == n


# is_disarium(75)  # ➞ False
# 7^1 + 5^2 = 7 + 25 = 32

is_disarium(135)  # ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

is_disarium(544)  # ➞ False

is_disarium(518)  # ➞ True

is_disarium(466)  # ➞ False

is_disarium(8)  # ➞ True
