#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # first intituion is greedy alg, but can't find the greed property
        # then tried to convert it into the graph but too sophiscated 
        # identify the optimal structure: the max profits over n days
        # is simply the sum of every incrase.
        yes_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if yes_price >= p:
                yes_price = p
            else:
                profit += (p - yes_price)
                yes_price = p
        
        return profit
    
    # extensive question: adding transaction fee or limits to that
    
        
# @lc code=end

