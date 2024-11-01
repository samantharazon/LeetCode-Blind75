
def isValid(s: str) -> bool:

    if len(s) % 2 != 0:
        return False

    dict = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for val in s:
        if val in dict.keys():
            stack.append(val)
        else:
            if stack == []:
                return False

            key = stack.pop()

            if val != dict[key]:
                return False

    return stack == []


s = "()"
print(f"\ns: {s}")
result = isValid(s)
print("result:", result)

s = "(){}[]"
print(f"\ns: {s}")
result = isValid(s)
print("result:", result)

s = "(]"
print(f"\ns: {s}")
result = isValid(s)
print("s: ", s)
print("result:", result)

s = "(("
print(f"\ns: {s}")
result = isValid(s)
print("s: ", s)
print("result:", result)
