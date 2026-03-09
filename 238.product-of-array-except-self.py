#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # count the number of zero
        # if the number of zero is greater than 1 return an all zero list
        output = [0]*len(nums)
        cnt = 0
        mark = 0
        # small improvement can be done here
        # just calculate the pruduct of all non-zero numebrs
        for i in range(len(nums)):
            if nums[i] == 0:
                mark = i
                cnt += 1
                if cnt >= 2:
                    return output 
                mark = i
        product_of_all = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                product_of_all *= nums[i]
        if (cnt != 0):
            output[mark] = product_of_all
            return output
        for i in range(len(nums)):
            output[i] = int(product_of_all / nums[i])
        return output 
            
    # another ideal solution 
    # Prefix Sum/Product - Understanding how to build cumulative products
    # from left-to-right and right-to-left to avoid recomputation
            
        
# @lc code=end

