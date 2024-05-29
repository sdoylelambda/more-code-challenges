# Tic Tac Toe

# Create a function that takes a list of character inputs from a 
# Tic Tac Toe game. Inputs will be taken from player1 as "X", player2 as "O", 
# and empty spaces as "#". The program will return the winner or tie results.

# All inputs are valid (there will be no games where both players win).

# UPER

# Understand - 
# Input: matrix of "X" and "O" or "#"
# Output: Winner or tie
# possible_wins = 
# [[0,1], [1,1], [1, 2]] or reverse
# [[0, 0], [0,1], [0, 2]] or [+1, 0] or [+2, 0]
# [[0, 0], [1, 0], [2, 0]] or [0, +1] or [0, +2]


def tic_tac_toe(board):
    k=['O','X']
    y=[]
    for i in board:
        for j in i:
            y.append(j)
    s=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for l in k:
        for i in s:
            t=0
            for j in i:
                if(y[j]==l):
                    t+=1
            if(t==3):
                print(l)
                return l
    print('Draw')
    return 'Draw'


tic_tac_toe([
  ["X", "O", "O"],
  ["O", "X", "O"],
  ["O", "#", "X"]
])  # ➞ "Player 1 wins"


tic_tac_toe([
  ["X", "O", "O"],
  ["O", "X", "O"],
  ["X", "#", "O"]
])  # ➞ "Player 2 wins"


tic_tac_toe([
  ["X", "X", "O"],
  ["O", "X", "O"],
  ["X", "O", "#"]
])  # ➞ "It's a Tie"
