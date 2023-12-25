class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sumition=0
        if len(mat) %2 == 0:
            for i in range(len(mat)):
                sumition+=mat[i][i]
                sumition+=mat[len(mat)-1-i][i]
        else:
            for i in range(len(mat)):
                sumition+=mat[i][i]
                sumition+=mat[len(mat)-1-i][i]
            sumition-=mat[len(mat)//2][len(mat)//2] 
        return sumition          
            
        