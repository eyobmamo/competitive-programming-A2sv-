class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row=len(strs)
        col=len(strs[0])
        del_col=0
        for c in range(col):
            n_c=False
            for r in range(row-1):
                if ord(strs[r][c])>ord(strs[r+1][c]):
                    n_c=True
            if n_c:
                del_col +=1
        return del_col                

        