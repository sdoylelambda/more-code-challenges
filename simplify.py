import re

# Simplified Fractions

# Create a function that returns the simplified version of a fraction.

# UPER

# Understand
# Input: str - num/num
# Output:str - num/num - or whole num as str
# A fraction is simplified if there are no common factors (except 1) between the numerator and the denominator. 
# For example, 4/6 is not simplified, since 4 and 6 both share 2 as a factor.
# If improper fractions can be transformed into integers, do so in your code (see example #4).

# Plan
# Option 1
# a = get number until slash
# b = get number after slash

# if b / a == num > 0 
# return b / a

# recursive
# a / 2 == whole number proceed = a
# b / 2 == whole number proceed = b
# if not whole number
# return "a/b"

# Execute

# Revise


# def simplify(txt):
#     # a = get number until slash
#     a, b = re.findall('\d+', txt)
#     # x, y = txt.split('/')
#     print(a, b)

    # first_number = []
    # second_number = []
    # for num in a:
    #     first_number.append(num[0])
    #     a.pop(0)
    #     second_number.insert(len(a), num[a[len(a)]])
    #     a.pop(-1)
    # print(first_number, second_number)
    # b = get number after slash
    # b = re.search()
    # if b / a == num > 0 
    # return b / a

    # recursive
    # a / 2 == whole number proceed = a
    # b / 2 == whole number proceed = b
    # if not whole number
    # return "a/b"


def divide_nums(a, b):
    if a % 2 == 0 and b % 2 == 0:
        x = a / 2
        y = b / 2
        print('updated:', x, y)
        divide_nums(x, y)
    # if a % b > 0:
    #     a = 
    print('divide_nums:', a, b)
    return a, b
    

def simplify(txt):
    # a, b = get numbers split by slash
    a, b = re.findall('\d+', txt)
    # print(a, b)
    if a > b:
        i = int(a) / int(b)
        print('i', i)
        return i
    # x, y = txt.split('/')
    
    # recursive
    t, y = divide_nums(int(a), int(b))
    print('output:', int(t), int(y))

# simplify("4/6")  # ➞ "2/3"

# simplify("10/11")  # ➞ "10/11"

simplify("100/400")  # ➞ "1/4"

# simplify("8/4")  # ➞ "2"
