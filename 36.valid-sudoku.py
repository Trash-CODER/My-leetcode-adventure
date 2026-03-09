#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squre_hash_set = {} # or dict()
        for i in range(9): 
            squre_hash_set[i] = set()
        r , c = 0 , 0
        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                # check the row
                if (board[i][j] != '.'):
                    if(board[i][j] in row_set  ):
                        return False
                    else:
                        row_set.add(board[i][j])
                #check the col
                if (board[j][i] != '.'):
                    if(board[j][i] in col_set ):
                        return False
                    else:
                        col_set.add(board[j][i])
        for i in range(9):
            for j in range(9):
                square_num = (i//3)*3 + j//3
                if (board[i][j] != '.'):
                    if (board[i][j] in squre_hash_set[square_num]):
                        return False
                    else:
                        squre_hash_set[square_num].add(board[i][j])
                        
        return True
                    
                
                
                
                
                
        
# @lc code=end

