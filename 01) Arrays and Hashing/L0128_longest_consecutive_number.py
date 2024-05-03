
def longestConsecutive(nums: list[int]):
    numSet = set(nums)   
    longest = 0

    for n in nums:
        if (n - 1) not in numSet: 
            length = 0
            while (n + length) in numSet: 
                length += 1
            longest = max(length, longest)
    return longest


nums = [100,4,200,1,3,2]
result = longestConsecutive(nums)
print("\nInput: nums = ", nums)
print("Output: ", result)

nums = [0,3,7,2,5,8,4,6,0,1]
result = longestConsecutive(nums)
print("\nInput: nums = ", nums)
print("Output: ", result)

nums = [9, 343, 543, 10, 7, 894, 8]
result = longestConsecutive(nums)
print("\nInput: nums = ", nums)
print("Output: ", result)

print()