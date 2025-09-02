def double_array(arr, index= 0):
    # Creates a new list
    # return [item * 2 for item in arr]

    # Modifies the list in-place without recursion
    # if not arr:
    #     return None
    #
    # for i in range(len(arr)):
    #     arr[i] = arr[i] * 2
    #
    # return arr

    # Using recursion
    if index >= len(arr):
        return None

    arr[index] *= 2
    double_array(arr, index + 1)

    return arr

print(double_array([1, 2, 3, 4, 5]))