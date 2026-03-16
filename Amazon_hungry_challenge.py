from collections import Counter
class solution:
    def Min_hungry_diff(self, arr:list[int]) -> int:
        hunger = arr[1:]
        
        # meorization dic to speed up the code
        memo = {}
                
        def h_solver(N: int , hunger:list[int]) -> int:
            state = (N, tuple(hunger))
            if state in memo:
                return memo[state]
            
            min_val = get_diff(hunger)
            if N == 0 or min_val == 0:
                return min_val
            for i in range(1, len(hunger)):
                if hunger[i] > 0:
                    hunger[i] -= 1
                    res = h_solver(N - 1, hunger)
                    hunger[i]  += 1
                    min_val  = min(min_val, res)    
            memo[state] = min_val
            return min_val
                
                       
        def get_diff(hunger:list[int]) ->  int:
                re = 0
                for i in range(len(hunger) - 1):
                    re += abs(hunger[i+1] - hunger[i])
                return re
        return h_solver(arr[0], hunger)
    
    '''
    # top down(recusion) -> bottom up(dynamic programming)
    def get_diff(h):
            return sum(abs(h[i] - h[i+1]) for i in range(len(h)-1))

        # current_states stores: { (hunger_tuple): min_difference_found }
        current_states = {initial_hunger: get_diff(initial_hunger)}
        
        overall_min = current_states[initial_hunger]

        # Use a for loop to represent each sandwich being handed out
        for _ in range(N):
            next_states = {}
            
            for state, diff in current_states.items():
                # For each state, try giving a sandwich to each person
                h_list = list(state)
                for i in range(len(h_list)):
                    if h_list[i] > 0:
                        # Create the new state
                        h_list[i] -= 1
                        new_state = tuple(h_list)
                        new_diff = get_diff(h_list)
                        
                        # Optimization: Update the global min
                        overall_min = min(overall_min, new_diff)
                        
                        # Keep the state if it's new or has a better diff (though diff is fixed for a state)
                        if new_state not in next_states:
                            next_states[new_state] = new_diff
                        
                        # Backtrack the list for the next person in this round
                        h_list[i] += 1
            
            # If no more sandwiches can be given (all hunger 0), stop
            if not next_states:
                break
                
            # Move to the next "round" of sandwich distribution
            current_states = next_states
            
        return overall_min
    '''
    

if __name__ == "__main__":
    arr = [3, 2, 1, 0, 4, 1, 0]
    print(solution().Min_hungry_diff(arr))