def containsDuplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


nums = [1,2,3,1]
print("\nnums: ", nums)
result = containsDuplicate(nums)
print("result: ", result)

nums = [1,2,3,4]
print("\nnums: ", nums)
result = containsDuplicate(nums)
print("result: ", result)

nums = [1,1,1,3,3,4,3,2,4,2]
print("\nnums: ", nums)
result = containsDuplicate(nums)
print("result: ", result)

print("\n")