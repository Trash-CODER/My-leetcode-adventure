#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        curr_length = 0
        left = 0
        right = 0
        char_dic = dict()
        while (right < len(s)):
            if s[right] in char_dic:
                curr_length = right - left
                max_length = max(max_length, curr_length)
                left = char_dic[s[right]] + 1
                right = left
                char_dic.clear()
            else:
                char_dic[s[right]] = right
                right += 1
                curr_length = right - left
                max_length = max(max_length, curr_length)
        return max_length
        
                
        

        
# @lc code=end

