class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        rows=[0]*9
        cols=[0]*9
        subMat=[0]*9
        
        for i in range(9):
            for j in range(9):
            
             val=board[i][j]
            
             if val==".":
                val=0

             else:    
                val=int(board[i][j])

             
             if val==0:
                continue
             pos=1<<(val-1)

             if (rows[i] & pos):
                return False
             rows[i]|=pos
            
             if (cols[j] & pos):
                return False
             cols[j]|=pos

             idx=(i//3)*3 + (j//3)

             if (subMat[idx] & pos):
                return False
             subMat[idx]|=pos  

        return True  

            




        