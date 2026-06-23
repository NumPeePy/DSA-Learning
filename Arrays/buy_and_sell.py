# ========================================================================
# Buy and Sell stock
# ========================================================================

prices = [4, 5, 8, 2, 3, 1, 9, 10, 2, 4]
n = len(prices)

buy = 3
buying_price = prices[buy]

selling_price = buying_price

for i in range(buy + 1, n):

    if prices[i] > selling_price:
            selling_price = prices[i]

print(f"Maximum profit: {selling_price - buying_price}")

# Time Complexity:
# Best:     O(N)
# Average:  O(N)
# Worst:    O(N)

# Space Complexity:
# O(1)