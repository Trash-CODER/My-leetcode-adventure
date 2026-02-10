#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pidx = 0 # index of the current unique elem
        i = 1 # next checking index
        while(i < len(nums)):
            if (nums[i] == nums[pidx]):
                i += 1
            else:
                nums[pidx+1] = nums[i]
                pidx += 1
                i += 1
        return pidx + 1
        
# @lc code=end

