'''
You are given an integer array prices where prices[i] is the price of
a given stock on the i-th day, and an integer k. 
Find the maximum profit you can achieve. You may complete at most k transactions. 
(Note: You cannot engage in multiple transactions simultaneously; i.e., 
you must sell the stock before you buy again).
Example:Input: k = 2, prices = [3, 2, 6, 5, 0, 3]
Output: 7 (Buy on day 2 [price 2], sell on day 3 [price 6], profit = 4. 
Then buy on day 5 [price 0], sell on day 6 [price 3], profit = 3. Total profit = 7)
'''

def max_profit(k, prices):
    if not prices:
        return 0

    n = len(prices)
    if k >= n // 2:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))

    dp = [[0] * n for _ in range(k + 1)]

    for i in range(1, k + 1):
        max_diff = -prices[0]
        for j in range(1, n):
            dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
            max_diff = max(max_diff, dp[i - 1][j] - prices[j])

    return dp[k][n - 1]


k = 2
prices = [3, 2, 6, 5, 0, 3]
print(max_profit(k, prices))  # Output: 7