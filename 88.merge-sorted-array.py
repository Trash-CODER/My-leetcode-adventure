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
        # temporay array to hold, use the space to trade for time
        tmp_arra = [0]*(m+n)
        i = 0
        j = 0
        cnt = 0
        while i < m and j < n:
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
        if j == n :
            while(i < m):
                tmp_arra[cnt] = nums1[i]
                cnt += 1
                i += 1
        for i in range(n+m):
            nums1[i] = tmp_arra[i]
        
# @lc code=end

