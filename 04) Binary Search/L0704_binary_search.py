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
            print("target", target, "exists in nums, its index is", m)
            return m
        
    print("target", target, "does not exist in nums, returning -1")
    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(f"\nnums: {nums}, target={target}")
result = search(nums, target)
print(f"result = {result}")

nums = [-1, 0, 3, 5, 9, 12]
target = -2
print(f"\nnums: {nums}, target={target}")
result = search(nums, target)
print(f"result = {result}")

print("\n")