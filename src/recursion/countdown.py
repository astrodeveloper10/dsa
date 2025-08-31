def countdown(number):
    # while number >= 0:
    #     print(number)
    #     number -= 1
    print(number)

    if number == 0:
        return
    countdown(number - 1)

countdown(10)