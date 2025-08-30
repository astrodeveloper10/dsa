"""
Write a function that accepts a string that contains all the letters of the alphabet except one and returns the missing letter.
For example, the string, "the quick brown box jumps over a lazy dog" contains all the letters of the alphabet except the letter "f".
The function should have a time complexity of O(N).
"""
import  string

def return_missing_letter(input_string):
    for char in string.ascii_lowercase:
        if char not in input_string:
            return char

    return None



print(return_missing_letter('the quick brown box jumps over a lazy dog'))