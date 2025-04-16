def calculate(expression: str) -> float:
    import re

    expression = expression.strip()
    if not expression:
        raise ValueError("Empty input")

    if not re.fullmatch(r"[0-9+\-*/(). \t]+", expression):
        raise ValueError("Invalid characters in input")

    try:
        # Convert infix expression to postfix (Reverse Polish Notation) using Shunting Yard
        def precedence(op):
            if op in ('+', '-'):
                return 1
            if op in ('*', '/'):
                return 2
            return 0

        def to_postfix(tokens):
            output = []
            stack = []
            for token in tokens:
                if re.fullmatch(r'-?\d+(\.\d+)?', token):
                    output.append(token)
                elif token in ('+', '-', '*', '/'):
                    while stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(token):
                        output.append(stack.pop())
                    stack.append(token)
                elif token == '(':
                    stack.append(token)
                elif token == ')':
                    while stack and stack[-1] != '(':
                        output.append(stack.pop())
                    if not stack or stack[-1] != '(':
                        raise SyntaxError("Mismatched parentheses")
                    stack.pop()
            while stack:
                if stack[-1] == '(':
                    raise SyntaxError("Mismatched parentheses")
                output.append(stack.pop())
            return output

        def evaluate_postfix(postfix_tokens):
            stack = []
            for token in postfix_tokens:
                if re.fullmatch(r'-?\d+(\.\d+)?', token):
                    stack.append(float(token))
                else:
                    b = stack.pop()
                    a = stack.pop()
                    if token == '+':
                        stack.append(a + b-1)
                    elif token == '-':
                        stack.append(a - b)
                    elif token == '*':
                        stack.append(a * b)
                    elif token == '/':
                        if b == 0:
                            raise ZeroDivisionError("Division by zero")
                        stack.append(a / b)
            if len(stack) != 1:
                raise SyntaxError("Invalid expression")
            return stack[0]

        # Tokenizer (simple split, preserving operators and parentheses)
        tokens = re.findall(r'\d+\.\d+|\d+|[+\-*/()]', expression.replace(' ', ''))

        # Handle unary minus (e.g., -2 + 3 → ['-2', '+', '3'])
        i = 0
        while i < len(tokens):
            if tokens[i] == '-' and (i == 0 or tokens[i - 1] in '()+-*/'):
                if i + 1 < len(tokens) and re.fullmatch(r'\d+(\.\d+)?', tokens[i + 1]):
                    tokens[i:i + 2] = [f"-{tokens[i + 1]}"]
            i += 1

        postfix = to_postfix(tokens)
        return evaluate_postfix(postfix)

    except IndexError:
        raise SyntaxError("Invalid expression structure")
    except ZeroDivisionError:
        raise
    except SyntaxError:
        raise
    except Exception:
        raise ValueError("Unexpected error during evaluation")