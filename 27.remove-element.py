#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # first thought is to use the data structure set to do it 
        # however the constraints requires in-place
        i = 0 #mark the current checking index
        pidx = 0 # mark the current saving index
        k = 0
        while(i < len(nums)):
            if (nums[i] == val):
                i += 1
            else:
                nums[pidx] = nums[i]
                pidx += 1
                i += 1
                k += 1
        return k
            
                    

        
# @lc code=end

