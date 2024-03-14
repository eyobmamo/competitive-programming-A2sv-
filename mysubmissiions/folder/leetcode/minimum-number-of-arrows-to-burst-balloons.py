class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x :x[0])
        print(points)
        end = points[0][1]
        arrow = 1
        for i in range(len(points)-1):
            if points[i+1][0] <= end and points[i+1][1] < end:
                end = points[i+1][1]
            elif points[i+1][0] > end :
                arrow += 1
                end = points[i+1][1] 
        return arrow           

        