#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hasp_map = dict()
        left, right = 0, 0
        max_count = 0
        max_len = 0
        while (right < len(s)):
            if s[right] in hasp_map:
                hasp_map[s[right]] += 1
                max_count = max(max_count, hasp_map[s[right]])
                if((right - left + 1) - max_count > k):
                    hasp_map[s[left]] -= 1
                    left += 1
                    max_count = max(hasp_map.values())
            else:   
                hasp_map[s[right]] = 1 
                max_count = max(max_count, hasp_map[s[right]])
                if((right - left + 1) - max_count > k):
                    hasp_map[s[left]] -= 1
                    left += 1
                    max_count = max(hasp_map.values())
                
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len

    '''
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet: # keep deleted untill the duplicate is removed
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    '''
            

        
# @lc code=end

