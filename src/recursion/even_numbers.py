"""
Use recursion to write a function that accepts an array of numbers and returns a new array containing just the even numbers.
"""

def get_even_numbers(arr, index=0):
    if arr is None:
        return None

    if index >= len(arr):
        return []

    rest = get_even_numbers(arr, index + 1)

    if arr[index] % 2 == 0:
        return [arr[index]] + rest
    else:
        return rest

print(get_even_numbers([1, 2, 3, 4, 5]))