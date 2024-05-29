# Underscore-Hash Staircase

# Create a function that will build a staircase using the underscore _ and hash # symbols. 

# UPER

# Understand
# Input: Number - positive or negative values.
# Output: String
# Positive - Upward direction  
# Negative - Downwards - reversed()
# Add \n after each set ~ loop add('\n')
# Solve without recursion
#   _ = empty stace
#   # = part of stairs

# Plan
# Option 1
# for stair in range(input):
# underscore = ''
# hashes = input
# output += hashes
# output += '\n'
# hashes -= 1 - .remove(-1)
# loop continue
# if hashes < input:
#   underscore += '_'
#   output += underscore
# return output


def staircase(n):
    output = ''
    underscore = ''
    hashes = ''
    while range(n) > 0:
        output += '#' * n
        output += '\n'
        hashes[0: -1]
        print('stair', hashes)

        if len(hashes) < n:
            underscore += '_'
            output += underscore
            print('hashes', output)

    print('output', output)
    return output


staircase(3)  # ➞ "__#\n_##\n###"
# __#
# _##
# ###

# staircase(7)  # ➞ "______#\n_____##\n____###\n___####\n__#####\n_######\n#######"
# ______#
# _____##
# ____###
# ___####
# __#####
# _######
# #######

# staircase(2)  # ➞ "_#\n##"
# _#
# ##

# staircase(-8)  # ➞ "########\n_#######\n__######\n___#####\n____####\n_____###\n______##\n_______#"
# ########
# _#######
# __######
# ___#####
# ____####
# _____###
# ______##
# _______#

