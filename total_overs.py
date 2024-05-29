# Cricket Balls to Overs!

# In cricket, an over consists of six deliveries a bowler bowls from one end.

# Create a function that takes the number
# of balls bowled by a bowler and calculates the
# number of overs and balls bowled by him/her.

# The number following the decimal point represents the balls remaining after the last over. Therefore, it will only
# ever have a value of 1-5.

# Return the value as a
# float, in the format overs.balls.


# UPER

# Understand
# Input: number
# Output: number - float
# The output is in a.b format always.
#   a = overs - ? what is equation? input / 6
#   b = number 0-5 - balls remaining after the last over

# Plan

# Option 1
# a = input / 6
# b = remainder divided by 6


# Execute
#

# Revise


def total_overs(balls):
    a = int(balls) / 6
    b = a % 6
    print('a', a)
    print('b', b)
    print(a, '.', b)


# Examples

# total_overs(2400)  # ➞ 400

total_overs(164)  # ➞ 27.2
# # 27 overs and 2 balls were bowled by the bowler.

# total_overs(945)  # ➞ 157.3
# # 157 overs and 3 balls were bowled by the bowler.

# total_overs(5)  # ➞ 0.5
