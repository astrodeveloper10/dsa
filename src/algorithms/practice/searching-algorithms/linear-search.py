import timeit

def linear_search_ordered_arr(arr, search_value):
    for index, element in enumerate(arr):
        if element == search_value:
            return  index
        elif element > search_value:
            break
    return "Item not found"


execution_time = timeit.timeit(lambda: print(linear_search_ordered_arr([5, 7, 21, 29, 38, 41, 55], 29)), number= 10 )
print(f"Execution time for ordered list: {execution_time * 1000:.4f} milliseconds")
