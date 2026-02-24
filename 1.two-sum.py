#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        # btrual force 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target ==  nums[j] + nums[i]:
                    return [i,j]
        '''
        tmp_hash = {}
        for i in range(len(nums)):
            tmp_hash.setdefault(nums[i],i)
            
        for i in range(len(nums)):
            if target - nums[i] in tmp_hash:
                if i != tmp_hash.get(target - nums[i]):
                    return [i,tmp_hash.get(target - nums[i])]
        
                
        
# @lc code=end

