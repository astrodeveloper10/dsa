def reverse_string_with_recursion(str):
    if not str:
        return ''

    # iva + s
    # va + is
    # a + vis
    # '' + avis
    return reverse_string_with_recursion(str[1:]) + str[0]

print(reverse_string_with_recursion('siva'))