def greatest_number(arr):
    if not arr:
        return None

    max_num = arr[0]

    for i in arr:
        if i > max_num:
            max_num = i

    return  max_num

print(greatest_number([10, 100, 9, 71, 206, 501, 22, 7]))