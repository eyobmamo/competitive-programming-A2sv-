class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix)
        col=len(matrix[0])
        transpos=[0]*col
        transpos[0]=[1,2,3,4]
        col_n=0
        print(transpos)
        while col_n<col:
            list1=[]
            for i in range(row):
                list1.append(matrix[i][col_n])
            transpos[col_n]=list1
            col_n+=1
        return transpos        
        