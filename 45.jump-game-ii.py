#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
    
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
        if len(nums) == 1 :
            return 0
        if len(nums) - 1 <= cur_furthest_reach:
            return 1
        step = 0
        
        while (pre_furthest_reach < cur_furthest_reach):
            next_index = find_max(current_index + 1, cur_furthest_reach)
            pre_furthest_reach = cur_furthest_reach
            cur_furthest_reach = next_index + nums[next_index]
            current_index = next_index
            step += 1
            if(cur_furthest_reach >= len(nums) - 1 ):
                step += 1
                break
        return step
        '''
        # previous alg is too complex
        jumps = 0
        farthest = 0
        current_end = 0
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            # if the index reach previous farthest point 
            # then it must jump otherwise it would stuck in the current window
            if i == current_end :
                current_end = farthest
                jumps += 1
                # Made mistake here
                # this if block shold be nested in 
                # bcz shouldn't check this untill  the index hit ur farthest reach
                if farthest >= len(nums) - 1:
                    break
        return jumps
        
        
        
# @lc code=end

