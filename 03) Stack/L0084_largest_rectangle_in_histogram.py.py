# determine the area of rectangles for each possible starting point (or bar)
def largestRectangleArea(heights):
    numBars = len(heights)
    maxArea = 0
    stackIndex = []

    for index in range(numBars + 1):        # The +1 ensures that there's an additional iteration after the last bar (index numBars) to handle any bars that remain in the stack.
        # Determine when to calculate the area of a rectangle (only calculate areas when you have a shorter bar or have reached the end)
        # while the stack is not empty [AND] (we've reached the end of the histogram (i == n) [OR] the current bar is shorter than the bar at the top index of the stack)
        while stackIndex and (index == numBars  or heights[index] <= heights[stackIndex[-1]]):
            height = heights[stackIndex.pop()]
            
            # Calculate the width of the rectangle
            if not  stackIndex:
                width = index
            else:
                width = index - stackIndex[-1] - 1

            maxArea = max(maxArea, height * width)
        
        # Push the current index onto the stack
        stackIndex.append(index)
    return maxArea


heights = [2,1,5,6,2,3]
print("\nheights: ", heights)
result = largestRectangleArea(heights)
print("result: ", result)
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

heights = [2,4]
print("\nheights: ", heights)
result = largestRectangleArea(heights)
print("result: ", result)
# Output: 4

print("\n")