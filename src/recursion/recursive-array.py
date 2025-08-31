def print_recursive_array(arr):
    for item in arr:
        if isinstance(item, int):
            print(item)
        else:
            print_recursive_array(item)


print_recursive_array(
    [
        1,
        2,
        3,
        [4, 5, 6],
        7,
        [
            8,
            [9, 10, 11, [
                12, 13, 14
            ]]
        ],
        [15, 16, 17, 18, 19,
            [20, 21, 22,
                [ 23, 24, 25,
                    [ 26, 27, 28 ]
                ], 30, 31,
            ], 32
        ], 33
    ]
)