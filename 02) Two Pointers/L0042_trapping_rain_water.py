def trap(height: list[int]) -> int:

    if not height:
        return 0

    l = 0
    r = len(height) - 1
    leftMax = height[l]
    rightMax = height[r]
    res = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]

    return res



height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
result = trap(height)
print("\nheight: ", height)
print("result: ", result)
print()
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

height = [4, 2, 0, 3, 2, 5]
result = trap(height)
print("height: ", height)
print("result: ", result)
print()
# Output: 9
