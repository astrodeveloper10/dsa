"""
Write a function that accepts an array of strings and returns the first duplicate value it finds.
For example, if the array is ["a", "b", "c", "d", "c", "e", "f"], the function should return "c",
since it’s duplicated within the array. (You can assume that there’s one pair of duplicates within the array.)

Make sure the function has an efficiency of O(N).
"""

def get_first_duplicate_value(arr):
    duplicate_dict = {}

    for item in arr:
        if item in duplicate_dict:
            return item

        duplicate_dict[item] = duplicate_dict.setdefault(item, 0) + 1

    return None

print(get_first_duplicate_value(["a", "b", "c", "d", "c", "e", "f"]))