"""
Write a function that returns the intersection of two arrays.
The intersection is a third array that contains all values contained within the first two arrays.
For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8] is [2, 4].

Your function should have a complexity of O(N).
(If your programming language has a built-in way of doing this, don’t use it. The idea is to build the algorithm yourself.)
"""

def two_array_intersection(arr1, arr2):
    arr3 = []

    for item in arr1:
        if item in arr2:
            arr3.append(item)

    return arr3


print(two_array_intersection([1, 2, 3, 4, 5], [0, 2, 4, 6, 8]))