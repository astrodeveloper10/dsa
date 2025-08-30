from src.datastructures.implementations.stack_impl import StackImpl

class Linter:
    def __init__(self):
        self.stack = StackImpl()

    def lint(self, text):
        while self.stack.read():
            self.stack.pop()

        matching_braces = { "(": ")", "[": "]", "{": "}" }

        for char in text:
            if char in matching_braces.keys():
                self.stack.push(char)
            elif char in matching_braces.values():
                if not self.stack.read():
                    return f'{char} does not have opening brace'
                else:
                    popped_opening_brace = self.stack.pop()

                    if char != matching_braces.get(popped_opening_brace):
                        return f'{char} has mismatched opening brace'

        if self.stack.read():
            return f'{self.stack.read()} does not have closing brace'

        return True


linter = Linter()
print(linter.lint('const x = { y: [1, 2, 3]}'))