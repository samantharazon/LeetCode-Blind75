def threeSum(nums: list[int]) -> list[list[int]]:
    
    res = []
    nums.sort()     # -4, -1, -1, 0, 1, 2


    # -4=a   |  -1=b  -1  0  1  2=c

    for index, a_value in enumerate(nums): # iterating through nums. keeping track of index and current value
        # Find (a)...
        if index > 0 and a_value == nums[index - 1]:  # don't reuse value
            continue

        l = index + 1
        r = len(nums) - 1

        # Find (b) and (c)...
        # 2SumII Solution:
        while l < r:
            sumThree = a_value + nums[l] + nums[r]
            if sumThree > 0:
                r -= 1
            elif sumThree < 0:
                l += 1
            else:
                res.append([a_value, nums[l], nums[r]])
                l += 1
                # if it's same value, keep shifting && don't pass right pointer
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return res


nums = [-1, 0, 1, 2, -1, -4]
result = threeSum(nums)
print("\nnums: ", nums)
print("result: ", result)
print()
# Output: [[-1,-1,2],[-1,0,1]]
'''
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''

nums = [-3, 3, 4, -3, 1, 2]
result = threeSum(nums)
print("\nnums: ", nums)
print("result: ", result)
print()

nums = [0, 1, 1]
result = threeSum(nums)
print("nums: ", nums)
print("result: ", result)
print()
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

nums = [0, 0, 0]
result = threeSum(nums)
print("\nnums: ", nums)
print("result: ", result)
print()
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
