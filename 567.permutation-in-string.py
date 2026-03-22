#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # according the test cases
        # mistake made so far
        # misunderstand the defintion of permuuation
        # also need to record the number of each char
        char_count = Counter(s1)
        l , r = 0, 0
        while (r < len(s2)):
            if s2[r] in char_count and char_count[s2[r]] > 0:
                char_count[s2[r]] -= 1
                r += 1
                if r - l  == len(s1):
                    return True
            else:
                if s2[r] in char_count:
                    while (s2[l] != s2[r]):
                        if s2[l] in char_count:
                            char_count[s2[l]] += 1
                        l += 1
                    l += 1
                    r += 1
                else:
                    char_count = Counter(s1)
                    l = r + 1
                    r += 1
                
        return False
        
# @lc code=end

