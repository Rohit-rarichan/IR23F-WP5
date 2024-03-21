class RPNCalculator:
    def __init__(self):
        self.stack = []

    def evaluate_rpn(self, expression):
        tokens = expression.split()
        for token in tokens:
            if token.isdigit():
                self.stack.append(int(token))
            elif token in "+-*/":
                self._apply_operator(token)
        return self.stack.pop()
