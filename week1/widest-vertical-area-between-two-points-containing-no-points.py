class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = []
        for ele in points:
            arr.append(ele[0])
        arr = sorted(arr)

        maxDiff = 0
        i = 1

        while i < len(arr):
            if arr[i] - arr[i-1] >= maxDiff: maxDiff = arr[i] - arr[i-1]
            i += 1
        
        return maxDiff   

        