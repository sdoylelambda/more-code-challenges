# A Circle and Two Squares

# Imagine a circle and two squares: a smaller and a bigger one.

# Create a function, that takes an integer (radius of the circle) and returns the difference of the
# areas of the two squares.

# Uses only positive integer parameters.


# UPER

# Understand
# input: radius of the circle
# output: the difference of the areas of the two shapes.

# Plan
# Determine area of the circle - PieR^2
# Determine area of the square - A=4×r^2
# Subtract square area from circle area and return

# Execute
# Option 1
# circle_area = PieR^2
# square_area = A=4×r^2
# return circle_area - square_area

# Revise

import math


def square_areas_difference(r):
    return 2 * r ** 2


# Examples
square_areas_difference(5)  # ➞ 50

# square_areas_difference(6)  # ➞ 72

# square_areas_difference(7)  # ➞ 98
