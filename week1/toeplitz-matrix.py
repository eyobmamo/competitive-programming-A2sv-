class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row=len(matrix)
        column=len(matrix[0])
        count=0
        while count<row-1:
            if matrix[count][0:column-1]==matrix[count+1][1:column]:
                pass 
            else:
                return False
            count+=1    
        return True               

        