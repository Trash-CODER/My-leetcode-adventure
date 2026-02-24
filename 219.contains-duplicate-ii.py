#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        tmp_set = set()
        for i in range(len(nums)):
            if  nums[i] not in tmp_set:
                tmp_set.add(nums[i])
            else:
                start = i - k if i - k >= 0 else 0
                end  = i + k if i + k < len(nums) else len(nums) - 1
                while start <= end:
                    # here need to check they are the same index
                    if nums[start] == nums[i] and start != i:
                        return True
                    start += 1
        return False
        '''
        
        tmp_set = set()
        for i in range(len(nums)):
            if nums[i] in tmp_set:
                return True
            tmp_set.add(nums[i])
            # the catch here is once the gap is greater the k
            # dump the the ealries elem added into set
            if len(tmp_set) > k:
                tmp_set.remove(nums[i-k])
        return False        
        
# @lc code=end

