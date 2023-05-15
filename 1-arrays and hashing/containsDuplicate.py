def containsDuplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


nums = [1,2,3,1]
result = containsDuplicate(nums)
print("nums: ", nums)
print("result: ", result)

nums = [1,2,3,4]
result = containsDuplicate(nums)
print("\nnums: ", nums)
print("result: ", result)

nums = [1,1,1,3,3,4,3,2,4,2]
result = containsDuplicate(nums)
print("\nnums: ", nums)
print("result: ", result)