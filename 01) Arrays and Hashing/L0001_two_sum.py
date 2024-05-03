def twoSum(nums, target: int):

    dictionary = {}

    for i in range(len(nums)):
        
        complement = target - nums[i]

        if complement in dictionary:
            # return [ value (index) of complement in dict, current index ]
            return [dictionary[complement], i] 
        else:
            # key = nums[i] (future complement to find)
            # value = index of num in arrray
            dictionary[nums[i]] = i 
                            
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


print("=============================")
print("=============================")
thisdict = {
  3: 0,
  2: 1,
  4: 2
}
print([thisdict[2]])
print("=============================")
print("=============================")


# def twoSum(nums, target: int):

#     dictionary = {}

#     for i in range(len(nums)):

#         num = nums[i]   # current value in nums array
#         complement = target - num

#         if num in dictionary:
#             return [dictionary[num], i] # [find key and print its value, print current i]
#         else:
#             dictionary[complement] = i  # store complement at current i

#     return None