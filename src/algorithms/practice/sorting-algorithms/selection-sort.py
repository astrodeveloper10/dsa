def selection_sort(arr):
    for i in range(len(arr)):
        lowest_number_index = i

        for j in range(i + 1, len(arr) - 1):
            if arr[j] < arr[lowest_number_index]:
                lowest_number_index = j

        if lowest_number_index != i:
            arr[lowest_number_index], arr[i] = arr[i], arr[lowest_number_index]

    print(arr)


selection_sort([2, 6, 1, 3])