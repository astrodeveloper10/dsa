class StackImpl:
    def __init__(self):
        self.data = []
        self.length = 0

    def push(self, element):
        self.data.append(element)
        self.length += 1

    def pop(self):
        if self.length > 0:
            self.length -= 1
            return self.data.pop()
        return None

    def read(self):
        if self.length > 0:
            return self.data[-1]
        return None

# s = StackImpl()
# s.push(10)
# s.push(20)
# s.push(30)
# print(f'Stack is: {s.data}')
# print(f'Length of the stack is: {s.length}')
# print(f'Popped element is: {s.pop()}')
# print(f'Length of the stack is: {s.length}')
#
# print(f'Top element is: {s.read()}')
# print()
#
# s1 = StackImpl()
# s1.push(40)
# s1.push(50)
# print(f'Stack is: {s1.data}')
# print(f'Length of the stack is: {s1.length}')
# print(f'Popped element is: {s1.pop()}')
# print(f'Length of the stack is: {s1.length}')
# print(f'Top element is: {s1.read()}')