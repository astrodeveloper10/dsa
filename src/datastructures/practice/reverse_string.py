from src.datastructures.implementations.stack_impl import StackImpl

def reverse_string(string):
    stack = StackImpl()
    result = ''

    for char in string:
        stack.push(char)

    while stack.length > 0:
        result += stack.pop()

    return result


print(reverse_string('abcde'))