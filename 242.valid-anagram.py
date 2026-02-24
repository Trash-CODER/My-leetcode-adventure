#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tmp_hash = {}
        
        if len(s) != len(t):
            return False
        for letter in s:
            if letter in tmp_hash:
                 tmp_hash[letter] = tmp_hash[letter] + 1
            else:
                 tmp_hash.setdefault(letter,1)
        for letter in t:
            if letter in tmp_hash:
                 tmp_hash[letter] = tmp_hash[letter] - 1
            else:
                 return False
        values = tmp_hash.values()
        for va in values:
            if va != 0:
                return False
        return True
        
                    
# @lc code=end

