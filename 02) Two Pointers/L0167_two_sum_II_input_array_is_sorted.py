def twoSum(numbers: list[int], target: int) -> list[int]:

    l = 0
    r = len(numbers) - 1

    while l < r:
        curSum = numbers[l] + numbers[r]

        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l + 1, r + 1]
    return []


numbers = [2, 7, 11, 15]
target = 9
print(f"\nnumbers: {numbers}, target= {target}")
result = twoSum(numbers, target)
print("result: ", result)
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

numbers = [2, 3, 4]
target = 6
print(f"\nnumbers: {numbers}, target= {target}")
result = twoSum(numbers, target)
print("numbers: ", numbers)
print("result: ", result)
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

numbers = [-1, 0]
target = -1
print(f"\nnumbers: {numbers}, target= {target}")
result = twoSum(numbers, target)
print("numbers: ", numbers)
print("result: ", result)
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
