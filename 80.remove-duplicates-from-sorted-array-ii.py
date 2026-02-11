#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        # same with the removeDup 1(use two pointers to walk through the list)
        # The difference is that each elm can appear at most twice
        # So we need a flag to determine that 
        flag = False
        pidx = 0
        i = 1
        while (i < len(nums)):
            # check if the current elm = previous elm
            if(nums[pidx] == nums[i]):
                # check if the elm has appeared more than twice
                if(flag):
                    i += 1
                else: 
                    #!!!! there might need some gap between pidx+1 and i
                    if(i - pidx != 1):
                        nums[pidx+1] = nums[i]
                        
                    i += 1
                    pidx += 1
                    flag = True
                    
            else:
                #reset the flag
                flag = False
                nums[pidx+1] = nums[i]
                pidx += 1
                i += 1
        return pidx + 1      
        '''
        # same logic but hit the smart more
        # the core is to check the current i is the third duplicates
        # and k only move forward with i when  current elm is not the same with k
        
        k = 2 
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k       
    
        # the latter code is simple but some how it takes longer and more memory.  
        
# @lc code=end

