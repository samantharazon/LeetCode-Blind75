
def evalRPN(tokens):
    stack = []
    operators = {'*', '+', '-', '/'}

    for i in tokens:
        if i not in operators:
            stack.append(int(i))
        else:
            second = stack.pop()
            first = stack.pop()

            if i == '+':
                stack.append(first + second)
            elif i == '-':
                stack.append(first - second)
            elif i == '*':
                stack.append(first * second)
            elif i == '/':
                stack.append(int(first / second))
    return stack[0]


tokens = ["2", "1", "+", "3", "*"]
print(f"\ntokens: {tokens}")
result = evalRPN(tokens)
print("result:", result)

tokens = ["4", "13", "5", "/", "+"]
print(f"\ntokens: {tokens}")
result = evalRPN(tokens)
print("result:", result)

print("\n")
