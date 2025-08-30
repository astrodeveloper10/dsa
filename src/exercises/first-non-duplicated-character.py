"""
Write a function that returns the first non-duplicated character in a string.
For example, the string, "minimum" has two characters that only exist once—the "n" and the "u",
so your function should return the "n", since it occurs first.

The function should have an efficiency of O(N).
"""

def get_first_non_duplicated_character(string):
    char_dict = {}

    for char in string:
        char_dict[char] = char_dict.setdefault(char, 0) + 1

    for item in char_dict.keys():
        if char_dict.get(item) == 1:
            return item

    return None

print(get_first_non_duplicated_character('minimum'))