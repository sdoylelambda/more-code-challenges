# Create a Stair

# Write a function which takes an integer steps and returns a string representing an 
# upward stair with steps representing the number of the steps in the stair. 
# Each step will be represented by combinations of underscore(s), newline(s), and vertical line(s).

# So, if you print the result for a stair with three steps, it will look something like this:

#       _
#     _|
#   _|
# _|

# UPER

# Understand
# Input: int - num of steps
# Output: str - with steps
# All steps are '_|' except the top '_'
# For zero, return ___ (three underscores).
# Since the stair is upward, the beginning of the code is the top of the stair.
# Start with last step first.
# All numbers are positive.
# A step is 2 lines - _| + next or top step


# Plan
# Option 1
# variables for step new line and top step
# var for num of spaces starting with total number of spaces -2 each time
# output += spaces_var + last step
# loop
# output += spaces_var + step plus 
# return output

# Option 2
# output += spaces_var + last step
# Recursion
# while len > 0:
# output += spaces + stair

# Execute

# Revise

def stair(steps):
	# variables for step new line and top step
    output = ''
    top_step = '_'
    step = '_|'
    new_line = '\n'
    num_of_spaces = steps * 2 

    # var for num of spaces starting with total number of spaces -2 each time
    spaces = ' ' * int(num_of_spaces)
    print(spaces)

    output += spaces + top_step + new_line
    # loop
    while len(range(steps)) > 0:
        output += spaces + step + new_line
        num_of_spaces = steps - 2 
        print('spaces:', num_of_spaces)
        spaces = ' ' * int(num_of_spaces)
        steps -= 1
    # return output
    print('output', output)

# stair(1)   # ➞ "  _\n_|"
# 2 spaces, 1 underscore, 1 newline, 1 underscore, 1 vertical line

stair(2)   # ➞ "    _\n  _|\n_|"
# # 4 spaces, 1 undescore, 1 newline, 2 spaces, 1 underscore,
# # 1 vertical line, 1 newline, 1 underscore, 1 vertical line

# stair(3)  # ➞ "      _\n    _|\n  _|\n_|"
# # 6 spaces, 1 undescore, 1 newline, 4 spaces, 1 underscore,
# # 1 vertical line, 1 newline, 2 spaces, ...

# stair(4)  # ➞ "        _\n      _|\n    _|\n  _|\n_|"
# # 8 spaces, 1 undescore, 1 newline, 6 spaces, 1 underscore,
# # 1 vertical line,  ...
