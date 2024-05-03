def maxProfit(prices) -> int:
    left_buy = 0  
    right_sell = 1  
    maxProfit = 0

    while right_sell< len(prices):

        if prices[left_buy] < prices[right_sell]:
            profit = prices[right_sell] - prices[left_buy]
            maxProfit = max(maxProfit, profit)
        else:
            left_buy= right_sell
        right_sell += 1

    return maxProfit


prices = [7,5,1,3,6,4]
result = maxProfit(prices)
print(prices)
print("\nMaximum Profit: ", result)
print("--------------------")

prices = [7,6,4,1,3]
result = maxProfit(prices)
print(prices)
print("\nMaximum Profit: ", result)
print("--------------------")