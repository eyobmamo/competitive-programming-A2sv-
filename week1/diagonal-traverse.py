class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic={}
        dic=defaultdict(list)
        row=len(mat)
        col=len(mat[0])
        for n_r in range(row):
            for n_c in range(col):
                dic[n_r+n_c].append(mat[n_r][n_c])
        output=[]
        for k,v in dic.items():
            if k%2==0:
                output.extend(reversed(v))
            else:
                output.extend(v)    
        return output         



        