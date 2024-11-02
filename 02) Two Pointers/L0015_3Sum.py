# -4=(a)   |  -1=(b)  -1  0  1  2=(c)
#                L               R
def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()

    for i in range(len(nums)):
        # (a)...
        a_val = nums[i]
        if i > 0 and a_val == nums[i-1]:
            continue

        # (b) and (c)...
        l = i + 1
        r = len(nums) - 1

        while l < r:
            b_val = nums[l]
            c_val = nums[r]
            sum = a_val + b_val + c_val

            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                res.append([a_val, b_val, c_val])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
    return res


''' WITH LOGGING
def threeSum_LOGGING(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()

    print(f"Sorted nums: {nums}")

    for index, a_value in enumerate(nums):
        print("====================")
        print(f"Considering a_value: {a_value} at index {index}")
        
        if index > 0 and a_value == nums[index - 1]:
            print("Duplicate a_value found, skipping to next")
            continue

        l, r = index + 1, len(nums) - 1

        while l < r:
            sumThree = a_value + nums[l] + nums[r]
            print(f"Trying triplet: (a_value={a_value}, nums[l]={nums[l]}, nums[r]={nums[r]}) - Sum: {sumThree}")
            print(f"Visualization: {nums}  i={index}  l={l}  r={r}")

            if sumThree > 0:
                r -= 1
                print(f"Sum > 0, moving right pointer left to r={r}")
            elif sumThree < 0:
                l += 1
                print(f"Sum < 0, moving left pointer right to l={l}")
            else:
                res.append([a_value, nums[l], nums[r]])
                print(f"Sum = 0, found triplet: {[a_value, nums[l], nums[r]]}")
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                    print(f"Skipping duplicate b_value: {nums[l]} after moving left pointer to l={l}")

    return res
'''

nums = [-1, 0, 1, 2, -1, -4]
print("\nnums: ", nums)
result = threeSum(nums)
print("result: ", result)
# Output: [[-1,-1,2],[-1,0,1]]

nums = [-3, 3, 4, -3, 1, 2]
print("\nnums: ", nums)
result = threeSum(nums)
print("result: ", result)

nums = [0, 1, 1]
print("\nnums: ", nums)
result = threeSum(nums)
print("result: ", result)
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

nums = [0, 0, 0]
print("\nnums: ", nums)
result = threeSum(nums)
print("result: ", result)
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

print("\n")
