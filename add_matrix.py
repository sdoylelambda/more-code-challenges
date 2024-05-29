# Add the Values of the Symbols in a Matrix
# Write a function that takes a list of lists and returns the value of all of the symbols in it, where each symbol adds or takes something from the total score. Symbol values:

# # = 5
# O = 3
# X = 1
# ! = -1
# !! = -3
# !!! = -5
# A list of lists containing 2 #s, a O, and a !!! would equal (0 + 5 + 5 + 3 - 5) 8.

# If the final score is negative, return 0 

# Strings in the lists will only be #, O, X, !, !! and !!!.

# UPER

# Understand 
# input: list of lists
# ouput: number 0 or greater
# check_score([
#   ["#", "!"],   -> [5, -1]
#   ["!!", "X"]   -> [-3, 1]
# ]) 5 - 1 - 3 + 1 = ➞ 2

# Plan
# Option 1:
# Create dictonary where keys are the symbol and values are the value associated
# Create output list 
# Loop thru each list 
# Loop thru nexted list
# convert each value to numaric and append to output list
# Return with sum(output_list)
# If less than 0 return 0

# Opttion 2 - Convert to one output array

# OPtion 3 - Split join

# Execution

# def check_score(s):
#     print('START ---------------------------------->')
#     # Create dictonary where keys are the symbol and values are the value associated
#     symbol_values = { '#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5 }
#     # Create output list 
#     output_list = []
#     # Loop thru each list 
#     for list in s:
#         # Loop thru nexted list
#         for nested_list in list:
#             # convert each value to numaric and append to output list
#             value_of_symbol = symbol_values.get(nested_list)
#             output_list.append(value_of_symbol)

#     print(output_list)
#     # Return with sum(output_list)
#     output_value = sum(output_list)
#     # If less than 0 return 0
#     if output_value < 0:
#         print('OUTPUT: 0   :D')
#         return 0
    
#     print('OUTPUT:', output_value)
#     return output_value

# Revise

def check_score(s):
    symbol_values = { '#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5 }
    output_list = []
    for list in s:
        for nested_list in list:
            value_of_symbol = symbol_values.get(nested_list)
            output_list.append(value_of_symbol)

    output_value = sum(output_list)
    if output_value < 0:
        return 0
    
    return output_value


check_score([
  ["#", "!"],
  ["!!", "X"]
])  # ➞ 2

check_score([
  ["!!!", "O", "!"],
  ["X", "#", "!!!"],
  ["!!", "X", "O"]
])  # ➞ 0

check_score([
  ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
  ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
  ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
  ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
  ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
  ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
  ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
  ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
  ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
  ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
  ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
  ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
  ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
  ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
])  # ➞ 12
