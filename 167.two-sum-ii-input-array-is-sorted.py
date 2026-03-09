#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers 
        # brtual force l = 0 and with r stating at last inde it compares
        # every time with the target till s[l]+ s[r] = target
        
        # optimal 
        left, right = 0, len(numbers) - 1
        while (left <  right):
            if(numbers[left] + numbers[right] < target):
                left += 1
            elif(numbers[left] + numbers[right] > target):
                right -= 1
            else:
                return [left + 1,right + 1]
        return None 
# @lc code=end

