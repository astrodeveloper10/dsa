def sum_of_array(arr):
    if not arr:
        return 0

    return arr[0] + sum_of_array(arr[1:])

print(sum_of_array([1, 2, 3, 4, 5]))
