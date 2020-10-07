'''
Also: 121,122
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time 
(i.e., you must sell the stock before you buy again).
'''
import sys

# Time O(n) , Space O(1)
def maxProfit(prices):
    one_buy = two_buy =   sys.maxsize
    one_profit = two_profit = 0
    for p in prices:
        one_buy = min(one_buy,p) # 第一次买的最低价
        one_profit = max(one_profit,p - one_buy) # 第一次买时， 最大可能利润
        two_buy = min(two_buy,p - one_profit) # 第二次买时，为了加上第一次的利润，最低价为p - one_profit
        # 可以理解为，由于第一次的one_profit的缘故，第二次的profit是在第一次的基础上的，因此可以理解为第二次买时
        # 股票的价格都降低了one_profit，这样算出来才是两次总的profit
        two_profit = max(two_profit,p - two_buy)
    return two_profit

# Time O(n) , Space O(n)
# 从前往后遍历一遍， dp为当天之前可能的最大利润
# 从后往前遍历一遍， dp2为当天之后可能的最大利润
def maxProfit1(prices):
    n = len(prices)
    dp1 = [0] * n
    dp2 = [0] * n
    total = 0
    low = float('inf')
    for i in range(n):
        low = min(low, prices[i])
        if i != 0:
            dp1[i] = max(dp1[i-1], prices[i] - low)
    
    high = float('-inf')
    for i in range(n-1, -1, -1):
        high = max(high, prices[i])
        if i != n-1:
            dp2[i] = max(dp2[i+1], high - prices[i])
        if i != 0:
            total = max(total, dp2[i] + dp1[i])
    return total