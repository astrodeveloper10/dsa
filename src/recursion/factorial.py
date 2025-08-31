def factorial(number):
    if number < 0:
        return 'Please enter a positive number'
    elif number in [0, 1]:
        return 1
    else:
        # result = 1
        #
        # while number > 0:
        #     result = result * number
        #     number -= 1
        # return result
        return number * factorial(number - 1)

print(factorial(5))
print(factorial(1))
print(factorial(0))
print(factorial(-1))