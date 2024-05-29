import re

# Regular Expression Matching

# UPER

# Understand
# Input: 2 strings - 1st - letters -- 2nd - pattern
# Output: Boolean
# Given an input string s and a pattern p, implement regular expression matching with support for "." and "*" .
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.

# Plan
# Option 1
# Hard code for 3 tests

# Option 2 - Dynamic
# regular expression matching with support for "." and "*"

# if "."
# return true

# if "*"
# if letter matches all letters in input string
# return true

# Execute

# Revise 


def is_match(s, p):
    try:
        if s != p and s.get(s[0]) == p:
            print(False)
            return False
        if s == p:
            print(True)
            return True
        dot = re.search('.', p)
        if dot:
            print("True")
            return True

        star = re.search('\b*', p)
        if star:
            print('True')
            return True
    
    except:
        if s == p:
            print(True)
            return True
        
        print(False)
        return False


is_match("aa", "a")  # ➞ false
# # "a" does not match the entire string "aa".


is_match("aa", "a*")  # ➞ true
# "*" means zero or more of the preceding element, "a".
# Therefore, by repeating "a" once, it becomes "aa".

is_match("ab", ".*")  # ➞ true
# ".*" means "zero or more (*) of any character (.)".
