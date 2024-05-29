# Matrix Multiplication

# Create a function that multiplies two matricies (n x n each).
# Limit to 2 x 2 matricies.

# UPER
# Input: List of lists with 2 and 2 inner most with 2 values - [[x, x],[x, x]], [[x, x], [x, x]]
# Output: List of lists with 2 inner lists with 2 values - [[x, x], [x, x]]
# Matrix Breakdown:
# matrix_mult(
#[[4, 2]    [[5, 6], === 
#,[3, 1]],  [3, 8]]) ===
#                ➞ [[26, 40], [18, 26]]


# matrix = [[a, b], [c, d]], [[e, f], [g, h]]
# test_1 = [[4, 2], [3, 1]], [[5, 6], [3, 8]]

# equation = [[a * e] + [b * g], [a * f] + [b * h]], [[c * e] + [d * g], [c * f] + [d * h]]
# test_one = [[4 * 5] + [2 * 3], [4 * 6] + [2 * 8]], [[3 * 5] + [1 * 3], [3 * 6] + [1 * 8]]
# breakdown = 
# w = [a * e] + [b * g]
# x = [a * f] + [b * h]
# y = [c * e] + [d * g]
# z = [c * f] + [d * h]
#
# answer_mat = [w, x] [y, z]
# answer_one = [26, 40], [18, 26]

# Plan
# Option 1
# create output list
# Declare input as matrix above
# run equation breakdown
# return output

# Option 2
# create output list
# For loops pull out values
# a-h
# run equation
# return output




# def matrix_mult(m1, m2):
# 	# create output list
	
#     # Declare input as matrix above
# 	# print(m1[0])
# 	a = m1[0][0]
# 	b = m1[0][1]
# 	c = m1[1][0]
# 	d = m1[1][1]
# 	e = m2[0][0]
# 	f = m2[0][1]
# 	g = m2[1][0]
# 	h = m2[1][1]

#     # run equation breakdown
# 	first_equation = [a * e], [b * g]  # , [a * f] + [b * h]], [[c * e] + [d * g], [c * f] + [d * h]]
# 	first_value = first_equation[0] + first_equation[1]
# 	print(sum(first_value))
# 	second_equation = [a * f] + [b * h]  #], [[c * e] + [d * g], [c * f] + [d * h]]
# 	second_value = second_equation[0] + second_equation[1]
# 	print(second_value)
# 	third_equation = [c * e] + [d * g] #, [c * f] + [d * h]]
# 	third_value = third_equation[0] + third_equation[1]
# 	print(third_value)
# 	forth_equation = [c * f] + [d * h]
# 	forth_value = forth_equation[0] + forth_equation[1]
# 	print(sum(forth_equation))
# 	output_matrix = [[sum(first_value), second_value], [third_value, forth_value]]
# 	print(output_matrix)
# 	return output_matrix

	# for time_to_add in equation:
	#     print(time_to_add)
    # return output





# def matrix_mult(m1, m2):
	# matrix = [[a, b], [c, d]], [[e, f], [g, h]]
	# a = m1[0][0]
	# b = m1[0][1]
	# c = m1[1][0]
	# d = m1[1][1]
	# e = m2[0][0]
	# f = m2[0][1]
	# g = m2[1][0]
	# h = m2[1][1]
	# output_matrix = [a * e + b * g, a * f + b * h], [c * e + d * g, c * f + d * h]
	# print(output_matrix)
	# first_equation = [a * e], [b * g]
	# first_value = first_equation[0] + first_equation[1]
	# second_equation = [a * f] + [b * h]
	# second_value = second_equation[0] + second_equation[1]
	# third_equation = [c * e] + [d * g]
	# third_value = third_equation[0] + third_equation[1]
	# forth_equation = [c * f] + [d * h]
	# forth_value = forth_equation[0] + forth_equation[1]
	
	# output_matrix = [[sum(first_value), second_value], [third_value, forth_value]]
	# return output_matrix

def matrix_mult(m1, m2):
    [[e, f],[g, h]], [[a, b], [c, d]] = m1, m2
    print(m1)
    return [[a*e + c*f, b*e + d*f], [a*g + c*h, b*g + d*h]]
	

# Examples
matrix_mult([[4, 2],[3, 1]], [[5, 6], [3, 8]]) 
#                ➞ [[26, 40], [18, 26]]

# matrix_mult([[3, 6],[4, 5]], [[8, 1], [7, 2]]) 
#                ➞ [[66, 15], [67, 14]]

# matrix_mult([[7, 5],[2, 2]], [[6, 7], [3, 2]]) 
#                ➞ [[57, 59], [18, 18]]


































# def matrix_mult(m1, m2):
# 	# create output list
# 	output_matrix = []
#     # Declare input as matrix above
# 	print(m1[0])
#     # for m in m1:
# 	# 	for n in range(len(m)):
# 	# 	    print(n) 
# 	# matrix = [[a, b], [c, d]], [[e, f], [g, h]]
#     # run equation breakdown
#     # return output