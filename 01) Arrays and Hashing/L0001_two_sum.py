def twoSum(nums, target: int):

    dictionary = {}

    for i in range(len(nums)):
        
        complement = target - nums[i]

        if complement in dictionary:
            # return [ value (index) of complement in dict, current index ]
            return [dictionary[complement], i] 
        else:
            # key = nums[i] (future complement to find)
            # value = index of num in array
            dictionary[nums[i]] = i 
                            
    return None

nums = [11, 2, 15, 7]
target = 9
print("\nArray: ", nums)
print("Target: ", target)
result = twoSum(nums, target)
print("Indices: ", result)


nums = [3, 2, 4]
target = 6
print("\nArray: ", nums)
print("Target: ", target)
result = twoSum(nums, target)
print("Indices: ", result)

nums = [3, 3]
target = 6
print("\nArray: ", nums)
print("Target: ", target)
result = twoSum(nums, target)
print("Indices: ", result)