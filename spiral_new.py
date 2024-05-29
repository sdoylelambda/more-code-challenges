# Spiral Matrix

# In this challenge, transform a string into a spiral contained inside a regular square matrix. 
# To build the matrix, you are given the dimension of its side:

# If the side of the matrix is odd, the spiral starting point will be the exact center of the matrix.
# If the side of the matrix is even, the spiral starting point will be placed in the lower columns half of the lower rows half.
# # "x" represents the matrix center

# side = 3 (odd)
# matrix = [
#   [" ", " ", " "],
#   [" ", "x", " "],
#   [" ", " ", " "]
# ]

# side = 4 (even)
# matrix = [
#   [" ", " ", " ", " "],
#   [" ", "x", " ", " "],
#   [" ", " ", " ", " "],
#   [" ", " ", " ", " "],
# ]
# The length of the string has to match exactly the number of cells inside the matrix:

# If the string length is greater than the number of cells, you have to cut off the unnecessary characters.
# If the string length is lower than the number of cells, you have to add a series of "+" to the end of the string 
# until its length match the number of cells.
# side = 3 (9 cells)
# string = "EDABITTEROUS"
# # You'll need only "EDABITTER", while "OUS" is discarded.
# string = "EDABITTER"

# side = 4 (16 cells)
# string = "EDABITTEROUS"
# # You'll need all the string plus 4 "+" to match the cells.
# string = "EDABITTEROUS++++"

# Starting from the center that you found, you have to fill a regular square matrix side * side placing the characters of the 
# given string str, following a clockwise spiral pattern (first move to the right).

# side = 3 (odd)
# string = "EDABITTEROUS"
# matrix = [
#   ["T", "E", "R"],
#   ["T", "E", "D"],
#   ["I", "B", "A"]
# ]
# matrix_aka = [
#   ["7", "8", "9"],
#   ["6", "1", "2"],
#   ["5", "4", "3"]
# ]

# side = 4 (even)
# string = "EDABITTEROUS"
# matrix = [
#   ["T", "E", "R", "O"],
#   ["T", "E", "D", "U"],
#   ["I", "B", "A", "S"],
#   ["+", "+", "+", "+"],
# ]
# matrix_aka = [
#   ["7", "8", "9", "0"],
#   ["6", "1", 2", "11"],
#   ["5", "4", "3", "12"],
#   ["16", "15", "14", "13"],
# ]

# Remember, the first move from the center is to the right, and then you proceed clockwise and concentrically.
# As given side, you can expect any valid value greater than 1.

# UPER

# Understand - Create lists with size and count equal to 'side' passed in with letters from string starting at center going clockwise
# Input: 
# 1. number - of lists with same number of values
# 2. string - all caps - values to be passed in above
# Output: - list of lists with input string starting at center going clockwise
# If string has move values than alotted, remove extra chars
# If string has less values than alotted, add "+"
# Use double quotes for output

# If even number of values
# Start up and right from middle
# Then go right
# Then go down
# Then go left twice
# Then up twice
# Then right twice - Three if can - += here
# Repeat with plus 1 from above

# If odd number of values
# Add string chars starting with the center
# Then go right
# Then go down
# Then go left twice
# Then up twice
# Then right twice - Three if can - += here
# Repeat with plus 1 from above


# Plan

# Option 1
# Create x empty list of lists
# Update input string to final length of values
# Find center
# Add string chars starting with the center
# Then go right
# Then go down
# Then go left twice
# Then up twice
# Then right twice - Three if can - += here
# Repeat with plus 1 from above





def create_empty_output_lists(side: str) -> list:
    output = []
    for count in range(side):
        output.append(list(range(side)))

    return output


def enrich_input_string(string: str, output) -> str:
    count = len(output) * len(output)
    while len(string) > count:
        string = string[:-1]

    while len(string) < count:
        string += "+"

    return string

def find_center(output):
    a = ''
    output_center = output
    output_center[a] += [a]
    print("output_center", output_center)

    return output_center



def spiral_matrix(side: int, string: str) -> list:

    output = create_empty_output_lists(side)
    # output[0][0] = "B"

    # Update input string to final length of values
    enriched_string = enrich_input_string(string, output)
    print("enriched_string", enriched_string)

    # Find center
    center = find_center(output)
    # position = center
    
    # Add string chars starting with the center
    center = string.pop()
    print('center pop:::::', center)
    # Then go right
    # Then go down
    # Then go left twice
    # Then up twice
    # Then right twice - Three if can - += here
    # Repeat with plus 1 from above
    print(output)
    return output


# spiral_matrix(2, "DOG")  # ➞ [
#   ["D", "O"],
#   ["+", "G"]
# ]

spiral_matrix(3, "COPYRIGHTS")  # ➞ [
#   ["G", "H", "T"],
#   ["I", "C", "O"],
#   ["R", "Y", "P"]
# ]

# spiral_matrix(4, "SUPERLUMBERJACK")  # ➞ [
#   ["U", "M", "B", "E"],
#   ["L", "S", "U", "R"],
#   ["R", "E", "P", "J"],
#   ["+", "K", "C", "A"]
# ]

# spiral_matrix(6, "SHESELLSSHELLSBYTHESEASHOREWITHOUTASHELLSSELLINGLICENSE")  # ➞ [
#   [ "E", "A", "S", "H", "O", "R" ],
#   [ "S", "L", "S", "S", "H", "E" ],
#   [ "E", "L", "S", "H", "E", "W" ],
#   [ "H", "E", "S", "E", "L", "I" ],
#   [ "T", "Y", "B", "S", "L", "T" ],
#   [ "S", "A", "T", "U", "O", "H" ]
# ])
