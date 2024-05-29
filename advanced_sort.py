# Advanced List Sort
# Create a function that takes a list of numbers or strings and 
# returns a list with the items from the original list stored into sublists. 
# Items of the same value should be in the same sublist.
# The sublists should be returned in the order of each element's first appearance in the given list.

# UPER

# Understand - Take input list and create sub lists with same values 
# input: list
# output: list of lists

# Plan 
# Option 1
# create output list
# create placeholder value
# iterate thru list
# pop first value and make first value placeholder
# see if next is the same
# if so add it to output list
# if not 
# add to outputl list under new list
# continue checking all values then start over

output_list = []
temp_list = []

def append_list(lst, placeholder):
    for l in lst:
        print('l =======', l)
        if l == placeholder:
            # if so add it to output list
            temp_list.append(l)
            lst.remove(l)
            return lst


def advanced_sort(lst):
    while len(lst) > 0:
        placeholder = lst.pop(0)
        temp_list.append(placeholder)
        print('placeholder', placeholder)
        append_list(lst, placeholder, temp_list)

        output_list.append(temp_list)
        temp_list = []
                # temp_list.append(l)
                # continue checking all values then start over

    print('output_list', output_list)
    return output_list

# advanced_sort([2, 1, 2, 1])  # ➞ [[2, 2], [1, 1]]

advanced_sort([5, 4, 5, 5, 4, 3])  # ➞ [[5, 5, 5], [4, 4], [3]]

# advanced_sort(["b", "a", "b", "a", "c"])  # ➞ [["b", "b"], ["a", "a"], ["c"]]
