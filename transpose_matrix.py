# Enter the Matrix

# In this challenge, you have to obtain a sentence from the elements of a given matrix. 
# In the matrix, each word of the sentence follows a columnar order from the top to the bottom, 
# instead of the usual left-to-right order: it's time for transposition!

# Given a matrix mtx, implement a function that returns the complete sentence as a string, 
# with the words separated by a space between them.

# All given matrices are regular, as to say that each column has the same length.
# Punctuation is already given, you just have to add the spaces in the returned string.

def transpose_matrix(mtx):
    str = ""
    print(str.join(mtx))


transpose_matrix([
  ["Enter"],
  ["the"],
  ["Matrix!"]
])  #➞ "Enter the Matrix!"

# transpose_matrix([
#   ["The", "are"],
#   ["columns", "rows."]
# ]) ➞ "The columns are rows."

# transpose_matrix([
#   ["You", "the"],
#   ["must", "table"],
#   ["transpose", "order."]
# ]) ➞ "You must transpose the table order."
