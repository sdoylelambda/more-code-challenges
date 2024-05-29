# The Karaca's Encryption Algorithm

# Make a function that encrypts a given input with these steps:



# UPER

# Understand
# Input: string - All inputs are strings, no uppercases and all output must be strings.
# Output: string
# Input: "apple"
# Step 1: Reverse the input: "elppa"
# Step 2: Replace all vowels using the following chart:

# a => 0
# e => 1
# i => 2
# o => 2
# u => 3

# # "1lpp0"
# Step 3: Add "aca" to the end of the word: "1lpp0aca"

# Output: "1lpp0aca"

# Plan
# Option 1
# reverse input string - .reverse()
# replace vowels with dict values
# for letter in input:
# if letter in dict:
# return value
# add 'aca' to the end


# def encrypt(word):
#     vowels = {
#         'a': 0,
#         'e': 1,
#         'i': 2,
#         'o': 2,
#         'u': 3,
#     }
#     output = ''
#     word = reversed(word)
#     for letter in word:
#         if letter in vowels:
#             letter = vowels.get(letter)
#         output += str(letter)

#     output += 'aca'
#     return output

def encrypt(word):
	word = word[::-1]
	for r in (("a", "0"), ("e", "1"), ("o", "2"), ("u", "3")):
		word = word.replace(*r)
		
	return word+'aca'


encrypt("banana")  # ➞ "0n0n0baca"

encrypt("karaca")  # ➞ "0c0r0kaca"

encrypt("burak")  # ➞ "k0r3baca"

encrypt("alpaca")  # ➞ "0c0pl0aca"

