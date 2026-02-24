#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        citations.sort()
        h_max = 1
        for i in range(len(citations)):
            for j in range(len(citations)):
                if citations[j] >= h_max:
                    break 
                
            if len(citations) - j  >= h_max and citations[j] >= h_max:
                h_max += 1
            else:
                break
        return h_max - 1
        '''
        '''
        # n lg n 
        citations.sort()
        
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                return len(citations) - i
        return 0
        '''
        # optimal solution:
        bucket = [0] * (len(citations) + 1)
        # fill the bucket to count the each citation respetively
        for citation in citations:
            bucket[min(citation, len(citations))] += 1
        # Then check if the h_index is valid
        h_index = len(citations)
        cuml =  0
        for  j in range(len(citations), -1, -1 ):
            cuml += bucket[j]
            if cuml >= j:
                return j
            
        
# @lc code=end

