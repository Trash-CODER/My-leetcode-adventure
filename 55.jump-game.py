#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        # it is pretty complex
        def find_max( s:int, e: int ) -> int:
            max = 0
            while (s <= e):
                # one important thing, when they have same values
                # keep the one whose index is bigger (not right)
                
                # need to comapre index + corrspoding value
                if s + nums[s] >= max + nums[max]:
                    max = s
                s += 1
            return max
                
            
            
        current_index = 0
        pre_furthest_reach = 0
        cur_furthest_reach = nums[0]
        
        # the catch here is if current_idex/fur never reach 
        # to the final index, using them as the invariants might
        # lead to the inf loop
        
        # exception:
        if len(nums) == 1 or cur_furthest_reach >= len(nums)-1:
            return True
        
        while (pre_furthest_reach < cur_furthest_reach):
            next_index = find_max(current_index + 1, cur_furthest_reach)
            pre_furthest_reach = cur_furthest_reach
            cur_furthest_reach = next_index + nums[next_index]
            current_index = next_index
            if(cur_furthest_reach >= len(nums) - 1 ):
                return True
        
        return False 
        '''
        # simplifed version
        farthest_reach = 0
        
        for i in range(len(nums)):
            if i > farthest_reach:
                return False
            
            farthest_reach = max(farthest_reach, i + nums[i])
            
            if farthest_reach >= len(nums) - 1:
                return True
            
                
        
# @lc code=end

