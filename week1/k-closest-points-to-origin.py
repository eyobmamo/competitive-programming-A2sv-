class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output=[]
        points.sort(key=lambda x: x[0]*x[0] +x[1]*x[1])
        #output.append(points[:k])
        return points[:k]
        