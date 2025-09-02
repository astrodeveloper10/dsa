def count_x(str):
    if not str:
        return 0

    if str[0] == 'x':
        return 1 + count_x(str[1:])
    else:
        return count_x(str[1:])


print(count_x('xbcdx'))