##############################################################
def findDuplicate(nums):
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow
##############################################################

nums = [1,3,4,2,2]
print("\nnums:", nums) 
result = findDuplicate(nums) 
print("Duplicate Number:", result)

nums = [3,1,3,4,2]
print("\nnums:", nums) 
result = findDuplicate(nums) 
print("Duplicate Number:", result)

nums = [3,3,3,3,3]
print("\nnums:", nums) 
result = findDuplicate(nums) 
print("Duplicate Number:", result)

print("\n")