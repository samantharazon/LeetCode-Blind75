def productExceptSelf(nums):
    
    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):  # start at beginning, go to end
        res[i] = prefix         # set the result value at i = prefix
        prefix *= nums[i]       # calculate new prefix
    postfix = 1
           # range(start,........stop,..step)
    for i in range(len(nums) - 1, -1, -1):  # start at end, go to beginning
        res[i] *= postfix                   # set result value at i times what's already there
        postfix *= nums[i]                  # calculate new postfix
    return res

nums = [2,3,4,5]
result = productExceptSelf(nums)
print("\nnums: ", nums)
print("result: ", result)

nums = [1,2,3,4]
result = productExceptSelf(nums)
print("\nnums: ", nums)
print("result: ", result)

nums = [-1,1,0,-3,3]
result = productExceptSelf(nums)
print("\nnums: ", nums)
print("result: ", result)