#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # possible approaches to solve this problem
        '''
        # 1. brtual force reuslt in time limit exceeded 
        length = len(nums)
        k = k % length
        for i in range(k):
            tmp = nums[length - 1]
            # traverse an array backward
            for j in range(length - 2, -1, -1):
                nums[j+1] = nums[j]
            nums[0] = tmp
        '''
        '''
        # 2. two arrays 
        length = len(nums)
        k = k % length
        arr = [None] * length
        # here just use (i + k)% len(nums) 
        for i in range(k):
            arr[i] = nums[length - k + i]
        for i in range(length - k):
            arr[i + k] = nums[i]
        for i in range(length):
            nums[i] = arr[i]        
        '''
        
        '''
        # 3. recursion: T = T(n-k) + T(k)
        # but the thing the function header is fixed. 
        # Can't pass the length
        length = len(nums)
        k = k % length
        if (k != 0):
            i = int(length/k)
        else: 
            i = 0
        while (i > 0 and length >= k):
            if(length - k >= k):
                for j in range(k):
                    tmp = nums[length - 1 - j]
                    nums [length - 1 - j] = nums [length - 1 - k - j]
                    nums [length - 1 - k - j] = tmp
            
        
            else:
                
                for j in range (length - k):
                    m = length - k - 1 - j
                    for z in range(k):
                        tmp = nums[m]
                        nums[m] = nums[m+1]
                        nums[m+1] = tmp
                        m += 1
                #(removed)
                j = 0
                while(j < length - k):
                    m = length - k - 1 - j
                    for z in range(k):
                        tmp = nums[m]
                        nums[m] = nums[m+1]
                        nums[m+1] = tmp
                        m += 1
                    j += 1
                #
                
    
                    
            length = length - k  
            i -= 1    
            '''
        #4. reversal trick
        l, r = 0, len(nums)-1
        k = k % len(nums)
        # revese the array
        while(l < r):
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l += 1
            r -= 1
        # reverse the k parts 
        l, r = 0, k-1
        while(l < r):
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l += 1
            r -= 1
          # reverse the k parts 
        l, r = k, len(nums)-1
        while(l < r):
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l += 1
            r -= 1

        
        
# @lc code=end

