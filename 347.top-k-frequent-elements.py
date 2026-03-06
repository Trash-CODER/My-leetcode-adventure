#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        hash_map = defaultdict(int)
        for num in nums:
            hash_map[num] = hash_map[num] + 1
        val = list(hash_map.items())
        val.sort(key = lambda x : x[1])
        output = []
        for i in range(k):
            output.append(val[len(val) - 1 - i][0])
        return output 
        '''
        # Abstract Data Type: Priority Queue
        # Min-heap
        # The heapq libary only implements min-heap
        # negate trick used here to make it served as a max-heap
        # "The heapq.heappush() method determines priority based on Python’s standard sequence comparison rules.
        # and it doesn't accept a key to determine the priority of the val
        heap = []
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n,0)   
        for key, val in counter.items():
            heapq.heappush(heap,(-val,key))
        res = []
        while (len(res) < k):
            res.append(heapq.heappop(heap)[1])
        return res

        
        
# @lc code=end

