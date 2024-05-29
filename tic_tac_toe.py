# Tic Tac Toe

# Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is a win for 
# "X", "O", or a "Draw", where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot.
# Make sure that if O wins, you return the letter "O" and not the integer 0 (zero) and if it's a draw, 
# make sure you return the capitalised word "Draw". If you return "X" or "O", make sure they're capitalised too.

# UPER

# Understand
# Input: Matrix
# Output: "X" or "O" or "Draw"
# See if either X or O has 3 in a row
# Return the winner or Draw
# 3 in a row verticle
# 3 in a row horizontal
# 3 in a row diagnal

# Plan
# Option 1
# Check top left value
# See if value to right or below is the same
# If so proceed
# If not
# Check middle top value
# See if value below is the same
# If so proceed
# If not
# check top 3rd value
# check to see if value below is the same
# If so proceed
# If not
# Check middle first value
# See if value to the right is the same
# If so proceed
# If not
# (diagnal)
# check top first value
# see if middle value the same
# if not 
# check top right value
# see if middle the same
# check bottom left see if the same
# Return output

# Option 2
# for 3 loops
# check for possible wins
# position[0] all = X or Y
# position[1] all = X or Y
# position[2] all = X or Y
# if not return "Draw"


def tic_tac_toe(board):
    first_line = board[0]
    second_line = board[1]
    third_line = board[2]

    # Left vertical, middle vertical, right vertical
    # Horizontal top, middle, bottom
    # Diagnals both directions
    if first_line[0] == 'X' and second_line[0] == 'X' and third_line[0] == 'X' or \
        first_line[1] == 'X' and second_line[1] == 'X' and third_line[1] == 'X' or \
        first_line[2] == 'X' and second_line[2] == 'X' and third_line[2] == 'X' or \
        first_line[0] == 'X' and first_line[1] == 'X' and first_line[2] == 'X' or \
        second_line[0] == 'X' and second_line[1] == 'X' and second_line[2] == 'X' or \
        third_line[0] == 'X' and third_line[1] == 'X' and third_line[2] == 'X' or \
        first_line[0] == 'X' and second_line[1] == 'X' and third_line[2] == 'X' or \
        first_line[2] == 'X' and second_line[1] == 'X' and third_line[0] == 'X':
        print('return: X')
        return 'X'

    if first_line[0] == 'O' and second_line[0] == 'O' and third_line[0] == 'O' or \
        first_line[1] == 'O' and second_line[1] == 'O' and third_line[1] == 'O' or \
        first_line[2] == 'O' and second_line[2] == 'O' and third_line[2] == 'O' or \
        first_line[0] == 'O' and first_line[1] == 'O' and first_line[2] == 'O' or \
        second_line[0] == 'O' and second_line[1] == 'O' and second_line[2] == 'O' or \
        third_line[0] == 'O' and third_line[1] == 'O' and third_line[2] == 'O' or \
        first_line[0] == 'O' and second_line[1] == 'O' and third_line[2] == 'O' or \
        first_line[2] == 'O' and second_line[1] == 'O' and third_line[0] == 'O':
        print('return: O')
        return 'O'
    
    return 'Draw'


# def tic_tac_toe(board):
# 	k=['O','X']
# 	y=[]
# 	for i in board:
# 		for j in i:
# 			y.append(j)
# 	s=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
# 	for l in k:
# 		for i in s:
# 			t=0
# 			for j in i:
# 				if(y[j]==l):
# 					t+=1
# 			if(t==3):
# 				return l
# 	return 'Draw'

























    # for 3 loops
    # for position in board:
    #     print('position', position)
    #     # check for possible wins
    #     if position[0] == 'X':
    #         print('yes') 
        # position[1] all = X or Y
        # position[2] all = X or Y
        # if not return "Draw"
    























# tic_tac_toe([
#   ["X", "O", "X"],
#   ["O", "X",  "O"],
#   ["O", "X",  "X"]
# ])  # ➞ "X"

tic_tac_toe([
  ["O", "O", "O"],
  ["O", "X", "X"],
  ["E", "X", "X"]
])  # ➞ "O"

# tic_tac_toe([
#   ["X", "X", "O"],
#   ["O", "O", "X"],
#   ["X", "X", "O"]
# ])  # ➞ "Draw"

