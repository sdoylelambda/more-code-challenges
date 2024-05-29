# Atbash Cipher
# The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.

# Create a function that takes a string and applies the Atbash cipher to it.

# Capitalisation should be retained.

# Non-alphabetic characters should not be altered.

import string


def atbash(txt):
    output_str = ''
    alphebet = list(string.ascii_lowercase)
    reverse_alphebet = list(string.ascii_lowercase)
    reverse_alphebet.reverse()

    for char in txt:
         # If value is upper case make lower case
        upper_cased_value = False
        if char.isupper():
            upper_cased_value = True
            char = char.lower()

        # If not letter return char
        if char not in alphebet and char not in reverse_alphebet:
            output_str += char

        # Get letters position to add reverse letter
        count = 0
        for letter in alphebet:
            if letter == char:
                value_to_add = reverse_alphebet[count]
                if upper_cased_value:
                    value_to_add = value_to_add.upper()

                output_str += value_to_add
                break
            count += 1

    return output_str



# atbash("apple")  # ➞ "zkkov"

atbash("Hello world!")  # ➞ "Svool dliow!"

# atbash("Christmas is the 25th of December")  # ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"

# UPER

# Understand - Reverse the string letters positions. Case sensitive
# INPUT: string
# OUTPUT: string

# Plan - 

# Option 1 
# have 4 lists.
# 1st - a-z
# 2nd - z-a
# 3rd - A-Z
# 4th - Z-A
# if not letter return char
# get letters position 
# return letters reverse position value

# Option 2 
# have 2 lists.
# 1st - a-z
# 2nd - z-a
# if not letter return char
# if value is upper case make lower case - (return upper case)
# get letters position 
# return letters reverse position value

            
