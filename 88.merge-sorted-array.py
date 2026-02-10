#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        """
        # This approach satisfies the logic but violates the "in-place" constraint. 
        # To meet $O(1)$ space complexity requirements, 
        # we must utilize the trailing zero-space in nums1 
        # instead of allocating a third array.
        
        
        # temporay array to hold, use the space to trade for time
        tmp_arra = [0]*(m+n)
        i = 0
        j = 0
        cnt = 0
        while i < m and j < n: #bugfix:shouldn't use <=
            if nums1[i] < nums2[j]:
                tmp_arra[cnt] = nums1[i]
                i += 1
                cnt += 1
            else:
                tmp_arra[cnt] = nums2[j]
                j += 1
                cnt += 1
        
        if i == m:
            while(j < n):
                tmp_arra[cnt] = nums2[j]
                cnt += 1
                j += 1
        if j == n :  # bugfix: syntax mix-up: elif instead elseif
            while(i < m):
                tmp_arra[cnt] = nums1[i]
                cnt += 1
                i += 1
        for i in range(n+m):
            nums1[i] = tmp_arra[i]
"""
        # modifed 
        right = n + m - 1
        midx = m - 1
        nidx = n -1
        
        #comapre two array and put the greater one in the back of array
        while (midx >= 0 and nidx >= 0):
            if nums1[midx] < nums2[nidx]:
                nums1[right] = nums2[nidx]
                right -= 1
                nidx -= 1
            else:
                nums1[right] = nums1[midx]
                right -= 1
                midx -= 1
        # check if any element in array  hasn't been compared
        
        if (nidx >= 0):
            while(nidx >= 0):
                nums1[nidx] = nums2[nidx]
                nidx -= 1
    
            
            
        
# @lc code=end

