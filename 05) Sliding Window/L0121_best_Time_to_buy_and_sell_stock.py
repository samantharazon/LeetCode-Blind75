def maxProfit(prices) -> int:
    left_buy = 0  
    right_sell = 1  
    maxProfit = 0

    while right_sell< len(prices):

        # if statement to find right day to buy. continue moving l by one if value next to it is less
        if prices[left_buy] < prices[right_sell]:
            # also find day to sell
            profit = prices[right_sell] - prices[left_buy]
            maxProfit = max(maxProfit, profit)
        else:
            left_buy= right_sell
        right_sell += 1

    return maxProfit


prices = [7,5,1,3,6,4]
print(f"\nprices: {prices}")
result = maxProfit(prices)
print("Max Profit", result)

prices = [7,6,4,1,3]
print(f"\nprices: {prices}")
result = maxProfit(prices)
print("MaxProfit: ", result)

print("\n")