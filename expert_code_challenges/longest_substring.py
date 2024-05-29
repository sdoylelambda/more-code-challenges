# Longest Alternating Substring

# Given a string of digits, return the longest substring with alternating odd/even or even/odd digits.
 
# If two or more substrings have the same length, return the substring that occurs first.

# The minimum alternating substring size is 2, and there will always be at least one alternating substring.

# UPER

# Understand return longest substring of alternating odd/even
# Input: string of numbers
# Output: string of numbers

# Option 1
# Create substing list
# turn input into list
# loop thru input
# recursive 
# if num % 2 == 0


# def longest_substring(digits):
#     substring_list = []
#     digits_list = list(digits)
#     counter = 0

#     while len(digits_list) > 0:

#         for i in range(len(digits_list)):
#             for number in digits:
#                 print(number, i, digits_list)
#                 if int(number) % 2 == 0 and int(digits_list[i]) % 2 != 0:
#                     digits_list.pop(0)
#                     substring_list.append(number)

#     print(substring_list)

# def is_next_opposite():
#     if int(number) % 2 == 0 and int(digits_list[i]) % 2 != 0:
#         digits_list.pop(0)
#         substring_list.append(number)

# def longest_substring(digits):
#     substring_list = []
#     digits_list = list(digits)
#     counter = 0

    

#     for i in range(len(digits_list)):
#         print(i)
#         flip_switch = False
#         flip_switch_back = True

#         if int(digits_list[0]) % 2 == 0:
#             # flip_switch = True

#         # First value even
#             while len(digits_list) > 2:
#                 if int(digits_list[i]) % 2 == 0 and int(digits_list[i+1]) % 2 != 0:  
#                     print(digits_list)
#                     substring_list.append(digits_list[i])
#                     digits_list.pop(0)

#                 if int(digits_list[i]) % 2 != 0 and int(digits_list[i+1]) % 2 == 0:  
#                     print(digits_list)
#                     substring_list.append(digits_list[i])
#                     digits_list.pop(0)

#                 else:
#                     digits_list.pop(0)

#             # First value odd
#             while len(digits_list) > 2:
#                 if int(digits_list[i]) % 2 != 0 and int(digits_list[i+1]) % 2 == 0:  
#                     print(digits_list)
#                     substring_list.append(digits_list[i])
#                     digits_list.pop(0)
#                     flip_switch = True

#                 if int(digits_list[i]) % 2 == 0 and int(digits_list[i+1]) % 2 != 0:  
#                     print(digits_list)
#                     substring_list.append(digits_list[i])
#                     digits_list.pop(0)
#                     flip_switch = False

#                 else:
#                     digits_list.pop(0)
            
substring_lists = []

def helper(starts_odd, digits_list, i, substring_lists):
    while len(digits_list) > 2:
        if int(digits_list[i]) % 2 != 0 and int(digits_list[i+1]) % 2 == 0 and starts_odd == False:  
            print(digits_list)
            substring_list.append(digits_list[i])
            digits_list.pop(0)
    
        else:
            if int(digits_list[i]) % 2 == 0 and int(digits_list[i+1]) % 2 != 0:  
                print(digits_list)
                substring_list.append(digits_list[i])
                digits_list.pop(0)
                starts_odd = True


def longest_substring(digits):
    digits_list = list(digits)
    starts_odd = False
    print(digits_list)

    while len(digits_list) > 2:

        if int(digits_list[0]) % 2 == 0:
            starts_odd = True

        for i in range(len(digits_list)):
          if starts_odd == True:
              print()
              helper(starts_odd, digits_list, i, substring_lists)

    print('output:', substring_lists)
	
longest_substring("225424272163254474441338664823")  # ➞ "272163254"
# # substrings = 254, 272163254, 474, 41, 38, 23

# longest_substring("594127169973391692147228678476")  # ➞ "16921472"
# # substrings = 94127, 169, 16921472, 678, 476

# longest_substring("721449827599186159274227324466")  # ➞ "7214"
# # substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
# # 7214 and 9274 have same length, but 7214 occurs first.

