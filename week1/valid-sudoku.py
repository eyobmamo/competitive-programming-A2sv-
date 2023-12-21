class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            cheak=set()
            for j in range(9):
                if board[i][j] != "." and  board[i][j] in cheak:
                    return False
                cheak.add(board[i][j])
        for i in range(9):
            cheakh=set()
            for j in range(9):
                if board[j][i] != "." and  board[j][i] in cheakh:
                    return False
                cheakh.add(board[j][i])
       
        rl,cl=1,1 
        while rl<4 and cl<4:
            cheakj=set()       
            for r_n in range(3*(rl-1),3*rl):
                for c_n in range(3*(cl-1),3*cl):
                    if board[r_n][c_n] != "." and board[r_n][c_n] in cheakj:
                        return False
                    cheakj.add(board[r_n][c_n])
            cl+=1
            if cl==4:
                rl+=1
                cl=0
        return True            




            

        

        