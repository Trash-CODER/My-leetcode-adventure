#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # too complciated
        '''
        left, right = 0, len(s) -1  
        left_flag = False
        right_flag = False
        while (left < right):
            tmp_l, tmp_r =  0, 0
            if( ord(s[left]) >=  48 and  ord(s[left]) <= 57 ):
                left_flag = True
                tmp_l = ord(s[left])
            elif(ord(s[left]) >=  65 and  ord(s[left]) <= 90):
                left_flag = True 
                tmp_l = ord(s[left])
            elif(ord(s[left]) >=  97 and  ord(s[left]) <= 122):
                left_flag = True 
                tmp_l = ord(s[left]) - 32
            else:
                left_flag = False
                left += 1
            if( ord(s[right]) >=  48 and  ord(s[right]) <= 57 ):
                right_flag = True
                tmp_r = ord(s[right])
            elif(ord(s[right]) >=  65 and  ord(s[right]) <= 90):
                right_flag = True 
                tmp_r = ord(s[right])
            elif(ord(s[right]) >=  97 and  ord(s[right]) <= 122):
                right_flag = True 
                tmp_r = ord(s[right]) - 32
            else:
                right_flag = False
                right -= 1
            # if comparbale 
            # be cautious about the '0' + 32 = 'P' 
            if(left_flag and right_flag):
                if(tmp_l != tmp_r):
                    return False
                else:
                    left += 1
                    right -= 1
                    continue
        return True
        '''
        # 2 reverse
        # regular expression
        '''
        import re
        new_str = re.sub(r"[^a-z0-9]", "", s.lower())
        return new_str == new_str[::-1]
        '''
        l , r = 0, len(s) - 1
        while( l < r):
            while( l < r and not s[l].isalnum()):
                l += 1
            while(l < r and not s[r].isalnum()):
                r -= 1
            if(s[l].lower() != s[r].lower()):
                return False
            l += 1
            r -= 1
        return True
            
        
                    
                
                
            
        
        
# @lc code=end

