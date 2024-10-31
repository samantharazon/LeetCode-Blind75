def maxArea(height: list[int]) -> int:
    res = 0
    l = 0
    r = len(height) - 1

    while l < r:
        # area = width * length
        area = min(height[l], height[r]) * (r - l)
        print("length:", min(height[l], height[r]), "* width:", r-l, "= area:", area)
        res = max(res, area)

        # shift over by whichever of two is the min value
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1

    return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print("\nheight: ", height)
result = maxArea(height)
print("result: ", result)  # result: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

height = [1, 1]
print("\nheight: ", height)
result = maxArea(height)
print("result: ", result)

print("\n")
