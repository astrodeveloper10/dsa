import timeit

def print_even_numbers(n):
    number = 2
    numbers = []

    while number <= n:
        if number % 2 == 0:
            numbers.append(number)
        number += 1

def print_even_numbers1(n):
    number = 2
    numbers = []

    while number <= n:
        numbers.append(number)
        number += 2

# Use timeit to measure performance
execution_time = timeit.timeit(lambda: print_even_numbers(100), number=100)
execution_time1 = timeit.timeit(lambda: print_even_numbers1(100), number=100)

print(f"Execution time: {execution_time * 1000:.4f} milliseconds")
print(f"Execution time: {execution_time1 * 1000:.4f} milliseconds")
