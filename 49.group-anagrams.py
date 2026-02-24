#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        group = []
        tmp_arr = []
        for str in strs:
            tmp_hash = {}
            for char in str:
                if char in tmp_hash:
                    tmp_hash[char] += 1
                else:
                    tmp_hash[char] = 0
            tmp_arr.append(tmp_hash)
        for i in range(len(tmp_arr)):
            sub_group = []
            if tmp_arr[i]  != None:
                sub_group.append(strs[i])
                for j in range(i+1, len(tmp_arr)):
                    if tmp_arr[i] == tmp_arr[j]:
                        sub_group.append(strs[j])
                        tmp_arr[j] = None
                group.append(sub_group)
        return group
        '''
        # sort all the string in the strings and then sort the strings
        hash_map= {}
        
        for str in strs:
            tmp_str = tuple(sorted(str))
            if tmp_str in hash_map:
                hash_map[tmp_str].append(str)
            else:
                tmp_arr = []
                tmp_arr.append(str)
                hash_map[tmp_str] = tmp_arr
        return list(hash_map.values())
        # the optimal solution is usig ASCII code 
        # use 26 size array to store the ASCII code and count the number which can be
        # used as key after it is turned into tuples
            
        
        
      
                    
            
        
# @lc code=end

