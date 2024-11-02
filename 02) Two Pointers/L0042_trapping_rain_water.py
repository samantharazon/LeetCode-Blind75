
def trap(height: list[int]) -> int:
    
    if not height:          # list is empty, return 0 because no water can be trapped.
        return 0

    l, r = 0, len(height) - 1                   # l and r are pointers at the leftmost and rightmost indices of the list.
    leftMax, rightMax = height[l], height[r]    # leftMax and rightMax store the maximum height encountered so far from the left and right sides respectively.
    res = 0                                     # res accumulates the total water trapped.

    # The idea is to move inward from both sides using two pointers (l and r) and keep track of the maximum heights encountered.
    while l < r:
        if leftMax < rightMax:                  # If leftMax is smaller, it means the amount of water trapped at the left pointer depends on leftMax
            l += 1
            current_bar = height[l]

            leftMax = max(leftMax, current_bar) # For each step, the water trapped at the current position is calculated as the difference between the maximum height (either leftMax or rightMax) and the height of the current bar. This difference is added to res.
            trapped_water = leftMax - current_bar
            res += trapped_water
        else:                                   # If rightMax is smaller or equal, it means the amount of water trapped at the right pointer depends on rightMax
            r -= 1
            current_bar = height[r]

            rightMax = max(rightMax, current_bar)
            trapped_water = rightMax - current_bar
            res += trapped_water
    return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print("\nheight: ", height)
result = trap(height)
print("result: ", result)
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

height = [4, 2, 0, 3, 2, 5]
print("\nheight: ", height)
result = trap(height)
print("result: ", result)
print()
# Output: 9
