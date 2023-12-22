class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = matrix[::-1]
        for r in range(len(matrix)):
            for c in range(r,len(matrix[0])):
                matrix[r][c],matrix[c][r]=matrix[c][r],matrix[r][c]

            
        
    
        

        """
        Do not return anything, modify matrix in-place instead.
        """
        