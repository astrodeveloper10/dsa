def insertion_sort(arr):
    for index in range(1, len(arr)):
        temp_value = arr[index]
        position = index - 1

        while position >= 0:
            if arr[position] > temp_value:
                arr[position + 1] = arr[position]
                position -= 1
            else:
                break

        arr[position + 1] = temp_value


insertion_sort([8, 4, 2, 3])