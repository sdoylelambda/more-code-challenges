# The Snake — Area Filling

# This challenge is based on the classic videogame "Snake".

# Assume the game screen is an n * n square, and the snake starts the game with length 1 (i.e. just the head) positioned on the 
# top left corner.

# For example, if n = 7 the game looks something like this:

# In this version of the game, the length of the snake doubles each time it eats food 
# (e.g. if the length is 4, after eating it becomes 8).

# Create a function that takes the side n of the game screen and returns the number of times the snake can eat before it runs 
# out of space in the game screen.

# UPER

# Understand
# Input: 1 number 
# Output: 1 number - times worm eats
# Side of board x self = total board size (n*n)
# Snake size 1 then doubles each time - 1, 2, 4, 8, 16, 32, ...900
# Return max snake size that is not above board size

# The given number will always be a positive integer (there are no exceptions to handle).


# Plan
# Option 1 
# board_size = n*n
# helper(): 
# return snake_size
# if snake_size > board_size
# run until larger
# return previous

# Option 2
# board_size = n*n
# while snake_size > board_size
# run until larger
# return previous

# Execute

# Revise


# def snakefill(n):
# 	board_size = n*n
# 	snake_size = 1
# 	count = 0
# 	print(snake_size, board_size)
# 	while snake_size < board_size:
# 		next_size = snake_size * 2
# 		print('next', next_size, board_size)
# 		if next_size > board_size:
# 			print('count:', count)
# 			return count
# 		if next_size == board_size:
# 			print('count:', count + 1)
# 			return count + 1
# 		snake_size = next_size
# 		count += 1
# 	print(count)
# 	return count


def snakefill(n):
	board_size = n*n
	snake_size = 1
	count = 0
	while snake_size < board_size:
		next_size = snake_size * 2
		if next_size > board_size:
			return count
		if next_size == board_size:
			return count + 1
		snake_size = next_size
		count += 1
	return count

# snakefill(3)  # ➞ 3

# snakefill(6)  # ➞ 5

# snakefill(24)  # ➞ 9

snakefill(1)  # ➞ 0

# snakefill(8)  # ➞ 6