class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def read(self):
        return self.data[-1]

class Linter:
    def __init__(self):
        self.stack = Stack()

    def is_opening_brace(self, char):
        return char in ["(", "[", "{"]

    def is_closing_brace(self, char):
        return char in [")", "]", "}"]

    def is_not_a_match(self, opening_brace, closing_brace):
        closing_brace = {")": "(", "]": "[", "}": "{"}
        if opening_brace != closing_brace.get(opening_brace):
            return True
        return False

    def lint(self, text):
        print(f"text is {text}")
        for char in text:
            print(f"char is {char}")
            if self.is_opening_brace(char):
                self.stack.push(char)
            elif self.is_closing_brace(char):
                popped_opening_brace = self.stack.pop()
                if not popped_opening_brace:
                    return f"{char} doesn't have opening brace"
                if self.is_not_a_match(popped_opening_brace, char):
                    return f"{char} has mismatched opening brace"
            if self.stack.read():
                return f"#{self.stack.read()} does not have closing brace"
        return True

linter = Linter()
linter.lint("(let x = { y: [1, 2, 3] } )")
