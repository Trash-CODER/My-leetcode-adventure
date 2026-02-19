#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        # first intituion is that brute force.
        # to caculate all the differences for each paris
        # 1. brute force (time limit exceeded)
        max = 0
        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                diff = prices[j] - prices[i]
                if (max < diff):
                    max = diff
        return max
        '''
        '''
        # 2. greedy approach
        # In order to have max gain, u need the both lowerest price and highest one
        low_price = 0
        high_price = 0
        max_profit = 0
        for i in range(len(prices)):
            #check lowest price
            if prices[i] < prices[low_price]:
                low_price = i
                high_price = i # reset it 
            if prices[i] > prices[high_price]:
                high_price = i
                diff = prices[high_price] - prices[low_price]
                if(diff > max_profit):
                    max_profit = diff
        return max_profit
        '''
        # simplified greedy alg
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        return profit
            
            
# @lc code=end

