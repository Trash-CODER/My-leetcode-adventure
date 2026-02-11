#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sdd = 1
        # Three Intuition 
        # 1 sorted, the majority elm will always be present at mid index 
        # 2 hashmap to store and count
        # 3 mooore voting
        '''  
        # use the map to store it
        map = {}
        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        # then find the max value among the keys 
        max_key = -1
        max_val = -1
        for key, value in map.items():
            if value > max_val:
                max_val = value
                max_key = key
        return max_key    
          
        '''
        # moore voting 
        # if there is a majority number, it will always lead, even if encounter other elms 
        # the worst case is each majority paris with no-major elms
        # and gets cancled. but n1-n2 >= 1 since n1 > n2
        candidate = -1
        cnt = 0
    
        for elm in nums:
            if cnt == 0:
                candidate = elm
                cnt += 1
            else:
                if candidate == elm:
                    cnt += 1
                else:
                    cnt -= 1
        return candidate
        
# @lc code=end