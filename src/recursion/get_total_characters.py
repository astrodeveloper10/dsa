"""
Use recursion to write a function that accepts an array of strings and returns the
total number of characters across all the strings. For example, if the input array is ["ab", "c", "def", "ghij"],
the output should be 10 since there are ten characters in total.
"""

def get_total_characters(arr, total_chars=0, index=0):
    if not arr:
        return None

    if index >= len(arr):
        return total_chars

    """
    Normal loop
    
    total_characters = 0

    for item in arr:
        total_characters += len(item)

    return total_characters
    """

    total_chars += len(arr[index])
    return get_total_characters(arr, total_chars, index + 1)



print(get_total_characters(['ab', 'c', 'def', 'ghij']))