
def isValid(s: str) -> bool:

    if len(s) % 2 != 0:
        return False

    dict = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for i in s:
        if i in dict.keys():
            stack.append(i)

        else:
            if stack == []:
                return False

            a = stack.pop()

            if i != dict[a]:    # look at the value of key "a" in dictionary. if the value "a" doesn't match key "i", it's false
                return False

    return stack == []


s = "()"
result = isValid(s)
print("s: ", s)
print(result)
print("---------------------")

s = "(){}[]"
result = isValid(s)
print("s: ", s)
print(result)
print("---------------------")

s = "(]"
result = isValid(s)
print("s: ", s)
print(result)
print("---------------------")

s = "(("
result = isValid(s)
print("s: ", s)
print(result)
print("---------------------")