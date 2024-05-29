# Concert Seats
# Create a function that determines whether each seat can "see" the front-stage. 

# A number can "see" the front-stage if it is strictly greater than the number before it.

# Everyone can see the front-stage in the example below:

# # FRONT STAGE
# [[1, 2, 3, 2, 1, 1],
# [2, 4, 4, 3, 2, 2],
# [5, 5, 5, 5, 4, 4],
# [6, 6, 7, 6, 5, 5]]

# # Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
# # 6 > 5 > 4 > 2 - so all numbers can see, etc.
# Not everyone can see the front-stage in the example below:

# # FRONT STAGE
# [[1, 2, 3, 2, 1, 1], 
# [2, 4, 4, 3, 2, 2], 
# [5, 5, 5, 10, 4, 4], 
# [6, 6, 7, 6, 5, 5]]

# # The 10 is directly in front of the 6 and blocking its view.
# The function should return True if every number can see the front-stage, and False if even a single number cannot.

# # Number must be strictly smaller than 
# # the number directly behind it.

# Numbers must be strictly greater than the number in front of it.
# All numbers within the lists will be whole numbers greater than or equal to zero.

# UPER

# Understand 
# input: 3-4 lists of veriying length
# output: bool
# return True if every number can see the front-stage, else False
# To see the stage the seat must have a larger number then all seats in front of it

# Plan
# Option 1
# 4 nested loops 
# Compare value of each position
# if any following loops positions are smaller
# return False

# Option 2
# Find length of the lists
# return False


# def can_see_stage(seats):
#     # Find length of the lists
#     for row in seats:
#         # loop thru each list
#         print('ROW:', row)
#         seat_value = 0
#         for position in len(seats):
#         # if any following loops positions are smaller
#             print('position', position)
#             if row[position] < seat_value:
#                 print('RETURN FALSE')
#                 return False

#     return True

def can_see_stage(seats):
    row_value_list = []
    for row in seats:
        # print('row', row)
        print('row_value_list', row_value_list)
        count = 0
        for seat in row:
            # print('seat', seat)
            row_value_list.append(seat)
            print('row[count], seat:', row[count], seat)
            count += 1

    
            for x in range(count):
                print('x', x)
                if row_value_list[x] > seat:
                    print('row_value_list', row_value_list[x], seat)
                    print('Return False')
                    return False
        
        
        
        row_value_list = []    
        

    # print('row_value_list', row_value_list)

    print('Return True')
    return True


# Examples

# can_see_stage([
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ])  # ➞ True

# can_see_stage([
#   [0, 0, 0],
#   [1, 1, 1],
#   [2, 2, 2]
# ]) ➞ True

# can_see_stage([
#   [2, 0, 0], 
#   [1, 1, 1], 
#   [2, 2, 2]
# ])  # ➞ False

# can_see_stage([
#   [1, 0, 0],
#   [1, 1, 1],
#   [2, 2, 2]
# ]) ➞ False

can_see_stage(
[[1, 2, 2], 
[1, 2, 3], 
[4, 4, 4]])