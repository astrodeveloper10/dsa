def factorial_bottom_up_approach(n, i=1, product=1):
    if i > n:
        return product

    return factorial_bottom_up_approach(5, i + 1, product * i)

print(factorial_bottom_up_approach(5))