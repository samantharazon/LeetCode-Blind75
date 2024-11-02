def maxArea(height: list[int]) -> int:
    res = 0
    l = 0
    r = len(height) - 1

    while l < r:
        length =  min(height[l], height[r]) # determined by the shorter of the two lines
        width = r - l # distance between the two lines
        area = length * width
        res = max(res, area) #  maximum area found so far 

        print(f"length:{length} * width:{width} = area:{area}")

        # The pointer pointing to the shorter line is moved inward to potentially find a larger area
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
