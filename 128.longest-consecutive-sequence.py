#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        
        num_set = set(nums)
        max_val = 0
        length = 0
        for num in num_set:
            if( num - 1 not in num_set):
                curr = num
                length = 1
                while (curr + 1 in num_set):
                    length += 1
                    curr += 1 
                if (max_val < length):
                    max_val = length               
        
                
        return max_val
                
            
# @lc code=end

