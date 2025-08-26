def has_duplicate_value(arr):
    existing_nums = [0] * 11

    for i in range(len(arr)):
        if existing_nums[arr[i]] == 1:
            return True
        else:
            existing_nums[arr[i]] = 1

    print(existing_nums)

    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    #         if (i != j) and arr[i] == arr[j]:
    #             return True
    return False

print(has_duplicate_value([3, 5, 8, 3]))