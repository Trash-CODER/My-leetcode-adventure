#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        # first solution, brute force
        # use two round, fix one end and then move the other end 
        
        
        # two pointers starting at different two ends
        # and the windth would be decease if pointers move toward the mid
        # Therefore the next height should increase, otherwise the volume would shrink
        # how to decide which pointer moves towards th other one 
        # idealy, keep the higher one and move the shorter one 
        max_area = 0.
        left, right = 0, len(height) - 1
        while(left < right ):
            curr_area = (right - left) * min(height[left], height[right])
            max_area = max(curr_area, max_area)
            
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return max_area
        
# @lc code=end

