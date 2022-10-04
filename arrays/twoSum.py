
def twoSum(nums, target: int):

    dictionary = {}

    for i in range(len(nums)):

        num = nums[i]   # current value in nums array
        complement = target - num

        if num in dictionary:
            return [dictionary[num], i]     # return value at dictionary key using num (complement we found earlier) and current placement in nums i
        else:
            dictionary[complement] = i  # store complement at current i

    return None


nums = [11, 2, 15, 7]
target = 9
result = twoSum(nums, target)
print("Array: ", nums)
print("Target: ", target)
print("\nIndices: ", result)
print("--------------------------")

nums = [3, 2, 4]
target = 6
result = twoSum(nums, target)
print("Array: ", nums)
print("Target: ", target)
print("\nIndices: ", result)
print("--------------------------")

nums = [3, 3]
target = 6
result = twoSum(nums, target)
print("Array: ", nums)
print("Target: ", target)
print("\nIndices: ", result)
print("--------------------------")
