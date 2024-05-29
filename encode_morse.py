# Encode Morse

# UPER

# Understand - Create a function that takes a string as an argument and returns the Morse code equivalent.
# Input value can be lower or upper case.
# Input string can have digits.
# Input string can have some special characters (e.g. comma, colon, apostrophe, period, question mark, exclamation mark).
# One space " " is expected after each character, except the last one.
# Ouput should be International Morse Code, and use the standard conventions for symbols not defined inside the ITU recommendation.
# Empty space? - added to char_to_dots dictonary

# Plan
# Option 1
# Loop thru message
# for each value return the dictonary value plan empty space " " - .value() 

# Option 2
# While
# convert to list
# pop off first value
# return the dictonary value plan empty space " " - .value()

# Option 3
# Recursion 

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.', 
  ' ': ' '
}

# def encode_morse(message):
#     output_message = ''
#     message_list = list(message)
    
#     while len(message_list) > 1:
#         char = message_list.pop(0)
#         morse_value = char_to_dots.get(char.upper())
#         output_message += morse_value + ' '

#     while len(message_list) > 0:
#         char = message_list.pop(0)
#         morse_value = char_to_dots.get(char.upper())
#         output_message += morse_value
    
#     print(output_message)
#     return output_message

# def encode_morse(message):
#     output_message = ''
#     message_list = list(message)
    
#     while len(message_list) > 1:
#         morse_value = char_to_dots.get(message_list.pop(0).upper())
#         output_message += morse_value + ' '

#     # Add the last value with no space after it.
#     morse_value = char_to_dots.get(message_list.pop(0).upper())
#     output_message += morse_value
    
#     print(output_message)
#     return output_message

# def encode_morse(message):
#     output_message = ''
#     message_list = list(message)
    
#     while len(message_list) > 0:
#         morse_value = char_to_dots.get(message_list.pop(0).upper())
#         output_message += morse_value + ' '

#     # Remove the last empty space.
#     result = output_message[:len(output_message)-1]
#     return result


def encode_morse(message):
    return ' '.join(char_to_dots[c] for c in message.upper())


encode_morse("did you got my mail ?")  # ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."

# encode_morse("HELP ME !")  # ➞ ".... . .-.. .--.   -- .   -.-.--"


