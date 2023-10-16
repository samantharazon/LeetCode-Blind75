# We are counting the length of each sequence
# return the longest length!!
# ex: nums = [100,4,200,1,3,2]
# sequence 1)  100      --> length=1
# sequence 2)  200      --> length=1
# sequence 3)  1,2,3,4  --> length=4

def longestConsecutive(nums: list[int]):
    numSet = set(nums)   # passing array to set
    longest = 0

    for n in nums:
        # check if it's the start of a sequence
        if (n - 1) not in numSet:   # check for left neighbor. if num doesn't have left neighbor, it's the start of a sequence
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