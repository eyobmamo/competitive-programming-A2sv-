class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        dis=0
        length=len(points)
        for i in range(length-1):
            minmum=min(abs( points[i][0] - points[i+1][0] ) , abs( points[i][1] - points[i+1][1] ))
            #print(minmum)
            remainder_d=max(abs( points[i][0] - points[i+1][0] ) , abs( points[i][1] - points[i+1][1] ))-minmum
           # print(r)
            dis+=(minmum+remainder_d)
        return (dis)


        