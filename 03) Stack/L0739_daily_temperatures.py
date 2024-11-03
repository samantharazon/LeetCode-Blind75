
def dailyTemperatures(temperatures):
        result = [0] * len(temperatures)    # An array of the same length as temperatures, initialized with zeros. This will store the number of days until a warmer temperature for each day.
        stack = []                          # The stack is a way to keep track of temperatures that haven't yet found a warmer temperature in the future. It will keep track of the indices of the temperatures that we are processing.
        
        for temp_index in range(len(temperatures)): # while the current temperature is warmer than the temperature at the index stored at the top of the stack:
            while stack and temperatures[stack[-1]] < temperatures[temp_index]:
                prev_day = stack.pop()
                warm_days = temp_index-prev_day
                result[prev_day] = warm_days #  This difference is the number of days until a warmer temperature for the day at index a.
            
            stack.append(temp_index)

        return result


temperatures = [73,74,75,71,69,72,76,73]
print(f"\ntemps: {temperatures}")
result = dailyTemperatures(temperatures)
print(f"result: {result}") # Output: [1,1,4,2,1,1,0,0]

temperatures = [30,40,50,60]
print(f"\ntemps: {temperatures}")
result = dailyTemperatures(temperatures)
print(f"result: {result}") # Output: [1,1,1,0]

temperatures = [30,60,90]
print(f"\ntemps: {temperatures}")
result = dailyTemperatures(temperatures)
print(f"result: {result}") # Output: [1,1,0]

print("\n")