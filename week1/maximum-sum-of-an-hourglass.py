class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row=len(grid)-2
        col=len(grid[0])-2
        maximum=0
        for r in range(row):
            for c in range(col):
                num=grid[0+r][0+c]+grid[0+r][1+c]+grid[0+r][2+c]+grid[1+r][1+c]+grid[2+r][0+c]+grid[2+r][1+c]+grid[r+2][2+c]
                maximum=max(num,maximum)
        return maximum        


        

        