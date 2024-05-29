# Parentheses Clusters

# Write a function that groups a string into parentheses clusters. Each cluster should be balanced.

# All input strings will only contain parentheses.

# Balanced: Every opening parens ( must exist with its matching closing parens ) in the same cluster.

# UPER

# Understand - Split string into list seperated by balanced clusters.
# Input: string
# Output: list of strings
# Balanced - Inner most closed parantheses, then potentially with an equal number of matching parantheses.

# Plan
# Option 1 
# Look thru input string
# Find "()"
# Check if any additional outer parantheses "(())"
# Append matching_parantheses to output list
# Remove matching_parantheses  
# Continue checking string and repeat
# When the entire string is checked, return output

# Execute 

# Revise 



def split(txt):
    txt_list = list(txt.strip())
    left_count = 0
    right_count = 0
    output_list = []
    temp_string = ''

    while len(txt_list) > 0:
    
        if txt_list[0] == '(':
            left_count += 1
            temp_string += '('
            txt_list.pop(0)

        if txt_list[0] == ')':
            right_count += 1
            temp_string += ')'
            txt_list.pop(0)

        



















def split(txt):
    txt_list = list(txt.strip())
    print(txt_list)
    output_list = []

    while len(txt_list) > 0:
        left_value = ''
        right_value = ''
        x = txt_list.pop(0)
        if x == '(':
            left_value += x
        else:
            right_value += x

        y = txt_list.pop(0)
        if y == '(':
            left_value += x
        else:
            right_value += x

    print("end", right_value, left_value)


split("()()()")  # ➞ ["()", "()", "()"]






































    # if '()' in txt:
    #     print('yes')


    # Look thru input string
    # count = 0
    # for t in txt:
    #     if txt_list[t] == '(' and txt_list[t + 1] == ')':
    #         print(True)


    # Check if any additional outer parantheses "(())"
    # Append matching_parantheses to output list
    # Remove matching_parantheses  
    # Continue checking string and repeat
    # When the entire string is checked, return output




# split("((()))")  # ➞ ["((()))"]

# split("((()))(())()()(()())")  # ➞ ["((()))", "(())", "()", "()", "(()())"]

# split("((())())(()(()()))")  # ➞ ["((())())", "(()(()()))"]

# split("")  # ➞ []

