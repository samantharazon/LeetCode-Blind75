def search(nums, target):
      l = 0
      r = len(nums) - 1
      
      while l <= r:
        m = (l + r) // 2
        
        if nums[m] > target:
          r = m - 1     
        elif nums[m] < target:
          l = m + 1
        else:
          return m
      
      return -1


nums = [-1,0,3,5,9,12]
target = 9
result = search(nums, target)
print(nums)
if result != -1:
    print(target, "exists in nums and its index is", result)
else:
    print(target, "does not exist in nums so return", result)
print("--------------------")

nums = [-1,0,3,5,9,12]
target = -2
result = search(nums, target)
print(nums)
if result != -1:
    print(target, "exists in nums and its index is", result)
else:
    print(target, "does not exist in nums so return", result)
print("--------------------")