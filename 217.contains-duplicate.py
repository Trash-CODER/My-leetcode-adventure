#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tmp_set = set()
        for num in nums:
            if num in tmp_set:
                return True
            else:
                tmp_set.add(num)
        return False
        
# @lc code=end

